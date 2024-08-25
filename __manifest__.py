# -*- coding: utf-8 -*-
{
    "name": "website_upload",
    "summary": """
    Website Extension that can automatically upload a file and have a route to access even if not logged in.
        """,
    "description": """
        To easily upload a file and generate links to it. it have a custom routes .. yourlink/web/website_upload
    """,
    "author": "Marksuuuu",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    "category": "Website",
    "version": "0.1",
    # any module necessary for this one to work correctly
    "depends": ["website", "base"],
    # always loaded
    "data": [
        "security/ir.model.access.csv",
        "views/website_upload_view.xml",
        "views/uploaded_files_view.xml",
        "views/menu.xml",
        "views/templates.xml",
    ],
    # only loaded in demonstration mode
    "demo": [
        "demo/demo.xml",
    ],
    "license": "LGPL-3",
}
