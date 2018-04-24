# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models
from odoo.tools.float_utils import float_compare




class AccountInvoice(models.Model):
    _inherit = "account.invoice"

    @api.onchange('team_id')
    def _set_operating_unit_line(self):
        for line in self.invoice_line_ids:
            line.operating_unit = self.team_id.operating_unit_id

    @api.model
    def invoice_line_move_line_get(self):
        res = []
        for line in self.invoice_line_ids:
            if line.quantity == 0:
                continue
            tax_ids = []
            for tax in line.invoice_line_tax_ids:
                tax_ids.append((4, tax.id, None))
                for child in tax.children_tax_ids:
                    if child.type_tax_use != 'none':
                        tax_ids.append((4, child.id, None))
            analytic_tag_ids = [(4, analytic_tag.id, None) for analytic_tag in line.analytic_tag_ids]

            move_line_dict = {
                'invl_id': line.id,
                'type': 'src',
                'name': line.name.split('\n')[0][:64],
                'price_unit': line.price_unit,
                'quantity': line.quantity,
                'price': line.price_subtotal,
                'account_id': line.account_id.id,
                'product_id': line.product_id.id,
                'uom_id': line.uom_id.id,
                'account_analytic_id': line.account_analytic_id.id,
                'tax_ids': tax_ids,
                'invoice_id': self.id,
                'operating_unit': line.operating_unit.id,
                'analytic_tag_ids': analytic_tag_ids
            }
            if line['account_analytic_id']:
                move_line_dict['analytic_line_ids'] = [(0, 0, line._get_analytic_line())]
            res.append(move_line_dict)
        return res

    @api.model
    def line_get_convert(self, line, part):
        return {
            'date_maturity': line.get('date_maturity', False),
            'partner_id': part,
            'name': line['name'],
            'debit': line['price'] > 0 and line['price'],
            'credit': line['price'] < 0 and -line['price'],
            'account_id': line['account_id'],
            'analytic_line_ids': line.get('analytic_line_ids', []),
            'amount_currency': line['price'] > 0 and abs(line.get('amount_currency', False)) or -abs(
                line.get('amount_currency', False)),
            'currency_id': line.get('currency_id', False),
            'quantity': line.get('quantity', 1.00),
            'product_id': line.get('product_id', False),
            'operating_unit': line.get('operating_unit', False),
            'product_uom_id': line.get('uom_id', False),
            'analytic_account_id': line.get('account_analytic_id', False),
            'invoice_id': line.get('invoice_id', False),
            'tax_ids': line.get('tax_ids', False),
            'tax_line_id': line.get('tax_line_id', False),
            'analytic_tag_ids': line.get('analytic_tag_ids', False),
        }


class InvoiceLine(models.Model):
    _inherit = "account.invoice.line"

    operating_unit = fields.Many2one('operating.unit','Operating Unit')

    @api.onchange('product_id')
    def _set_operating_unit(self):
        if self.invoice_id.team_id:
            self.operating_unit = self.invoice_id.team_id.operating_unit_id

    @api.multi
    def _get_analytic_line(self):
        ref = self.invoice_id.number
        return {
            'name': self.name,
            'operating_unit': self.operating_unit.id,
            'date': self.invoice_id.date_invoice,
            'account_id': self.account_analytic_id.id,
            'unit_amount': self.quantity,
            'amount': self.price_subtotal_signed,
            'product_id': self.product_id.id,
            'product_uom_id': self.uom_id.id,
            'general_account_id': self.account_id.id,
            'ref': ref,
        }

