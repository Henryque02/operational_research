'''A Alumeo fabrica chapas e barras de alumínio. A capacidade máxima de produção estimada são 800 chapas ou 600 barras por dia. 
   À demanda máxima diária são 550 chapas e 580 barras. O lucro por tonelada é $ 40 por chapa e $ 35 por barra. 
   Determine o mix ótimo de produção diária.'''

import sys
from config import setup_ampl

ampl = setup_ampl()

ampl.eval('''
    var chapa >= 0;
    var barra >= 0;
    maximize z: 35*barra + 40*chapa;
    subject to
        demanda_de_chapas: chapa <= 550;
        demanda_de_barras: barra <= 580;
        capacidade_max_producao: barra <= 600 - 0.75*chapa;
''')

ampl.solve()
print(f"Lucro ótimo: {ampl.getObjective('z').value()}")
print(f"chapa = {ampl.getVariable('chapa').value()}")
print(f"barra = {ampl.getVariable('barra').value()}")