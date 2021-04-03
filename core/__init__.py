from flask import Flask
import dash 

from scipy import signal as sg 
from scipy.io.wavfile import read, write
import numpy as np
from math import log2, pow

import matplotlib.pyplot as plt 
from typing import List, Dict, Union, TypeVar

from core.generator import *
from core.util import *

server = Flask(__name__)

APP = dash.Dash(__name__, server=server)

APP.title = "PitchCraft"