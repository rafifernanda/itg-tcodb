from odoo import fields, models


class EstatePropertyOffer(models.Model):

    # ---------------------------------------- Private Attributes ---------------------------------

    _name = "estate.property.offer"
    _description = "Real Estate Property Offer"

    # --------------------------------------- Fields Declaration ----------------------------------

    price = fields.Float("Price", required=True)
    state = fields.Selection(
        selection=[
            ("accepted", "Accepted"),
            ("refused", "Refused"),
        ],
        string="Status",
        copy=False,
        default=False,
    )

    # Relational
    partner_id = fields.Many2one("res.partner", string="Partner", required=True)
    property_id = fields.Many2one("estate.property", string="Property", required=True)

    property_type_id = fields.Many2one(
        "estate.property.type", related="property_id.property_type_id", string="Property Type", store=True
    )
    