from odoo import api, fields, models, _


class DepartmentModelDepartment(models.Model):
    _name = "department.department"
    _description = "Department department"
    # _rec_name = 'Company'

    name = fields.Char(string='Department Name', required=True)
    Company = fields.Char(string="Company Name")
    Date = fields.Datetime(sting="Date")
    reference = fields.Char(string='Order Reference', required=True, copy=False, readonly=True,index=True,
                            default=lambda self: _('New'))

    Employee_id = fields.One2many('employee.employee', 'Department_id', string="Employee Name")

    @api.model
    def create(self, vals):
        if vals.get('reference', _('New')) == _('New'):
            vals['reference'] = self.env['ir.sequence'].next_by_code('department.department') or _('New')
        res = super(DepartmentModelDepartment, self).create(vals)
        return res
