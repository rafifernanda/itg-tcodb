from odoo import fields, models


class EstatePropertyType(models.Model):

    # ---------------------------------------- Private Attributes ---------------------------------

    _name = "estate.property.type"
    _description = "Real Estate Property Type"
    _sql_constraints = [
        ("check_name", "UNIQUE(name)", "The name must be unique"),
    ]

    # --------------------------------------- Fields Declaration ----------------------------------

    # Basic
    name = fields.Char("Name", required=True)
    
    property_ids = fields.One2many("estate.property", "property_type_id", string="Properties")

