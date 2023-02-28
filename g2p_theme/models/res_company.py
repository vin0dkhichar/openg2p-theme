import base64

from odoo import models, tools
from odoo.modules.module import get_resource_path


class ResCompany(models.Model):
    _inherit = "res.company"

    def get_g2p_favicon(self):
        img_path = get_resource_path("g2p_theme", "static/img/favicon.png")
        with tools.file_open(img_path, "rb") as f:
            return base64.b64encode(f.read())
