
from core import np, log2, pow, List, Dict, TypeVar
RANGE = TypeVar('range')

# ~ ~ ~ ~ ~ ~ System Utils ~ ~ ~ ~ ~ ~ ~ #

class Systems:
    """
    Object containing dynamic pitch system objects
    ----------------------------------------------
        - A pitch system is an abstracted set of relations
    based on divisions of the octave. The western system
    divides the octave into 12 equal units where each unit
    is a set interval. This interval is referred to as 
    a semi tone. Semi represents half. We can infer that
    the base unit is 6 - which we have set in a class variable

        - By manipulating the base of the system, all relations will
    be subsequently altered.

        - Each system is generated upwards from an initializing frequencey
    """
    	
    base: int = 6

    tones: Dict[str, int] = {

        # generates the number of division for the octave

        'half_base_tone': base // 3,
        'tri_base_tone': base // 2,
        'quarter_base_tone': base-2,
        'fifth_base_tone': base-1,
        'base_tone': base,
        'seventh_base_tone': base+1,
        'eighth_base_tone': base+2,
        'ninth_base_tone': base+3,
        'tenth_base_tone': base+4,
        'eleventh_base_tone': base+5,

        'semi_tone': 2*base,
        'tri_tone': 3*base,
        'quarter_tone': 4*base,
        'sixth_tone': 6*base,
        'eighth_tone': 8*base,
        'twelevth_tone': 12*base,
        'twenty_fourth_tone': 24*base
    }

    interval_systems: Dict[str, float] = {

        # generates the float representation of the interval between frequencies

        'half_base_tone': 2**(1/tones['half_base_tone']),
        'tri_base_tone': 2**(1/tones['tri_base_tone']),
        'quarter_base_tone': 2**(1/tones['quarter_base_tone']),
        'fifth_base_tone': 2**(1/tones['fifth_base_tone']),
        'base_tone': 2**(1/tones['base_tone']),
        'seventh_base_tone': 2**(1/tones['seventh_base_tone']),
        'eighth_base_tone': 2**(1/tones['eighth_base_tone']),
        'ninth_base_tone': 2**(1/tones['ninth_base_tone']),
        'tenth_base_tone': 2**(1/tones['tenth_base_tone']),
        'eleventh_base_tone': 2**(1/tones['eleventh_base_tone']),

        'semi_tone': 2**(1/tones['semi_tone']),
        'tri_tone': 2**(1/tones['tri_tone']),
        'quarter_tone': 2**(1/tones['quarter_tone']),
        'sixth_tone': 2**(1/tones['sixth_tone']),
        'eighth_tone': 2**(1/tones['eighth_tone']),
        'twelevth_tone': 2**(1/tones['twelevth_tone']),
        'twenty_fourth_tone':2**(1/tones['twenty_fourth_tone'])
    }

    octave_systems: Dict[str, int] = {

        # generates all intervals, as floats between 1 and 2 (the octave)
        
        'half_base_tone': (tones['half_base_tone']-1)*8,
        'tri_base_tone': (tones['tri_base_tone']-1)*8,
        'quarter_base_tone': (tones['quarter_base_tone']-1)*8,
        'fifth_base_tone': (tones['fifth_base_tone']-1)*8,
        'base_tone': (tones['base_tone']-1)*8,
        'seventh_base_tone': (tones['seventh_base_tone']-1)*8,
        'eighth_base_tone': (tones['eighth_base_tone']-1)*8,
        'ninth_base_tone': (tones['ninth_base_tone']-1)*8,
        'tenth_base_tone': (tones['tenth_base_tone']-1)*8,
        'eleventh_base_tone': (tones['eleventh_base_tone']-1)*8,

        'semi_tone': (tones['semi_tone']-1)*8,
        'tri_tone': (tones['tri_tone']-1)*8,
        'quarter_tone': (tones['quarter_tone']-1)*8,
        'sixth_tone': (tones['sixth_tone']-1)*8,
        'eighth_tone': (tones['eighth_tone']-1)*8,
        'twelevth_tone': (tones['twelevth_tone']-1)*8,
        'twenty_fourth_tone': (tones['twenty_fourth_tone']-1*8)
    }

    fiveLimit_N1: Dict[str, float] = {

        # generates just intonation octave system

        'perfect unison': float(1.0/1.0),
        'minor second': float(16.0/15.0),
        'major second': float(9.0/8.0),
        'minor third': float(6.0/5.0),
        'major third': float(5.0/4.0),
        'perfect fourth': float(4.0/3.0),
        'aug fourth': float(45.0/32.0),
        'dim fifth': float(64.0/45.0),
        'minor sixth': float(8.0/5.0),
        'major sixth': float(5.0/3.0),
        'minor seventh': float(16.0/9.0),
        'major seventh': float(15.0/8.0),
        'perfect octave': float(2.0/1.0)

    }

    fiveLimit_N2: Dict[str, float] = {

        # generates just intonation octave system

        'perfect unison': float(1.0/1.0),
        'minor second': float(16.0/15.0),
        'major second': float(10.0/9.0),
        'minor third': float(6.0/5.0),
        'major third': float(5.0/4.0),
        'perfect fourth': float(4.0/3.0),
        'aug fourth': float(45.0/32.0),
        'dim fifth': float(64.0/45.0),
        'minor sixth': float(8.0/5.0),
        'major sixth': float(5.0/3.0),
        'minor seventh': float(9.0/5.0),
        'major seventh': float(15.0/8.0),
        'perfect octave': float(2.0/1.0)

    }

    fiveLimit_Stnrd: Dict[str, float] = {

        'perfect unison': float(1.0/1.0),
        'minor second': float(16.0/15.0),
        'major second': float(9.0/8.0),
        'minor third': float(6.0/5.0),
        'major third': float(5.0/4.0),
        'perfect fourth': float(4.0/3.0),
        'aug fourth': float(45.0/32.0),
        'dim fifth': float(64.0/45.0),
        'minor sixth': float(8.0/5.0),
        'major sixth': float(5.0/3.0),
        'minor seventh': float(9.0/5.0),
        'major seventh': float(15.0/8.0),
        'perfect octave': float(2.0/1.0)
    }

    fiveLimit_Extnd: Dict[str, float] = {

        'perfect unison': float(1.0/1.0),
        'minor second': float(16.0/15.0),
        'major second': float(9.0/8.0),
        'minor third': float(6.0/5.0),
        'major third': float(5.0/4.0),
        'perfect fourth': float(4.0/3.0),
        'aug fourth': float(25.0/18.0),
        'dim fifth': float(36.0/25.0),
        'minor sixth': float(8.0/5.0),
        'major sixth': float(5.0/3.0),
        'minor seventh': float(9.0/5.0),
        'major seventh': float(15.0/8.0),
        'perfect octave': float(2.0/1.0)
    }

    sevenLimit: Dict[str, float] = {

        'perfect unison': float(1.0/1.0),
        'minor second': float(15.0/14.0),
        'major second': float(8.0/7.0),
        'minor third': float(6.0/5.0),
        'major third': float(5.0/4.0),
        'perfect fourth': float(4.0/3.0),
        'aug fourth': float(7.0/5.0),
        'dim fifth': float(10.0/7.0),
        'perfect fifth': float(3.0/2.0),
        'minor sixth': float(8.0/5.0),
        'major sixth': float(5.0/3.0),
        'minor seventh': float(7.0/4.0),
        'major seventh': float(15.0/8.0),
        'perfect octave': float(2.0/1.0)
    }

    seventeenLimit: Dict[str, float] = {

        'perfect unison': float(1.0/1.0),
        'minor second': float(14.0/13.0),
        'major second': float(8.0/7.0),
        'minor third': float(6.0/5.0),
        'major third': float(5.0/4.0),
        'perfect fourth': float(4.0/3.0),
        'aug fourth': float(17.0/12.0),
        'dim fifth': float(24.0/17.0),
        'perfect fifth': float(3.0/2.0),
        'minor sixth': float(8.0/5.0),
        'major sixth': float(5.0/3.0),
        'minor seventh': float(7.0/4.0),
        'major seventh': float(13.0/7.0),
        'perfect octave': float(2.0/1.0)

    }

    @classmethod
    def update_system_base(cls, n_base: int):
        """
        Alter the base of all systems
        """
        cls.base = n_base

