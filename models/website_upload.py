from odoo import fields, models, api


class WebsiteUpload(models.Model):
    _name = 'website.upload'
    _description = 'Description'

    name = fields.Char(string='Name')
    description = fields.Char(string='Description')
    connection = fields.One2many('website.upload.file', 'connection_to_website_upload', string="File")


class WebsiteUploadFile(models.Model):
    _name = 'website.upload.file'
    _description = 'Description'

    connection_to_website_upload = fields.Many2one('website.upload')
    name = fields.Char(string='Name')
    description = fields.Char(string='Description')
    file = fields.Binary(string='File', required=True)
    file_url = fields.Char(string='File URL', readonly=True)


    @api.model
    def create(self, vals):
        # Call the original create() method to create the record
        record = super(WebsiteUploadFile, self).create(vals)

        if record.file and record.name:
            base_url = self.env['ir.config_parameter'].sudo().get_param('web.base.url')
            record.file_url = f"{base_url}/web/content/{record._name}/{record.id}/file/{record.name}"

        return record
