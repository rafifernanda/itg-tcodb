from odoo import fields, models

class EstatePropertyOffer(models.Model):
	_name = "estate.propery.offer"
	_description = "Real Estate Propery Offer"

	price = fields.Float("Price", required=True)
	state = fields.Selection(
		selection=[
		("accepted", "Accepted"),
		("refused", "Refused")
		],
		string="Status",
		copy=False,
		default=False
	)

	partner_id = fields.Many2one("res.partner", string="Partner", require=True)
	property_id = fields.Many2one("estate.property", string="Property", required=True)