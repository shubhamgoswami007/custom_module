from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class HospitalAppointment(models.Model):
    _name = "hospital.appointment"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Hospital Appointment"
    _order = "doctor_id,name,age"

    name = fields.Char(string='Order Reference', required=True, copy=False, readonly=True, index=True,
                       default=lambda self: _('New'))
    note = fields.Text(string='Description')
    age = fields.Integer(string='Age', related='patient_id.age', tracking=True)
    state = fields.Selection([('draft', "draft"),
                              ('confirm', "Confirm"), ('done', "Done"), ('closed', "Closed")],
                             string="Status", default='draft', tracking=True)
    patient_id = fields.Many2one('hospital.patient', string="Patient", required=True)
    prescription_line_ids = fields.One2many('appointment.prescription.lines', 'appointment_id', string="Prescription Line")
    date_appointment = fields.Date(string="Date")
    date_time = fields.Datetime(string="Date Time")
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'other')
    ], string="Gender")
    prescription = fields.Text(string="Doctor Prescription")
    doctor_id = fields.Many2one('hospital.doctor',string="Doctor Name")

    def action_confirm(self):
        self.state = "confirm"

    def action_done(self):
        self.state = 'done'

    def action_closed(self):
        self.state = 'closed'

    def action_draft(self):
        self.state = 'draft'

    @api.model
    def create(self, vals):
        if not vals.get('note'):
            vals['note'] = 'new patient'
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('hospital.appointment') or _('New')
        res = super(HospitalAppointment, self).create(vals)
        return res

    @api.onchange('patient_id')
    def onchange_patient_id(self):
        if self.patient_id:
            if self.patient_id.gender:
                self.gender = self.patient_id.gender
            if self.patient_id.note:
                self.note = self.patient_id.note
        else:
            self.gender = ''
            self.note = ''

    def unlink(self):
        if self.state == 'done':
            raise ValidationError(_("You Cannot Delete %s as it is in Done State" % self.name))
        return super(HospitalAppointment, self).unlink()


class AppointmentPrescriptionLine(models.Model):
    _name = "appointment.prescription.lines"
    _description = "Appointment Prescription Line"

    name = fields.Char(string="Medicine",required=True)
    qty = fields.Integer(string="Quantity")
    appointment_id = fields.Many2one('hospital.appointment',string="Appointment")
