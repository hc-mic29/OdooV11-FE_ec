# -*- coding: utf-8 -*-
from openerp import models, fields, api


class ProcurementOrder(models.Model):
    _inherit = 'procurement.order'

    @api.multi
    def propagate_wave(self, wave, order):
        if order.mrp_production_request_id:
            order.mrp_production_request_id.write({'wave_id': wave, })
        return super(ProcurementOrder, self).propagate_wave(wave, order)

class StockPickingWave(models.Model):
    _inherit = 'stock.picking.wave'

    # Production request generated by a procurement on the wave.
    procurement_production_request_ids = fields.One2many('mrp.production.request', 'wave_id', string='Production Requests', )
