from core import server, APP, layout
app=server

@app.route('/')
def index():
    return layout.Design.index_layout(APP)

@app.route('/system')
def system_build():
    return layout.Design.sys_layout(APP)