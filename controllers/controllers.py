# -*- coding: utf-8 -*-
# from odoo import http


# class GoldShop(http.Controller):
#     @http.route('/gold_shop/gold_shop/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/gold_shop/gold_shop/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('gold_shop.listing', {
#             'root': '/gold_shop/gold_shop',
#             'objects': http.request.env['gold_shop.gold_shop'].search([]),
#         })

#     @http.route('/gold_shop/gold_shop/objects/<model("gold_shop.gold_shop"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gold_shop.object', {
#             'object': obj
#         })
