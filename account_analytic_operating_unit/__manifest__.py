# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    "author": "Rapidsoft",
    'name': 'Account Analytic Operating Unit',
    'version': '1.0',
    'category': 'Accounting',
    'description': """
Set configuration for create analytic entries based on operating units
==============================================

Allows to add operating units to the following models:
----------------------------------------------------------------------
    * Purchase Order Line
    * Account Invoice Line
    * Account Analytic Line
    * Account Move Line
    
Create groups and filters on the analytic entries form,tree and pivot for operating units 

Also required the following modules (OCA):
    * operating_unit
    * sales_team_operating_unit
From repo: https://github.com/oca/operating-unit
    """,
    'website': 'https://www.rapidsoft.com.py',
    'depends': ['account','operating_unit','purchase'],
    'data': [
        'views/account_analytic_view.xml',
        'views/purchase_order_view.xml',
        'views/account_invoice_view.xml',
    ],
    'installable': True,
}