class Network:
    """
    Network object containing dynamic system building objects
    ---------------------------------------------------------
    There are four Networks present in this object. 
        - make_octaves:
             - builds a system of octaves based on the
                the number of octaves declared
        - make_octave_interval_system:
            - builds a sysem that divides the octave
                into declared intervals
        - make_system:
            - builds system in its entirety based on declared
                system type and system size 

                if the system is semi tone 12 division system,
                equal temperment is factored in

        - make_overtone series:
            - builds system according harmonic series
                and is factored towards just intonation
    """
    @staticmethod
    def make_octaves(hz: float, n_octaves: int) -> List[float]:

        """
        Generates Frequences Octaves apart for n Octaves
        ------------------------------------------------
        """
        # set a container to collect freqs
        octaves = [hz] 
        # begin with initializing freq
        curr_octave = hz
        for _ in range(n_octaves):
            # iterate through delcared octaves
            octave = curr_octave * 2.0
            # generate the next ocatve and collect
            octaves.append(octave)
            curr_octave = octave
        
        return octaves

    @staticmethod
    def make_octave_interval_system(tone_intvl: str) -> Dict[str, float]:
        """
        Generates Divisions of the Octave
        ---------------------------------
        Provides floats representing the size of each interval
        """
        # set container for ocatve based system
        interval_system ={}
        # iterate through number of divisions
        for tone in range(Systems.tones[tone_intvl]):
            # set interval
            interval_system[f"0-{tone}"] = (2**(tone+1))**(1/Systems.tones[tone_intvl])

        return interval_system

    @staticmethod
    def make_system(hz: float, system_type: float, 
                               system_size: int) -> Dict[str, float]:
        """
        Generate Musical System
        -----------------------
        Provides floats for every freq at its respective position in the system
        """
        # set container for system
        system = {}
        # iterate through the system size
        for pos in range(system_size):
            # set each freq position 
            freq = hz * (system_type)**pos 
            # each freq is generated by multiplying the original hz
            # by the position set as the power of the system type
            system[f"freq_{pos}"] = round(freq, 2)

        return system

    @staticmethod
    def make_overtone_series(hz: float, system_size: RANGE=range(0,16)) -> List[float]:
        """
        Generates Overtone Series in Just Intonation
        --------------------------------------------
        """
        overtone_series = []
        for pos in system_size:
            # iterate through system size, a defaulted at the first 16 partials
            # multiple position by the starting frequency
            harmonic = pos * hz
            overtone_series.append(harmonic)

        return overtone_series

    @staticmethod
    def make_just_series(hz: float) -> List[float]:

        """
        Generates Single Ocatve System of Just Intonation
        -------------------------------------------------
        """

        just_series = []

        for ii, intvl in Systems.fiveLimitIntvl.items():
            # iterate through five limit system intervals
            # multiple the base frequency by the interval
            just_series.append(hz*intvl)

        return just_series

