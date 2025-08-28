import sys
from config import setup_ampl

ampl = setup_ampl()

ampl.eval('''
    var chapa >= 0 integer;
    var barra >= 0 integer;
    maximize z: 35*barra + 40*chapa;
    subject to
        demanda_de_chapas: chapa <= 550;
        demanda_de_barras: barra <= 580;
        capacidade_max_producao: barra <= 600 - 0.75*chapa;
''')

ampl.solve()
print(f"resultado: {ampl.getObjective('z').value()}")
print(f"chapa = {ampl.getVariable('chapa').value()}")
print(f"barra = {ampl.getVariable('barra').value()}")
