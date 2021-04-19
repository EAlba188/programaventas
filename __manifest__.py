# -*- coding: utf-8 -*-
{
    'name': "programaventas",

    'summary': """Un programa de ventas cojonudo""",

    'description': """
        El mejor programa de ventas jamas visto
    """,

    'author': "Eden Alba",
    'website': "https://github.com/EAlba188/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/producto.xml',
        'views/cliente.xml',
        'views/venta.xml',
        'views/historico.xml',
        'wizards/productWizard.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
