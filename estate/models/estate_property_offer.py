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
    partner_id = fields.Many2one("Partner ID", required=True)