{
    'name': 'Artists Theme',
    'description': 'Artists Theme - Art Galleries, Photography, Painting',
    'category': 'Theme/Retail',
    'sequence': 310,
    'version': '1.0',
    'author': 'Odoo SA',
    'depends': ['theme_monglia', 'website_animate'],
    'data': [
        'views/assets.xml',
        'views/customize_modal.xml',
        'views/images.xml',
        'views/preset.xml',
        'views/snippets.xml',
        'views/snippets/s_banner_parallax.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
    'images': [
        'static/description/artists_description.png',
    ],
    'price': 4,
    'currency': 'EUR',
    'live_test_url': 'https://theme-artists.odoo.com',
}
