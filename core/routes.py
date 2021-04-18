from core import server, APP, layout
app=server

@app.route('/system')
def system_build():
    return 'System page'
