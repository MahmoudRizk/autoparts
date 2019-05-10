# -*- coding: utf-8 -*-
{
    'name': "autoparts",

    'summary': """
        Modifying search bar in eCommerce app, allowing to search with both Product or Category.""",

    'description': """
        Solution for the task asked to build something like https://autopartsegypt.com website.
        Modifying search bar in eCommerce app, allowing to search with both Product or Category. 
    """,

    'author': "Mahmoud Rizk",
    'website': "mahmoudahmedrizk@gmail.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'web', 'website_sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/resources.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}