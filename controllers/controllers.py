# -*- coding: utf-8 -*-
# from odoo import http


# class Programaventas(http.Controller):
#     @http.route('/programaventas/programaventas/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/programaventas/programaventas/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('programaventas.listing', {
#             'root': '/programaventas/programaventas',
#             'objects': http.request.env['programaventas.programaventas'].search([]),
#         })

#     @http.route('/programaventas/programaventas/objects/<model("programaventas.programaventas"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('programaventas.object', {
#             'object': obj
#         })
