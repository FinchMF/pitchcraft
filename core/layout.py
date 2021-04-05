
import core
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

core.APP.layout=html.Div(
    children=[
        html.H1('PitchCraft'),
        html.H3('Please Choose Starting Frequency'),
        dcc.Input(id='input-freq',
                    type='number',
                    placeholder=440.0),
        dcc.Input(id='input-sys',
                    type='text',
                    placeholder='semi tone'),
],
className='container')
