# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Department Models',
    'version': '1.0',
    'summary': 'simple Department Models',
    'sequence': 30,
    'description': """simple Department Models""",
    'category': 'Tools',
    'website': '',
    'depends': [
        'base'
    ],
    'data': [
        'Security/ir.model.access.csv',
        'Data/data.xml',
        'Views/Department_views.xml',
        'Views/Employee_views.xml'
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
