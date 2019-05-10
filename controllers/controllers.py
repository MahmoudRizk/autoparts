# -*- coding: utf-8 -*-
import logging
from werkzeug.exceptions import Forbidden, NotFound

from odoo import http, tools, _

# class Autoparts(http.Controller):
#     @http.route('/autoparts/autoparts/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/autoparts/autoparts/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('autoparts.listing', {
#             'root': '/autoparts/autoparts',
#             'objects': http.request.env['autoparts.autoparts'].search([]),
#         })

#     @http.route('/autoparts/autoparts/objects/<model("autoparts.autoparts"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('autoparts.object', {
#             'object': obj
#         })