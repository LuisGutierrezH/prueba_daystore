# -*- coding: utf-8 -*-
{
    'name': 'Prueba técnica DayStore',
    'summary': """ Módulo de rifa para empleados""",
    'author': 'Luis Fernando Gutiérrez',
    'depends': ['base', 'hr', 'hr_attendance', 'stock', 'product'],
    "data": [
        "security/ir.model.access.csv",
        "data/raffle_sequence.xml",
        "views/employee.xml",
        "views/product_template.xml",
        "views/menu.xml",
        "views/raffle_history.xml",
        #"wizard/raffle_wizard_views.xml",
    ],
    'application': True,
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
