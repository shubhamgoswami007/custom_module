from odoo import api, fields, models, _
from odoo.exceptions import ValidationError

class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "hospital patient"

    @api.model
    def default_get(self, fields):
        res = super(HospitalPatient, self).default_get(fields)
        res['note'] = 'NEW Patient Created'
        return res

    name = fields.Char(string='Name', required=True, tracking=True)
    reference = fields.Char(string='Order Reference', required=True, copy=False, readonly=True,index=True,
                            default=lambda self: _('New'))
    age = fields.Integer(string='Age',tracking=True)
    image = fields.Binary(string="Patient Image")
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'other'),
        ('kid', 'Kid')
    ], required=True, default='other',tracking=True)
    note = fields.Text(string='Description')
    state = fields.Selection([('draft', "draft"),
                              ('confirm', "Confirm"), ('done', "Done"), ('closed', "Closed")],
                             string="Status", default='draft',tracking=True)

    responsible_id = fields.Many2one('res.partner', string="Responsible")
    appointment_id = fields.One2many('hospital.appointment','patient_id',string="Appointment")
    appointment_count = fields.Integer(string='Appointment Count', compute='_compute_appointment_count')

    def _compute_appointment_count(self):
        for rec in self:
            appointment_count = self.env['hospital.appointment'].search_count([('patient_id', '=', rec.id)])
            rec.appointment_count = appointment_count

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
        if vals.get('reference', _('New')) == _('New'):
            vals['reference'] = self.env['ir.sequence'].next_by_code('hospital.patient') or _('New')
        res = super(HospitalPatient, self).create(vals)
        return res

    @api.constrains('name')
    def check_name(self):
        for rec in self:
            patients = self.env['hospital.patient'].search([('name', '=', rec.name), ('id', '!=', rec.id)])
            if patients:
                raise ValidationError(_("Name %s Already Exists" % rec.name))

    @api.constrains('age')
    def check_age(self):
        for rec in self:
            if rec.age == 0:
                raise ValidationError(_("Age Cannot Be Zero .. !"))

    def name_get(self):
        result = []
        for rec in self:
            name = '[' + rec.reference + '] ' + rec.name
            result.append((rec.id, name))
        return result

    def action_open_appointments(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Appointments',
            'res_model': 'hospital.appointment',
            'domain': [('patient_id', '=', self.id)],
            'context': {'default_patient_id': self.id},
            'view_mode': 'tree,form',
            'target': 'current',
        }
