'''Uma empresa fabrica dois produtos, A e B. O volume de vendas de A é de no mínimo 80% do total de vendas de ambos (A e B) 
   Contudo, a empresa não pode vender mais do que 100 unidades de A por dia. 
   Ambos os produtos usam uma matéria-prima cuja disponibilidade máxima diária é 240 Ib.
   As taxas de utilização da matéria-prima são 2 lb por unidade de A e 4 lb por unidade de B. 
   Os lucros unitários para A e B são $ 20 e $ 50, respectivamente. 
   Determine o mix de produto ótimo para a empresa.'''

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