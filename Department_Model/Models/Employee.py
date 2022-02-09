from odoo import api, fields, models, _


class DepartmentModelEmployee(models.Model):
    _name = "employee.employee"
    _description = "Department Employee"

    name = fields.Char(string='Employee Name', required=True)
    age = fields.Integer(string='Age')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'other')
    ], required=True, default='male')
    Experiance = fields.Text(string='Description')
    Date = fields.Datetime(sting="Joining Date")
    reference = fields.Char(string='Order Reference', required=True, copy=False, readonly=True, index=True,
                            default=lambda self: _('New'))
    Department_id = fields.Many2one('department.department', string="Department Name")

    @api.model
    def create(self, vals):
        if not vals.get('Experiance'):
            vals['Experiance'] = 'Experiance'
        if vals.get('reference', _('New')) == _('New'):
            vals['reference'] = self.env['ir.sequence'].next_by_code('employee.employee') or _('New')
        res = super(DepartmentModelEmployee, self).create(vals)
        return res
