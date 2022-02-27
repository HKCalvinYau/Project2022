# -*- coding: utf-8 -*-
from odoo import models, fields, api


class GuestSharing(models.Model):
    _name = 'guest.sharing'

    name = fields.Char("Title")
    g_image = fields.Binary("Image")
    description = fields.Html("Description")
    customer = fields.Char("By")

    

