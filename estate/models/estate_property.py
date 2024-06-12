from odoo import models, fields
from dateutil.relativedelta import relativedelta

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Real Estate Property"

    def _default_avail(self):
        return fields.Date.context_today(self) + relativedelta(months=3)

    name = fields.Char("Title", required=True)
    description = fields.Text("Description")
    postcode = fields.Char("Post Code")
    date_availability = fields.Date("Date Availablility", copy=False, default=lambda self: self._default_avail())
    expected_price = fields.Float("Expected Price", required=True)
    selling_price = fields.Float("Selling Price", readonly=True, copy=False)
    bedrooms = fields.Integer("Bedrooms", default=2)
    living_area = fields.Integer("Living Area")
    facades = fields.Integer("Facades")
    garage = fields.Boolean("Garage")
    garden = fields.Boolean("Garden")
    garden_area = fields.Integer("Garden Area")
    garden_orientation = fields.Selection(
        selection=[
            ("N", "North"),
            ("S", "South"),
            ("E", "East"),
            ("W", "West"),
            ],
            string="Garden Orientation")
    active = fields.Boolean("Active", default=True)
    state = fields.Selection(
        selection=[
            ("new", "New"),
            ("offer_received", "Offer Received"),
            ("offer_accepted", "Offer Accepted"),
            ("sold", "Sold"),
            ("canceled", "Canceled"),
        ],
        required=True,
        copy=False,
        default="new"
    )
    property_type_id = fields.Many2one("estate.property.type")
    buyer_id = fields.Many2one("res.partner", copy=False, string="Buyer")
    user_id = fields.Many2one("res.users", string="Salesperson", default= lambda self: self.env.user)
    offer_ids = fields.One2many("estate.property.offer", "property_id", string="Offers")
    tag_ids = fields.Many2many("estate.property.tag", string="Tags")

