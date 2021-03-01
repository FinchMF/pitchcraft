
from scipy import signal as sg 
from scipy.io.wavfile import read, write
import numpy as np
import util

from typing import List, Dict, TypeVar
RANGE = TypeVar('range')


class Hz:

    tone_intvl='semi_tone'
    intervals=util.Network.make_octave_interval_system(tone_intvl=tone_intvl)
    interval_system=util.Systems.interval_systems[tone_intvl]
    system_size=util.Systems.octave_systems[tone_intvl]

    def __init__(self, hz: float):

        self.__hz = hz
    
    @property
    def hz(self):
        return self.__hz

    @hz.setter
    def hz(self, hz: float):
        self.__hz = hz

    @classmethod
    def update_root_interval(cls, interval_type: str):

        cls.tone_intvl=interval_type


    def make_octaves(self, n_octaves: int) -> List[float]:

        return util.Network.make_octaves(hz=self.hz, n_octaves=n_octaves)

    def make_system(self, system_type: float=Hz.interval_system,
                          system_size: RANGE=range(Hz.system_size)) -> Dict[str, float]:

        return util.Network.make_system(hz=self.hz, system_type=system_type, system_size=system_size)

    def make_overtone_series(self, system_size: RANGE=range(0, 16)) -> List[float]:

        return util.Network.make_overtone_series(hz=self.hz, system_size=system_size)



def __make_wav(carrier: List[float], sr: int, hz: float, wav_type: str, 
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

    duration: float = 10.0
    duty: float = 0.8
    sr: int = 44100
    modulator_hz: float = 0.25
    ac: float = 1.0
    ka: float = 0.25

    def __init__(self, carrier_hz: float=util.pitch_to_hz['A'][4]):


        self.__hz = carrier_hz
        self.__sr = Wav.sr
        self.__duration = Wav.duration
        self.__duty = Wav.duty
        self.__modulator = np.sin(2 * np.pi * Wav.modulator_hz * ((Wav.sr * Wav.duration)/Wav.sr))

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
            return np.arange(self.sr * self.duration)
        
        @property
        def wav(self):
            return 2 * np.pi * self.carrier_hz * self.t_samples / self.sr
        
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
            cls.duration = duration

        @classmethod
        def update_duty(cls, duty: float):
            cls.duty = duty

        @classmethod
        def update_samplerate(cls, sr: int):
            cls.sr = sr

        @classmethod
        def update_modulator_hz(cls, modulator_hz: float):
            cls.modulator_hz = modulator_hz

        @classmethod
        def update_ac(cls, ac: float):
            cls.ac = ac 

        @classmethod
        def update_kc(cls, ka: float):
            cls.ka = ka
    
        def make_wav(self, wav_type: str, modulated: bool=False):

            if wav_type == 'sine':

                if modulated:

                    __make_wav(carrier=self.sin_carrier, sr=self.sr,
                               hz=self.hz, wav_type=wav_type, modulator=self.modulator, 
                               ac=Wav.ac, ka=Wav.ka)

                else:

                    __make_wav(carrier=self.sin_carrier, sr=self.sr, 
                            hz=self.hz, wav_type=wav_type)

            elif wav_type == 'sqaure':

                if modulated:

                    __make_wav(carrier=self.sq_carrier, sr=self.sr,
                               hz=self.hz, wav_type=wav_type, modulator=self.modulator, 
                               ac=Wav.ac, ka=Wav.ka)

                else:

                    __make_wav(carrier=self.sq_carrier, sr=self.sr,
                            hz=self.hz, wav_type=wav_type)

            elif wav_type == 'square_duty':

                if modulated:

                    __make_wav(carrier=self.sq_duty_carrier, sr=self.sr,
                               hz=self.hz, wav_type=wav_type, modulator=self.modulator, 
                               ac=Wav.ac, ka=Wav.ka)

                else:

                    __make_wav(carrier=self.sq_duty_carrier, sr=self.sr,
                            hz=self.hz, wav_type=wav_type)

            elif wav_type == 'sawtooth':

                if modulated:

                    __make_wav(carrier=self.sawtooth_carrier, sr=self.sr,
                               hz=self.hz, wav_type=wav_type, modulator=self.modulator, 
                               ac=Wav.ac, ka=Wav.ka)

                else:
                        
                    __make_wav(carrier=self.sawtooth_carrier, sr=self.sr,
                            hz=self.hz, wav_type=wav_type)




    

