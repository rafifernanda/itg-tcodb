from odoo import fields, models, api, _


class EstatePropertyType(models.Model):

    # ---------------------------------------- Private Attributes ---------------------------------

    _name = "estate.property.type"
    _description = "Real Estate Property Type"
    _order = "sequence, name"
    _sql_constraints = [
        ("check_name", "UNIQUE(name)", "The name must be unique"),
    ]

    # --------------------------------------- Fields Declaration ----------------------------------

    # Basic
    name = fields.Char("Name", required=True)
    sequence = fields.Integer("Sequence", default=10)
    
    # Relational
    property_ids = fields.One2many("estate.property", "property_type_id", string="Properties")

    # Computed (for stat button)
    offer_count = fields.Integer(string="Offers Count", compute="_compute_offer_count")
    offer_ids = fields.One2many("estate.property.offer", "property_type_id")

    # ---------------------------------------- Compute methods ------------------------------------

    @api.depends("offer_ids")
    def _compute_offer_count(self):
        for rec in self:
            rec.offer_count = len(rec.offer_ids)

    # ---------------------------------------- Action Methods -------------------------------------

    def action_view_offers(self):
        return {
            "name": _("Property Offers"),
            "type": "ir.actions.act_window",
            "view_mode": "tree",
            "res_model": "estate.property.offer",
            "domain": [("id", "in", self.offer_ids.ids)],
        }

