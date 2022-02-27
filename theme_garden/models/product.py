#*-* coding utf-8 *-*
import logging
from odoo import models, fields, api


logger = logging.getLogger(__name__)


class Product(models.Model):
    _inherit = "product.template"

    regular_price = fields.Float('Regular Price',digits='Product Price', help="Regular price for product on webiste")



