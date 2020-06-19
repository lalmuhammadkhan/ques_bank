# -*- coding: utf-8 -*-
{
    'name': "ques_bank",

    'summary': """
        Questions Objective + Subjective Bank
        """,

    'description': """
        Questions Bank
    """,

    'author': "786Solution",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail', 'report_xlsx', 'board', 'web_timeline',  'web_notify'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'data/auto_increment_sequence.xml',
        'views/views.xml',
        'views/templates.xml',
        'views/grades.xml',
        'views/subjects.xml',
        'views/sections_chapter.xml',
        'views/chapters_units.xml',
        'views/topics.xml',
        'views/cognitive_levels.xml',
        'views/item_types.xml',
        'views/scheme_of_assesment_slos.xml',
        'views/options.xml',
        'views/items_objective.xml',
        'views/items_subjective.xml',
        'views/settings.xml',
        # 'views/custom_users.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
