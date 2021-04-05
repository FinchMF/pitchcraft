# python tool
from typing import List, Dict, Union, TypeVar
# signal and wav utilities
from scipy import signal as sg 
from scipy.io.wavfile import read, write
# math utilits
import numpy as np
from math import log2, pow
# visual utility
import matplotlib.pyplot as plt 
# web utilities
from flask import Flask
import dash 
# application and server
server = Flask(__name__)
server.config['SECRET_KEY'] = 'pitchcraftsourcery'
server.config.from_object(__name__)
external_style_sheet = ['https://codepen.io/chriddyp/pen/dZVMbK.css']
APP = dash.Dash(__name__, server=server, external_stylesheets=external_style_sheet)
# application core
from core.generator import *
from core.util import *
from core.layout import *
from core.routes import *