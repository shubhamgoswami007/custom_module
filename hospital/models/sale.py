from odoo import api, fields, models

class SaleOrder(models.Model):
    _inherit = "sale.order"

    sale_descripton = fields.Char(string='Sale Descripton')