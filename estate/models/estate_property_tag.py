from odoo import fields, models


class EstatePropertyType(models.Model):

    # ---------------------------------------- Private Attributes ---------------------------------

    _name = "estate.property.tag"
    _description = "Real Estate Property Tag"

    # --------------------------------------- Fields Declaration ----------------------------------

    name = fields.Char("Name", required=True)
