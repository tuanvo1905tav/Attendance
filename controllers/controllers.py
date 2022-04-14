# -*- coding: utf-8 -*-
# from odoo import http


# class Project-attendance(http.Controller):
#     @http.route('/project-attendance/project-attendance', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/project-attendance/project-attendance/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('project-attendance.listing', {
#             'root': '/project-attendance/project-attendance',
#             'objects': http.request.env['project-attendance.project-attendance'].search([]),
#         })

#     @http.route('/project-attendance/project-attendance/objects/<model("project-attendance.project-attendance"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('project-attendance.object', {
#             'object': obj
#         })
