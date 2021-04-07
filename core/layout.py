
import core
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

core.APP.layout=html.Div(
    children=[
        html.H1('PitchCraft'),
        html.H3('Choose Starting Frequency'),
        dcc.Input(id='input-freq',
                    type='number',
                    placeholder=440.0),
        dcc.Input('input-base',
                    type='number',
                    placeholder=6),
        html.H3('Choose Interval System and Size'),
        dcc.Input(id='input-sys',
                    type='text',
                    placeholder='semi tone'),
        dcc.Input(id='input-sys-size',
                    type='number',
                    placeholder=88),
        html.H3('Choose Wav Type'),
        dcc.Input(id='input-form',
                    type='text',
                    placeholder='sine'),
        html.Hr(),
        html.H3('Make Samples'),
        html.Button('Generate',
                    id='make-command', n_clicks=0)
],
className='container')
