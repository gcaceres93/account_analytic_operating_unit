# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models



class AccountAnalytic(models.Model):
    _inherit = "account.analytic.line"

    operating_unit = fields.Many2one('operating.unit','Operating Unit')


