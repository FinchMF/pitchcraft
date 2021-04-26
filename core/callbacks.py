import core
from dash.dependencies import Input, Output, State

APP = core.APP

@APP.callback(
    Output('input-sys-size', 'value'),
    [Input('input-sys', 'value')],
    prevent_initial_callback=True
)
def set_sysSize(input_sys):

    return core.util.Systems.octave_systems[input_sys]

@APP.callback(
    Output('download-link', 'href'),
    [Input('make-command', 'n_clicks')],
    state=[
        State('input-freq', 'value'),
        State('input-sys', 'value'),
        State('input-sys-size', 'value'),
        State('input-form', 'value')
    ],
    prevent_initial_callback=True
)
def system_samples(n_clicks, in_freq,
                    in_sys, in_sys_size, in_form):
    
    core.generator.Hz().update(in_sys.replace(' ', '_'))

    PITCH = core.generator.Hz(hz=in_freq)
    PITCH.system_size = in_sys_size

    if not core.os.path.exists('sample_packages'):
        core.os.mkdir('sample_packages')

    for ii, freq in PITCH.make_system().items():

        core.generator.Wav(carrier_hz=freq).make_wav(in_form)
    
    core.make_archive('samples', 'zip', 'sample_packages')

    wavs = [w for w in core.os.listdir('sample_packages') if w.endswith('.wav')]
    for w in wavs:
        core.os.remove(core.os.path.join('sample_packages', w))
    
    return 'downloads/samples.zip'