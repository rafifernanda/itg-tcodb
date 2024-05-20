from odoo import models

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Real Estate Property"

    name = fields.Char("Title", required=True)
    description = fields.Text("Description")
    postcode = fields.Char("Post Code")
    date_availability = fields.Date("Date Availablility")
    expected_price = fields.Float("Expected Price", required=True)
    selling_price = fields.Float("Selling Price")
    bedrooms = fields.Integer("Bedrooms")
    living_area = fields.Integer("Living Area")
    facades = fields.Integer("Facades")
    garages = fields.Boolean("Garages")
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
