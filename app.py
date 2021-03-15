
import base64
import os
from urllib.parse import quote as urlquote

import dash
import dash_core_components as dcc 
import dash_html_components as html
from dash.dependencies import Input, Output

from flask import Flask, send_from_directory

import util

PACKAGE_DIRECTORY = './sample_packages'

if not os.path.exists(PACKAGE_DIRECTORY):
    os.makedirs(PACKAGE_DIRECTORY)

server = Flask(__name__)
app = dash.Dash(server=server)

server.route("/download/<path:path>")

app.layout = html.Div(
    [
        dcc.Input(
            id="pitch-intake",
            type="number",
            placeholder="Starting Hz"
        ),
        dcc.Dropdown(
            id="system-base-unit",
            placeholder="System Interval",
            options= [
                {"label": i, "value": i} 
                for i in util.Systems.tones.keys()
            ]
        ),
        dcc.Dropdown(
            id="system-size",
            placeholder="System Size",
            options=[
                {"label": i, "value": i}
                for i in util.Systems.tones.values()
            ]
        ),
        dcc.Dropdown(
            id="system-type",
            options= [
                {"label": "make interval system series", "value": "make system"},
                {"label": "make overtone series", "value": "make overtone"},
                {"label": "make octave series", "value": "make octave"}
            ],
            placeholder="System Type",
            multi=True

        )
    ]
)




if __name__ == "__main__":
    app.run_server(debug=True)

