{
    'name': 'Evaluación de desempeño',
    'version': '1.0',
    'summary': 'Módulo para gestionar el desempeño de cada empleado',
    'category': 'Productivity',
    'author': 'Cloe Romero Salguero',
    'website': 'https://tuweb.com',
    'license': 'LGPL-3',
    'depends': ['base', 'mail'],
    'icon': '/evaluacion_desempeno/static/description/iconodesempeno.png',
    'data': [
        'views/evaluacion_desempeno_views.xml',
        'security/ir.model.access.csv',
    ],

    'assets': {
        'web.assets_backend': [
            'evaluacion_desempeno/static/src/css/styles.css',  # Note la eliminación del slash inicial
        ],
    },
    'application': True,
    'installable': True,
    'auto_install': False,
    'description': """
    Módulo de Odoo para la gestión del desempeño de cada empleado
    """
}