# -*- coding: utf-8 -*-
{
    'name': "gold_shop",

    'summary': """
        Manage gold alloys and other stuff""",

    'description': """
    """,

    'author': "Vee",
    'website': "",
    'category': 'Extra Tools',
    'version': '14.0.0.1',
    'depends': ['base','sale','hr','mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/main_view.xml',
        'views/templates.xml',
        'views/transfers.xml',
        'views/partners.xml',
        'data/sequence.xml',
        'data/gold_data.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
}
