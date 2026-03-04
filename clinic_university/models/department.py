from odoo import models, fields

class ClinicDepartment(models.Model):
    _name = 'clinic.department'
    _description = 'clini cDepartment'
    _rec_name = 'name'

    name = fields.Char(string='Department Name', required=True)
    code = fields.Char(string='Department Code', required=True)
    specialty_ids = fields.One2many(
     'clinic.specialty.line',
        'line_id',
        string='Specialties'
    )


class CLinicLine(models.Model):

    _name ="clinic.specialty.line"
    
    line_id = fields.Many2one('clinic.department',string="Clinic")

    specialty_id = fields.Many2one('clinic.specialty',string="Specialty")


