
from scipy import signal as sg 
from scipy.io.wavfile import read, write
import numpy as np
import util

from typing import List, Dict, TypeVar
RANGE = TypeVar('range')


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

        if modulator:

            envelope = ac * (1.0 + ka * modulator)
            modulated = envelope * carrier
            modulated *= 0.3
            modulated_data = np.int16(modulated * 32767)
            write(f"modulated_{hz}_{wav_type}.wav", rate=sr, data=modulated_data)

        carrier *= 0.3
        data = np.int16(carrier * 32767)
        write(f"simple_{hz}_{wav_type}.wav", rate=sr, data=data)


class Wav:

    _duration: float = 10.0
    _duty: float = 0.8
    _sr: int = 44100
    _modulator_hz: float = 0.25
    _ac: float = 1.0
    _ka: float = 0.25

    def __init__(self, carrier_hz: float=util.pitch_to_hz['A'][4]):


        self.__hz = carrier_hz
        self.__sr = Wav._sr
        self.__duration = Wav._duration
        self.__duty = Wav._duty
        self.__modulator = np.sin(2 * np.pi * Wav._modulator_hz * ((self.__sr * self.__duration)/self.__sr))
        self.__t_samples = np.arange(self.__sr * self.__duration)
        self.__wav = 2 * np.pi * self.__hz * self.__t_samples / self.__sr

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
    def modulator(self):
        return self.__modulator

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

    def make_wav(self, wav_type: str, modulated: bool=False):

        if wav_type == 'sine':

            if modulated:

                Factory._make_wav(carrier=self.sin_carrier, sr=self.sr,
                            hz=self.hz, wav_type=wav_type, modulator=self.modulator, 
                            ac=Wav._ac, ka=Wav._ka)

            else:

                Factory._make_wav(carrier=self.sin_carrier, sr=self.sr, 
                        hz=self.hz, wav_type=wav_type)

        elif wav_type == 'sqaure':

            if modulated:

                Factory._make_wav(carrier=self.sq_carrier, sr=self.sr,
                            hz=self.hz, wav_type=wav_type, modulator=self.modulator, 
                            ac=Wav._ac, ka=Wav._ka)

            else:

                Factory._make_wav(carrier=self.sq_carrier, sr=self.sr,
                        hz=self.hz, wav_type=wav_type)

        elif wav_type == 'square_duty':

            if modulated:

                Factory._make_wav(carrier=self.sq_duty_carrier, sr=self.sr,
                            hz=self.hz, wav_type=wav_type, modulator=self.modulator, 
                            ac=Wav._ac, ka=Wav._ka)

            else:

                Factory._make_wav(carrier=self.sq_duty_carrier, sr=self.sr,
                        hz=self.hz, wav_type=wav_type)

        elif wav_type == 'sawtooth':

            if modulated:

                Factory._make_wav(carrier=self.sawtooth_carrier, sr=self.sr,
                            hz=self.hz, wav_type=wav_type, modulator=self.modulator, 
                            ac=Wav._ac, ka=Wav._ka)

            else:
                    
                Factory._make_wav(carrier=self.sawtooth_carrier, sr=self.sr,
                        hz=self.hz, wav_type=wav_type)

