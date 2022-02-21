# -*- coding: utf-8 -*-

import base64
import io
from odoo import models


class PatientAppointmentXlsx(models.AbstractModel):
    _name = 'report.hospital.report_patient_appointment_xls'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, patients):
        sheet = workbook.add_worksheet('Appointment')
        bold = workbook.add_format({'bold': True})

        row = 0
        col = 0

        sheet.write(row, col, 'Referance', bold)
        sheet.write(row, col+1, 'Patient Name')

        for app in data['appointments']:
            row += 1
            sheet.write(row, col, app['name'], bold)
            sheet.write(row, col+1, app['patient_id'][1])






