# -*- coding: utf-8 -*-

from werkzeug import utils

from odoo import http
from odoo.http import request


class WebsiteUpload(http.Controller):

    @http.route('/web/website_upload', auth='public')
    def index(self, **kw):
        my_data = request.env['website.upload.file'].sudo().search([])
        return request.render('website_upload.website_upload_page', {
            'my_data': my_data
        })


    @http.route('/mgrlog', type='http', auth='public', website=True)
    def my_page(self, **kw):
        return utils.redirect('http://www2.teamglac.com/mgrlog/')
