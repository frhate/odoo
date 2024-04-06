from odoo import models, fields, api

class PropertyBuilding(models.Model):
    _name = 'property.building'
    _description = 'Property Building Information'

    name = fields.Char(string='Name', required=True)
    project_id = fields.Many2one(comodel_name='project.project_info', string='Project', required=True,ondelete='cascade')
    hold_type_id = fields.Many2one(comodel_name='hold.type', string='Hold Type', required=True)
    state_id = fields.Many2one(comodel_name='res.country.state', string='State', required=True, ondelete='cascade')
    city_id = fields.Many2one(comodel_name='res.city', string='City', required=True, ondelete='cascade')
    land_no_id = fields.Char(string='Land No')
    municipality_no = fields.Char(string='Municipality No')

    # Building Names
    building_name = fields.Char(string='Building Name', required=True)
    arabic_name = fields.Char(string='Arabic Name', required=True)

    # Ejari Details
    ejari_building_name = fields.Char(string='Ejari Building Name', required=True)
    ejari_building_name_arabic = fields.Char(string='Ejari Arabic Name', required=True)
    ejari_building_area_size = fields.Float(string='Ejari Building Area Size', required=True)
    ejari_common_area_size = fields.Float(string='Ejari Common Area Size', required=True)
    ejari_leasable_area_size = fields.Float(string='Ejari Leasable Area Size', required=True)

    address = fields.Char(string='Address', required=True)
    unit_count = fields.Integer(string='Unit Count')
    completion_date = fields.Date(string='Completion Date')

    building_usage_ids = fields.Many2many(comodel_name='building.usage', string='Building Usage', required=True)
    building_type_id = fields.Many2one(comodel_name='building.type', string='Building Type', required=True)

    floor_count = fields.Integer(string='Floor Count')
    parking_count = fields.Integer(string='Parking Count')
    buid_area_size = fields.Float(string='Building Area Size')
    plot_area_size = fields.Float(string='Plot Area Size')
    leasable_area_size = fields.Float(string='Leasable Area Size')
    commom_area_size = fields.Float(string='Common Area Size')

    status = fields.Selection(string='Status', selection=[])  # Replace with your specific status options
    reference_number = fields.Char(string='Reference Number')
    approval_ref_no = fields.Char(string='Approval Reference No')
    active = fields.Boolean(string='Active', default=True)

    hold_type_id = fields.Many2one('projecto.project_info.hold_type', string='Hold Type')
    city_id = fields.Many2one('projecto.project_info.res.city', string='City')
    building_usage_ids = fields.Many2many('projecto.project_info.building.usage', string='Building Usage')
    building_type_id = fields.Many2one('projecto.project_info.building.type', string='Building Type')

