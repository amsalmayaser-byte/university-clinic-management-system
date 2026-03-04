from odoo import models, fields

class ClinicSpecialty(models.Model):
    _name = 'clinic.specialty'
    _description = 'clinic Specialty'
    _rec_name = 'name'

    name = fields.Char(string='Specialty Name', required=True)
    code = fields.Char(string='Specialty Code', required=True)
    consultation_charge = fields.Float(string='Consultation Charge', required=True)
    department_id = fields.Many2one(
        'clinic.department',
        string='Department',
        required=False
    )
