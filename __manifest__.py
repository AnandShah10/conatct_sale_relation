# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'contact_sale_relation',
    'version': '1.0',
    'summary': "Contact Sale relation module",
    'sequence': 10,
    'author': "anand",
    'description': """
Contact Sale relation (many2many)
""",
    'category': 'Custom/Relation',
    'website': 'https://www.odoo.com',
    'depends': ['base', 'contacts','sale'],
    'data': [
        'views/views.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
