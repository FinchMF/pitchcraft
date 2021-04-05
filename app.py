from core import APP, server

server=server
APP.title = "PitchCraft"

if __name__ == "__main__":
    APP.run_server(debug=True)