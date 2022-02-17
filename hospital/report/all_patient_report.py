from odoo import api, fields, models, _


class AllPatientReport(models.AbstractModel):
    _name = 'report.hospital.report_all_patient_details'
    _description = 'Patient Report'

    @api.model
    def _get_report_values(self, docids, data=None):
        domain = []
        gender = data.get('form_data').get('gender')
        age = data.get('form_data').get('age')
        if gender:
            domain += [('gender', '=', gender)]
        if age != 0:
            domain += ['age', '=', age]
        docs = self.env['hospital.patient'].search(domain)
        return {
            'docs': docs,
        }
