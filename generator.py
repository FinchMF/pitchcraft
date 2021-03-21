
from scipy import signal as sg 
from scipy.io.wavfile import read, write
import numpy as np
import util
import matplotlib.pyplot as plt 
from typing import List, Dict, Union, TypeVar
RANGE = TypeVar('range')
FIG = TypeVar('matplotlib.figure.Figure')


class Hz:
    """
    Hz object recieves a frequency 
    and develops dynamic pitch systems
    """
    # sets the system's base interval unit
    tone_intvl='semi_tone'

    def __init__(self, hz: float=None):

        """
        Constructor develops three systems:
            - octave interval system (system of interval divison within one octave)
            - interval system of divisions
            - octave system used to measure natural system size given 8 octaves
        """

        self.__hz = hz
        self.__intervals=util.Network.make_octave_interval_system(tone_intvl=Hz.tone_intvl)
        self.__interval_system=util.Systems.interval_systems[Hz.tone_intvl]
        self.__system_size=util.Systems.octave_systems[Hz.tone_intvl]
    
    @property
    def hz(self):
        return self.__hz

    @hz.setter
    def hz(self, hz: float):
        self.__hz = hz

    @property
    def interval_system_base_unit(self):
        return self.__interval_system

    @property
    def system_size(self):
        return self.__system_size
    
    @property
    def intervals(self):
        return self.__intervals

    @classmethod
    def tone_interval(cls):
        return cls.tone_intvl

    @classmethod
    def update(cls, interval_type: str):
        cls.tone_intvl=interval_type


    def make_octaves(self, n_octaves: int) -> List[float]:

        """
        Dynamically generates octave's frequencies
        ------------------------------------------
        Receives:
            - Starting Hz
            - number of desired octaves to generate 
        Return:
            - a list of frequencies that correspond to each octave
            respective to the number of octaves chosen above the 
            starting Hz
        """

        return util.Network.make_octaves(hz=self.hz, n_octaves=n_octaves)

    def make_system(self, system_size: int=None) -> Dict[str, float]:

        """
        Dynamically generates chromatic system's frequencies
        ----------------------------------------------------
        Recieves:
            - Starting Hz
            - System size (
                ie number of chromatic frequencies 
                from the the starting Hz moving up divisions
                based on the root interval system desired
                )
        Returns:
            - Dictionary of Frequency Positions and corresponding Frequencies
        """
        # if system size is not chosen, the deafult system size inherent
        # in the root interval system will be chosen
        system_size = self.system_size if system_size == None else system_size

        return util.Network.make_system(hz=self.hz, system_type=self.interval_system_base_unit, 
                                                    system_size=system_size)

    def make_overtone_series(self, system_size: RANGE=range(0, 16)) -> List[float]:

        """
        Dynamically generates Overtone Series' frequencies
        --------------------------------------------------
        Recieves:
            - Starting Hz
            - System Size (default to 16 partials)
        Returns:
            - List of 16 frequencies respective of the starting Hz
            corresponding to the harmonic series
        """

        return util.Network.make_overtone_series(hz=self.hz, system_size=system_size)

class Factory:
    @staticmethod
    def _make_wav(carrier: List[float], sr: int, hz: float, wav_type: str, 
                modulator: List[float]=None, ac: float=None, ka: float=None):

        """
        Dynamically generates tone as wav file
        --------------------------------------
        Recieves:
            - Starting Hz
            - Carrier array
            - Sample Rate
            - Wav Form Type
            - Modulator Carrier Hz
            - AC
            - KA
        Return:
            - Returns nothing as a function but saves a wav file
            based on the dictating data
        """
        # currently there is the option to overlay
        # a modulation envelope over the tone 
        if modulator:
            # construct the envelope pattern
            envelope = ac * (1.0 + ka * modulator)
            # develop the modulated data, passing it through the envelope
            modulated = envelope * carrier
            modulated *= 0.3 # the severity of the modualtion
            # generate the tone
            modulated_data = np.int16(modulated * 32767)
            write(f"modulated_{hz}_{wav_type}.wav", rate=sr, data=modulated_data)
        # if no modulation desired, a consistent tone is generated
        carrier *= 0.3 # the amplitude of the wav
        data = np.int16(carrier * 32767)
        write(f"simple_{hz}_{wav_type}.wav", rate=sr, data=data)

    @staticmethod
    def show_signal(wav_data: Union[List[float], 
                              Dict[str, List[float]]], zoom: int=500) -> FIG:
        """
        Generates graph showing wave form
        ---------------------------------
        Recieves:
            - wav data
        Returns:
            - graph
        """
        multi_signal = {
            "sine":"red",
            "square":"blue",
            "square_duty":"purple",
            "sawtooth":"green",
            "triangle":"yellow"
        }
        fig = plt.figure()
        plt.rcParams['figure.facecolor'] = 'black'
        plt.rcParams['axes.facecolor'] = 'black'

        if type(wav_data) == dict:

            for wav_type, data in wav_data.items():
                plt.plot(data[:zoom], color=multi_signal[wav_type])
        else:
            plt.plot(wav_data[:zoom], color='red')

        plt.close()

        return fig

