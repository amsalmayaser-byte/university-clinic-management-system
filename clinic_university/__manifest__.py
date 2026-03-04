{
    'name': 'University Clinic',
    'version': '1.0',
    'summary': 'Manage basic patient profiles for University Clinic',
    'description': 'Create and manage patient profiles (basic info only) for university clinic.',
    'category': 'Healthcare',
    'depends': ['base'],
    'data': [
        'views/clinic_patient_sequence.xml',
        'security/ir.model.access.csv',
        'views/clinic_patient_views.xml',
        'views/clinic_structure_views.xml',
    ],
    'installable': True,
    'application': True,
}
