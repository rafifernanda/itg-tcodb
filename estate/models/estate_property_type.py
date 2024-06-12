from odoo import fields, models

class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "Estate Property Model"

    name = fields.Char("Name", required=True)