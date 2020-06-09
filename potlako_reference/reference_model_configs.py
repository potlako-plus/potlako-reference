from edc_reference import site_reference_configs

site_reference_configs.register_from_visit_schedule(
    visit_models={
        'edc_appointment.appointment': ['potlako_subject.subjectvisit']})

configs = {
    'potlako_subject.cliniciancallfollowup': ['transport_support', 'investigation_ordered'],
    'potlako_subject.patientcallinitial': ['transport_support'],
    'potlako_subject.patientcallfollowup': ['transport_support', 'investigation_ordered'],
    'potlako_subject.missedvisit': ['transport_support']
}

for reference_name, fields in configs.items():
    site_reference_configs.add_fields_to_config(
        name=reference_name, fields=fields)
