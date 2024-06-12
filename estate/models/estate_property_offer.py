from dateutil.relativedelta import relativedelta
from odoo import api, models, fields

class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "Estate Property Offer"

    
    price = fields.Float("Price")
    status = fields.Selection([
        ("accepted", "Accepted"),
        ("refused", "Refused")
    ],
    string="Status"
    )
    partner_id = fields.Many2one("res.partner",required=True)
    property_id = fields.Many2one("estate.property",required=True)
    property_type_id = fields.Many2one("estate.property.type", related="property_id.property_type_id",string="Property Type", store=True)
    validity = fields.Integer(string="Validity", default=7)
    date_deadline = fields.Date(compute="_compute_validity",string="Deadline", inverse="_inverse_date_deadline")

    @api.depends("create_date", "validity")
    def _compute_validity(self):
        for rec in self:
            date = rec.create_date.date() if rec.create_date else fields.Date.today()
            rec.date_deadline = date + relativedelta(days=rec.validity)

    def _inverse_date_deadline(self):
        for rec in self:
            date = rec.create_date.date() if rec.create_date else fields.Date.today()
            rec.validity = (rec.date_deadline - date).days

