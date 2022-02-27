# -*- coding: utf-8 -*-
import random

from odoo import models, fields, api


class GardenConfig(models.Model):
    _name = 'garden.config'

    name = fields.Char("Name", default="Theme Garden Configurations")
    banner_image = fields.Binary("Banner Image")
    banner_text = fields.Char('Banner Text', defualt="TIME TO SPRING")
    banner_text_color = fields.Char("Banner Text Color", default="#FFFFFF")
    banner_text_background_color = fields.Char("Banner Text Background Color (Tranperent : #ffffff00)", default="#ffffff00" )
    button_text = fields.Char("Button Text", default="SHOP NOW")
    button_text_color = fields.Char("Button Text Color", default="#000000")
    button_text_background_color = fields.Char("Button Color", default="#FFFFFF")

    show_f_product = fields.Boolean("Show Featured Product", default=True)
    top_category_product_ids = fields.Many2many("product.public.category", 'product_table','pre_id','att_id', string="Top Products of Categories")

    show_top_collections = fields.Boolean("Show Top Collections", default=True)
    top_collections_ids = fields.Many2many('product.public.category', 'category_table','pre_id','att_id', string="Top 3 Collections")

    show_blog_featured = fields.Boolean("Blog Post", default=True)
    show_guest_post   = fields.Boolean("From our Guest", default=True)
    
    featured_collection =  fields.Many2many('product.public.category', 'featured_category_table','pre_id','att_id', string="Featured Collection")


    def get_top_2_categories(self):
        if self.top_category_product_ids:
            categories = self.top_category_product_ids
            data = {}
            for item in categories:
                category_products = self.env["product.template"].search([("public_categ_ids", "in", [item.id])], limit=4)
                data[item] = category_products
            return data
        else:
            categories = self.env["product.public.category"].search([], limit=2)
            data = {}
            for item in categories:
                category_products = self.env["product.template"].search([("public_categ_ids", "in", [item.id])], limit=4)
                data[item] = category_products
            return data

    @api.model
    def get_top_3_collections(self):
        if self.top_collections_ids:
            categories = self.top_collections_ids
            data = {}
            for item in categories:
                category_product = self.env["product.template"].search([("public_categ_ids", "in", [item.id])], limit=1)
                if category_product:
                    data[item] = category_product
                else:
                    data[item] = False
            return data
        else:
            categories = self.env["product.public.category"].search([], limit=4)
            data = {}
            for item in categories:
                category_product = self.env["product.template"].search([("public_categ_ids", "in", [item.id])], limit=1)
                if category_product:
                    data[item] = category_product
                else:
                    data[item] = False
            return data

    def get_featured_collection(self):
        if self.featured_collection:
            categories = self.featured_collection
            data = {}
            for item in categories[0]:
                category_products = self.env["product.template"].search([("public_categ_ids", "in", [item.id])], limit=4)
                data[item] = category_products
            return data

    #get random 4 products you may like
    def get_random_4_products(self):
        products = self.env["product.template"].search([])
        random_products = []
        if products:
            randomlist = []

            if len(products) > 4:
                last = 4
            else:
                last = len(products)

            for i in range(0, last):
                n = random.randint(0,len(products)-1)
                randomlist.append(n)
            
            for index in randomlist:
                random_products.append(products[index])

        return random_products



class WebsiteMenu(models.Model):
    _inherit = 'website.menu'
    footer_control = fields.Selection([('only_footer', 'Footer(Gardenia Floral Studio)'),
                                ('t_c_footer', 'Footer(Terms & Conditions)'),
                                ('t_c_header_footer', 'Footer(Header, Terms & Conditions )'),
                                ('none', 'None')], string="Footer Control")
    is_terms_and_cond_menu = fields.Boolean("#")
    is_store = fields.Boolean("Is Store?", default=False)


    def get_menu_categories(self):
        #check if each category as product
        category_ids = []
        categories = self.env["product.public.category"].search([])
        for item in categories:
            category_product = self.env["product.template"].search([("public_categ_ids", "in", [item.id])])
            if category_product:
                category_ids.append(item)
        return category_ids
            




    
    










    

