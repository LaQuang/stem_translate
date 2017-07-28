# -*- coding: utf-8 -*-
from odoo import http

# class StemTranslate(http.Controller):
#     @http.route('/stem_translate/stem_translate/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/stem_translate/stem_translate/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('stem_translate.listing', {
#             'root': '/stem_translate/stem_translate',
#             'objects': http.request.env['stem_translate.stem_translate'].search([]),
#         })

#     @http.route('/stem_translate/stem_translate/objects/<model("stem_translate.stem_translate"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('stem_translate.object', {
#             'object': obj
#         })