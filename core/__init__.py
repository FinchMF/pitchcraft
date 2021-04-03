# web utilities
from flask import Flask
import dash 
# signal and wav utilities
from scipy import signal as sg 
from scipy.io.wavfile import read, write
# math utilits
import numpy as np
from math import log2, pow
# visual utility
import matplotlib.pyplot as plt 
# python tool
from typing import List, Dict, Union, TypeVar
# application core
from core.generator import *
from core.util import *
from core.routes import *
from core.layout import *
# application and server
server = Flask(__name__)
APP = dash.Dash(__name__, server=server)
APP.title = "PitchCraft"