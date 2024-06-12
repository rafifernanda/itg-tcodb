from odoo import models, fields

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