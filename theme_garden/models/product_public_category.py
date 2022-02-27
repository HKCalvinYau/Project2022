#*-* coding utf-8 *-*
from odoo import models
from odoo.addons.http_routing.models.ir_http import slug




class PublicCategory(models.Model):
    _inherit = "product.public.category"

    def get_category_url(self):
        return  "/shop/category/%s" % slug(self)

    




