# -*- coding: utf-8 -*-
{
    'name': 'Campos adicionales para Leads',
    'summary': """ Este modulo permite añadir campos personalizados a los Leads """,
    'author': 'Andresow',
    'depends': ['base', 'crm','iap_crm'],
    "data": [
        "reports/proposal_honours.xml",
        "reports/payment_complete.xml",
        "reports/report.xml",
        "security/ir.model.access.csv",
        "views/crm_lead_views.xml",
    ],
    'application': True,
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