# ~ ~ ~ ~ ~ ~ Pitch Utils ~ ~ ~ ~ ~ ~ ~ #
class Transform:
    """
    Library of Equal Temperment Pitches set to their standard Hz 
    ------------------------------------------------------------
         - each pitch containing 10 octaves
         - enharmonic pitches are not used, defualts to #s
    
    """
    pitch_to_hz: Dict[str, Dict[int, float]] = {
                
                'C': {-1: 8.18,
                        0: 16.35,
                        1: 32.70,
                        2: 65.41,
                        3: 130.81,
                        4: 261.63,
                        5: 523.25,
                        6: 1046.50,
                        7: 2093.00,
                        8: 4186.00},
                'C#': {-1: 8.66,
                        0: 17.32,
                        1: 34.65,
                        2: 69.30,
                        3: 138.59,
                        4: 277.18,
                        5: 554.37,
                        6: 1108.73, 
                        7: 2217.46,
                        8: 4434.92},
                'D': {-1: 9.18,
                        0: 18.35,
                        1: 36.71,
                        2: 73.42,
                        3: 146.83,
                        4: 293.66,
                        5: 587.33,
                        6: 1174.66,
                        7: 2349.32,
                        8: 4698.64},
                'D#': {-1: 9.72,
                        0: 19.45,
                        1: 38.89,
                        2: 77.78,
                        3: 155.56,
                        4: 311.13,
                        5: 622.25,
                        6: 1244.51,
                        7: 2489.05,
                        8: 4978.03},
                'E': {-1: 10.3,
                        0: 20.60,
                        1: 41.20,
                        2: 82.41,
                        3: 164.81,
                        4: 329.63,
                        5: 659.26,
                        6: 1318.51,
                        7: 2637.02,
                        8: 5274.04},
                 'F': {-1: 10.91,
                        0: 21.83,
                        1: 43.65,
                        2: 87.31,
                        3: 174.61,
                        4: 349.23,
                        5: 698.46,
                        6: 1396.91,
                        7: 2793.83,
                        8: 5587.65},
                'F#': {-1: 11.56,
                        0: 23.12,
                        1: 46.25,
                        2: 92.50,
                        3: 185.00,
                        4: 369.99,
                        5: 739.99,
                        6: 1479.98,
                        7: 2959.96,
                        8: 5919.91},
                 'G': {-1: 12.25,
                        0: 24.50,
                        1: 49.00,
                        2: 98.00,
                        3: 196.00,
                        4: 392.00,
                        5: 783.99,
                        6: 1567.98,
                        7: 3135.95,
                        8: 6271.93},
                'G#': {-1: 12.98,
                        0: 25.96,
                        1: 51.91,
                        2: 103.83,
                        3: 207.65,
                        4: 415.30,
                        5: 830.61,
                        6: 1661.22,
                        7: 3322.44,
                        8: 6644.88},
                 'A': {-1: 13.75,
                        0: 27.50,
                        1: 55.00,
                        2: 110.00,
                        3: 220.00,
                        4: 440.00,
                        5: 880.00,
                        6: 1760.00,
                        7: 3520.00,
                        8: 7040.00},
                'A#': {-1: 14.57,
                        0: 29.14,
                        1: 58.27,
                        2: 116.54,
                        3: 233.08,
                        4: 466.16,
                        5: 932.33,
                        6: 1864.66,
                        7: 3729.31,
                        8: 7458.62},
                 'B': {-1: 15.43,
                        0: 30.87,
                        1: 61.74,
                        2: 123.47,
                        3: 246.94,
                        4: 493.88,
                        5: 987.77,
                        6: 1975.53,
                        7: 3951.07,
                        8: 7902.13}                  
                }

