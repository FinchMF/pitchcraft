
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

        html.H3('Choose Interval System and Size'),

        dcc.Dropdown(id='input-sys',
                    options= [
                        {'label': i, 'value': i,}
                        for i in core.util.Systems.tones.keys()
                    ],
                    value='semi_tone',
                    placeholder='Interval System',
                    style={
                        'width': '45%'
                    }),

        dcc.Dropdown(id='input-sys-size',
                    options=[
                        {'label': i, 'value': i,}
                        for i in core.util.Systems.octave_systems.values()
                    ],
                    value=88,
                    placeholder='System Size',
                    style={
                        'display': 'inline-block',
                        'width': '45%'
                    }),

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