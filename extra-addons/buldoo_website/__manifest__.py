{
    "name": "Buldoo Website",
    "version": "1.0",
    "category": "Website",
    "summary": "Landing page Buldoo",
    "depends": ["website"],
    "data": [
        "views/landing_page.xml",
        "views/menu.xml",
    ],
    "assets": {
        "web.assets_frontend": [
            "buldoo_website/static/css/landing.css",
        ],
    },
    "installable": True,
    "application": False,
}
