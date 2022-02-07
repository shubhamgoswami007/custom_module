from odoo import api, fields, models, _

class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "hospital patient"

    name = fields.Char(string='Name', required=True, tracking=True)
    reference = fields.Char(string='Order Reference', required=True, copy=False, readonly=True,index=True,
                            default=lambda self: _('New'))
    age = fields.Integer(string='Age',tracking=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'other')
    ], required=True, default='other',tracking=True)
    note = fields.Text(string='Description')
    state = fields.Selection([('draft', "draft"),
                              ('confirm', "Confirm"), ('done', "Done"), ('closed', "Closed")],
                             string="Status", default='draft',tracking=True)

    responsible_id = fields.Many2one('res.partner', string="Responsible")
    appointment_id = fields.One2many('hospital.appointment','patient_id',string="Appointment")


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