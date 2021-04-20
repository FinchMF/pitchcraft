
import core
import dash_core_components as dcc
import dash_html_components as html


standard_layout=html.Div(
    children=[
        html.H1('PitchCraft'),
        html.H3('Choose Starting Frequency'),
        dcc.Input(id='input-freq',
                    type='number',
                    value=440.0,
                    placeholder='Base Frequency'),
        dcc.Input('input-base',
                    type='number',
                    value=6,
                    placeholder='Base Root'),
        html.H3('Choose Interval System and Size'),
        dcc.Input(id='input-sys',
                    type='text',
                    value='semi tone',
                    placeholder='Interval System'),
        dcc.Input(id='input-sys-size',
                    type='number',
                    value=88,
                    placeholder='System Size'),
        html.H3('Choose Wav Type'),
        dcc.Input(id='input-form',
                    type='text',
                    value='sine',
                    placeholder='wav form'),
        html.Hr(),
        html.H3('Make Samples'),
        html.Button('Generate',
                    id='make-command', n_clicks=0),
        html.Br(),
        html.A(id='download-link', children='Download Samples')
],
className='container')

core.APP.layout=standard_layout