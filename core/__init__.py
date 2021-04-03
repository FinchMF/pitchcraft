# web utilities
from flask import Flask
import dash 
# application and server
server = Flask(__name__)
server.config['SECRET_KEY'] = 'pitchcraftsourcery'
server.config.from_object(__name__)
APP = dash.Dash(__name__, server=server)
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
# from core.routes import index
from core.layout import *
from core.routes import *