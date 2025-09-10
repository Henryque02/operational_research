'''Otimização de Recursos para Produção de Equipamentos
Uma empresa de tecnologia precisa produzir dois tipos de componentes eletrônicos: Componente X e
Componente Y, utilizando dois recursos escassos: Chipset e Memória RAM. O objetivo é minimizar os custos
de produção garantindo que as demandas mínimas de chipset e memória sejam atendidas. A tabela em anexo
resume a quantidade de cada recurso necessária para produzir uma unidade de cada componente, assim como
o custo de produção de cada um'''

import sys
from config import setup_ampl

ampl = setup_ampl()

ampl.eval('''
    var componente_x >= 0;
    var componente_y >= 0;
    minimize z: 2*componente_x + 4.50*componente_y;
    subject to
        min_ram: 20*componente_x + 5*componente_y >= 80;
        min_chipset: 3*componente_x + 40*componente_y >= 25;
''')
ampl.solve()
print(f"resultado: {ampl.getObjective('z').value()}")
print(f"componente_x = {ampl.getVariable('componente_x').value()}")
print(f"componente_y = {ampl.getVariable('componente_y').value()}")