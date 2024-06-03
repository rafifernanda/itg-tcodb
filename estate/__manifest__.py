# -*- coding: utf-8 -*-
# More info at https://www.odoo.com/documentation/master/reference/module.html

{
    "name": "Real Estate",
    "category": 'Real Estate/Brokerage',
    "version": "17.0.1.0.0",
    "depends": [
        "base", 
		"mail",
    ],
    "data": [
        "views/estate_property_views.xml",
		"views/estate_property_type_views.xml",
		"views/estate_property_offer_views.xml",
		"views/estate_property_tag_views.xml",
        "views/estate_menus.xml",
        "views/res_users_views.xml",

        "security/res_groups.xml",
        "security/ir.model.access.csv",

        "data/demo.xml",
    ],
    "application": True,
    'license': 'LGPL-3',
}
