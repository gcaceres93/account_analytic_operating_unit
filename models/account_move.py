# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models



class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    operating_unit = fields.Many2one('operating.unit','Operating Unit')

    @api.one
    def _prepare_analytic_line(self):
        """ Prepare the values used to create() an account.analytic.line upon validation of an account.move.line having
            an analytic account. This method is intended to be extended in other modules.
        """
        amount = (self.credit or 0.0) - (self.debit or 0.0)
        return {
            'name': self.name,
            'date': self.date,
            'account_id': self.analytic_account_id.id,
            'tag_ids': [(6, 0, self.analytic_tag_ids.ids)],
            'unit_amount': self.quantity,
            'product_id': self.product_id and self.product_id.id or False,
            'product_uom_id': self.product_uom_id and self.product_uom_id.id or False,
            'amount': self.company_currency_id.with_context(date=self.date or fields.Date.context_today(self)).compute(
                amount, self.analytic_account_id.currency_id) if self.analytic_account_id.currency_id else amount,
            'general_account_id': self.account_id.id,
            'ref': self.ref,
            'move_id': self.id,
            'user_id': self.invoice_id.user_id.id or self._uid,
            'operating_unit': self.operating_unit.id
        }



