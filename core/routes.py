from core import server, APP, layout
app=server

@app.route('/')
def index():
    return layout.index_layout(APP)