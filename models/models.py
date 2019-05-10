# -*- coding: utf-8 -*-

from odoo import models, fields, api
import requests

class autoparts(models.Model):
    _name = 'autoparts.autoparts'

    @api.model
    def test_search(self):
        result = {'category_id': '',
                  'product': '',
                 }
        if self._context['category']:
            result['category_id'] = self.env['product.public.category'].search([('name', 'ilike', self._context['category'])])._ids[0]

        result['product'] = self._context['product']
        return result