class Wav:

    """
    Wav object recieves a frequency,
    constructs a wav form
    and saves the audio as a wav file
    """
    # sets wav constructing factors
    _duration: float = 10.0 # in seconds
    _duty: float = 0.8
    _sr: int = 44100
    _modulator_hz: float = 0.25
    _ac: float = 1.0
    _ka: float = 0.25

    def __init__(self, carrier_hz: float=util.Transform.pitch_to_hz['A'][4]):

        """
        Constructor develops necessary components to generate wav form and wav file
        ---------------------------------------------------------------------------
        Default Hz is A4 (440.0hz)
        """
        self.__hz = carrier_hz
        self.__sr = Wav._sr
        self.__duration = Wav._duration
        self.__duty = Wav._duty
        self.__modulator = np.sin(2 * np.pi * Wav._modulator_hz * ((self.__sr * self.__duration)/self.__sr))
        self.__t_samples = np.arange(self.__sr * self.__duration)
        self.__wav = 2 * np.pi * self.__hz * self.__t_samples / self.__sr
        self.__W = {
            'sine': self.sin_carrier,
            'square': self.sq_carrier,
            'square_duty': self.sq_duty_carrier,
            'sawtooth': self.sawtooth_carrier,
            'triangle': self.triangle_carrier
        }

    # ~~~~ object configurations ~~~~~
    @property
    def sr(self):
        return self.__sr
    
    @sr.setter
    def sr(self, sr):
        self.__sr = sr
    
    @property
    def hz(self):
        return self.__hz

    @hz.setter
    def hz(self, carrier_hz):
        self.__hz = carrier_hz

    @property
    def duration(self):
        return self.__duration

    @duration.setter
    def duration(self, duration):
        self.__duration = duration

    @property
    def duty(self):
        return self.__duty

    @duty.setter
    def duty(self, duty):
        self.__duty = duty

    @property
    def t_samples(self):
        return self.__t_samples
    
    @property
    def wav(self):
        return self.__wav
    
    @property
    def sin_carrier(self):
        return np.sin(self.wav)

    @property
    def sq_carrier(self):
        return sg.square(self.wav)

    @property
    def sq_duty_carrier(self):
        return sg.square(self.wav, self.duty)

    @property
    def sawtooth_carrier(self):
        return sg.sawtooth(self.wav)

    @property
    def triangle_carrier(self):
        return np.abs(sg.sawtooth(self.wav))

    @property
    def modulator(self):
        return self.__modulator
    
    @property
    def W(self):
        return self.__W

    @classmethod
    def update_duration(cls, duration: float):
        cls._duration = duration

    @classmethod
    def update_duty(cls, duty: float):
        cls._duty = duty

    @classmethod
    def update_samplerate(cls, sr: int):
        cls._sr = sr

    @classmethod
    def update_modulator_hz(cls, modulator_hz: float):
        cls._modulator_hz = modulator_hz

    @classmethod
    def update_ac(cls, ac: float):
        cls._ac = ac 

    @classmethod
    def update_kc(cls, ka: float):
        cls._ka = ka

    # ~~~~ object functionality ~~~~
    def make_wav(self, wav_type: str, modulated: bool=False):

        """
        Generates Wav File
        ------------------
        Recieves:
            - wav form type
            - boolean switch if modulation desired
        Returns:
            - Generated Wav File
        """

        if modulated:
            # if modulation is turned on, necessary components are automatically added
            Factory._make_wav(carrier=self.W[wav_type], sr=self.sr,
                        hz=self.hz, wav_type=wav_type, modulator=self.modulator, 
                        ac=Wav._ac, ka=Wav._ka)

        else:
            # if modulation is not declared, a persistant tone is generated
            Factory._make_wav(carrier=self.W[wav_type], sr=self.sr, 
                    hz=self.hz, wav_type=wav_type)

    def show_wav(self, wav_type: str, zoom: int=500) -> FIG:

        """
        Generates a visual representation of the signal
        -----------------------------------------------
        """
        if wav_type == 'all': 
            wav_data=self.W

        else: 
            wav_data = self.W[wav_type]

        return Factory.show_signal(wav_data=wav_data, zoom=zoom)