# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Hospital Managemant',
    'version': '1.0',
    'summary': 'Hospital Managemant System',
    'sequence': 10,
    'description': """Hospital Managemant System""",
    'category': 'Tools',
    'website': 'https://Hospitalmangemant.com',
    'depends': [
        'sale',
        'portal',
        'utm',
        'mail'
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/data.xml',
        'wizard/create_appointment_view.xml',
        'views/patient.xml',
        'views/kids.xml',
        'views/Patient_gender.xml',
        'views/Appointment.xml',
        'views/sale.xml'

    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}