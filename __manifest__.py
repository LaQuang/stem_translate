# -*- coding: utf-8 -*-
{
    'name': "STEM Translate",

    'summary': 'Translate',

    'description': """
        This module provides management of translating document materials from LMS
    """,

    'author': "anh.bui",
    'website': "http://dtt.vn",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Education',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'openeducat_lms'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/translate_request.xml',
        'views/your_translations.xml',
        'views/menu.xml',
        'views/material_version_workflow.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}