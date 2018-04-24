# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    "author": "Eficent, "
              "Serpent Consulting Services Pvt. Ltd.,"
              "Rapidsoft.."
              "Odoo Community Association (OCA)",
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
----------------------------------------------------------------------
Create groups and filters on the analytic entries form,tree and pivot for operating units 
    """,
    'website': 'https://www.rapidsoft.com.py',
    'depends': ['account','operating_unit','purchase','sale_team_operating_unit'],
    'data': [
        'views/account_analytic_view.xml',
        'views/purchase_order_view.xml',
        'views/account_invoice_view.xml',
    ],
    'installable': True,
}
