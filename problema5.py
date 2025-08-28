import sys
from config import setup_ampl

ampl = setup_ampl()

ampl.eval('''
    var Produto_A >= 0;
    var Produto_B >= 0;
    maximize z: 20*Produto_A + 50*Produto_B;    
    subject to
        disponibilidade_de_materia_prima: 2*Produto_A + 4*Produto_B <= 240;
        volume_das_vendas: Produto_A >= 4*Produto_B;
        vendas_de_A: Produto_A <= 100;
''')

ampl.solve()
print(f"resultado: {ampl.getObjective('z').value()}")
print(f"Produto_A = {ampl.getVariable('Produto_A').value()}")
print(f"Produto_B = {ampl.getVariable('Produto_B').value()}")
