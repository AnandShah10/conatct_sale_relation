from odoo import models, fields, api, _


class Contact(models.Model):
    _inherit = 'res.partner'

    sale_order_ids = fields.Many2many('sale.order', string='Sale Orders')


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    partner_ids = fields.Many2many('res.partner', string="Partners")

