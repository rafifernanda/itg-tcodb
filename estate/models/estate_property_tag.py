from odoo import fields, models


class EstatePropertyTag(models.Model):

    # ---------------------------------------- Private Attributes ---------------------------------

    _name = "estate.property.tag"
    _description = "Real Estate Property Tag"
    _sql_constraints = [
        ("check_name", "UNIQUE(name)", "The name must be unique"),
    ]

    # --------------------------------------- Fields Declaration ----------------------------------

    name = fields.Char("Name", required=True)
    color = fields.Integer("Color Index")

