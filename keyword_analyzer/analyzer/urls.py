from keyword_analyzer.analyzer import views

layout = [
    {
        'rule': '/',
        'view_func': views.index,
        'methods': ['GET']
    },
    {
        'rule': '/get_statistics/',
        'view_func': views.get_statistics,
        'methods': ['POST']
    }
]