class Detect:
    """
    Detect Object algorthimcally detects nearest pitch and cent offset
    ------------------------------------------------------------------
    """
    # set equal temperment 
    # set relation between A4 and C0
    A4 = int(Transform.pitch_to_hz['A'][4])
    C0 = A4*pow(2, -4.75)
    # set the names of 12 tones
    name = [
        "C", "C#",
        "D", "D#",
        "E", "F", "F#",
        "G", "G#",
        "A", "A#", "B"
    ]

    def __init__(self, start_freq: float, end_freq: float=None):

        self.__freq = start_freq
        self.__end_freq = end_freq

    @property
    def freq(self):
        return self.__freq

    @freq.setter
    def freq(self, freq):
        self.__freq = freq

    @property
    def end_freq(self):
        return self.__end_freq

    @end_freq.setter
    def end_freq(self, end_freq):
        self.__end_feq = end_freq

    def closest_pitch(self)-> str:
        """
        Detects pitch and octave closest to Hz
        --------------------------------------
        Pitches are in relation to wester equal temperment 12 tone system
        """
        # detect pitch index
        h = round(12*log2(self.freq/Detect.C0))
        # detect octave
        octave = h // 12
        # detect pitch name index from pitch name list
        n = h % 12

        return f"{Detect.name[n]}{str(octave)}"

    def find_cent_diff(self, freq_: float=None)-> float:
        """
        Detects cent difference between two Hz
        --------------------------------------
        """
        # This function can take in a new frequency 
        # or use the 'end_freq' instantiated in the object 
        if freq_:

            freq_2 = freq_
        else:
            freq_2 = self.end_freq

        return round(1200 *log2(self.freq/freq_2),2)

    def find_offset_from_closet_pitch(self):
        """
        Detects cent difference between hz and closest pitch
        ----------------------------------------------------
        """
        # detect closest pitch
        f = self.closest_pitch()
        # if pitch is a natural pitch
        if len(f) == 2:
            diff = self.find_cent_diff(freq_=Transform.pitch_to_hz[f[0]][int(f[1])])
        # if pitch is a sharp
        elif len(f) == 3:
            diff = self.find_cent_diff(freq_=Transform.pitch_to_hz[f[0:2]][int(f[2])])
        
        return f, diff