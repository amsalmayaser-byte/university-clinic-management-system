from odoo import models, fields

class ClinicDoctor(models.Model):
    _name = 'clinic.doctor'
    _description = 'clinic Doctor'
    _rec_name = 'doctor_name'

    doctor_name = fields.Char(string="Doctor Name", required=True)
    doctor_code = fields.Char(string="Doctor Code", required=True)

    department_id = fields.Many2one(
        'clinic.department',
        string="Department",
        required=True
    )

    specialty_ids = fields.Many2many(
        'clinic.specialty',
        string="Specialties",
        required=True
    )

    qualification = fields.Char(string="Qualification")
    experience_years = fields.Integer(string="Experience Years")
    consultation_charge = fields.Float(string="Consultation Charge")
    phone = fields.Char(string="Phone", required=True)
    email = fields.Char(string="Email", required=True)