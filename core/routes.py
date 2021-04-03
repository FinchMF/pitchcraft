from core import APP, layout

@APP.route('/')
def index():
    return layout.index_layout(APP)