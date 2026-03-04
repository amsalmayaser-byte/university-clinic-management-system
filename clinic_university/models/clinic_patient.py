from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import date
from dateutil import relativedelta

class ClinicPatient(models.Model):
    _name = 'clinic.patient'
    _description = 'Patient Profile'
    _rec_name = 'full_name'  

     # ===== Full Name =====
    first_name = fields.Char(string='First Name', required=True)               
    middle_name = fields.Char(string='Middle Name')                                     
    last_name = fields.Char(string='Last Name', required=True)                   
    family_name = fields.Char(string='Family Name')                                       
    full_name = fields.Char(string='Full Name', compute='_compute_full_name', store=True)  

    @api.depends('first_name', 'middle_name', 'last_name', 'family_name')
    def _compute_full_name(self):
        for rec in self:
            # Combine all name parts in one line, ignoring empty fields
            names = filter(None, [rec.first_name, rec.middle_name, rec.last_name, rec.family_name])
            rec.full_name = ' '.join(names)

    # ===== General Patient Info =====
    mrn = fields.Char(string='MRN', readonly=True)  
    birth_date = fields.Date(string='Birth Date', required=True) 
    age = fields.Integer(string='Age', compute='_compute_age', store=True)  
    gender = fields.Selection([('male','Male'),('female','Female')], string='Gender', required=True)  
    phone = fields.Char(string='Phone')  
    email = fields.Char(string='Email') 
    address = fields.Char(string='Address', required=True)                   
    patient_type = fields.Selection([
        ('student','Student'),         
        ('professor','Professor'),      
        ('employee','Employee'),       
        ('employee_child','Employee Child'),                    
        ('other','Other')           
    ], string='Patient Type', required=True)
    university_id = fields.Char(string='University ID')  

    # ===== Medical Info =====
    blood_type = fields.Selection([
        ('A+', 'A+'), ('A-', 'A-'),
        ('B+', 'B+'), ('B-', 'B-'),
        ('AB+', 'AB+'), ('AB-', 'AB-'),
        ('O+', 'O+'), ('O-', 'O-')
    ], string='Blood Type')   
    chronic_diseases = fields.Text(string='Chronic Diseases')  
    allergies = fields.Text(string='Allergies')  
    previous_surgeries = fields.Text(string='Previous Surgeries')  

    # ===== Compute Age =====
    @api.depends('birth_date')
    def _compute_age(self):
        for rec in self:
            if rec.birth_date:
                today = date.today()
                rec.age = relativedelta.relativedelta(today, rec.birth_date).years
            else:
                rec.age = 0

    # ===== MRN Auto-Generation & Automatic res.partner Creation =====
    @api.model
    def create(self, vals):
        # Auto-generate MRN if not provided
        if not vals.get('mrn'):
            seq = self.env['ir.sequence'].next_by_code('clinic.patient.mrn') or 'MRN00001'
            vals['mrn'] = seq

        patient = super().create(vals)

        # Automatically create a res.partner record for the patient
        self.env['res.partner'].create({
            'name': patient.full_name,  
            'email': patient.email,
            'phone': patient.phone,
            'customer_rank': 1,  
        })

        return patient