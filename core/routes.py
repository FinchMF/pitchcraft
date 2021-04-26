from core import server, APP, layout, os, send_from_directory

@server.route('/system')
def system_build():
    return 'System page'

@server.route('/downloads/<path:path>')
def serve_static(path):
    root_dir = os.getcwd()
    print(root_dir)
    return send_from_directory(
        os.path.join(root_dir), path
    )

@server.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(server.root_path, 'assets'),
                                'favicon.ico', mimetype='image/vnd.microsoft.icon')