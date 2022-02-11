from odoo import api, fields, models, _

class CreateAppointmentWizard(models.TransientModel):
    _name = "create.appointment.wizard"
    _description = "Create Appointment Wizard"

    name = fields.Char(string='Name', required=True)
    patient_id = fields.Many2one('hospital.patient', string="Patient", required=True)

    def action_create_appointment(self):
        vals = {
            'patient_id': self.patient_id.id,
            'doctor_id': 2,
            'date_appointment': self.date_appointment
        }
        appointment_rec = self.env['hospital.appointment'].create(vals)
        return {
            'name': _('Appointment'),
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'hospital.appointment',
            'res_id': appointment_rec.id,
        }

    @api.model
    def default_get(self, fields):
        res = super(CreateAppointmentWizard, self).default_get(fields)
        if self._context.get('active_id'):
            res['patient_id'] = self._context.get('active_id')
        return res