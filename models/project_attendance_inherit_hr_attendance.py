from odoo import fields, models, api


class HrAttendance(models.Model):
    _inherit = 'hr.attendance'
    _description = 'Description'

    fk_employee = fields.Many2one(comodel_name='hr.employee', string='Employee name')
