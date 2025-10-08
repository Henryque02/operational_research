import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from config_solver import setup_ampl

def modelo():
    ampl = setup_ampl('highs')
    modelo = """
    var
    va