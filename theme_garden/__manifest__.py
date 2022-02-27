#*-* coding utf-8 *-*
{
    'name': 'Gardenia Floral Theme',
    'description': 'Gardenia Floral Theme shipped to Odoo.',
    'version': '1.0',
    'author': 'X',
    'data': [   
                'data/garden_config.xml',
                'views/product.xml',
                'views/layout.xml',
    			'views/submenu.xml',
                'views/blog.xml',
                'views/guest_sharing.xml',
                'views/header.xml',
                'views/footer.xml',
                'views/home.xml',
                'views/shop.xml',
    		    'views/assets.xml',
    		    'views/about.xml',
                'views/delivery_info.xml',
                'views/media_coverage.xml',
                'views/workshop.xml',
                'views/contact.xml',
                'views/login.xml',
                'views/signup.xml',
                'views/terms_conditions.xml',
                'security/ir.model.access.csv',
                ],

       
                
    'category': 'Theme/Creative',
    'depends': ['website', 'website_sale', 'website_blog', 'portal', 'product_line_control'],
}