'''Otimização de Recursos para Produção de Equipamentos
Uma empresa de tecnologia precisa produzir dois tipos de componentes eletrônicos: Componente X e
Componente Y, utilizando dois recursos escassos: Chipset e Memória RAM. O objetivo é minimizar os custos
de produção garantindo que as demandas mínimas de chipset e memória sejam atendidas. A tabela em anexo
resume a quantidade de cada recurso necessária para produzir uma unidade de cada componente, assim como
o custo de produção de cada um

Propostas para Complicar o Problema:
1.Adicionar Mais Componentes Eletrônicos (Mais Variáveis):
Ao invés de apenas dois componentes, adicione mais tipos de componentes eletrônicos. Isso pode ser
expandido para, por exemplo, cinco componentes (Componente X, Y, Z, W, e V).
2.Mais Tipos de Recursos (Mais Restrições):
Ao invés de apenas Chipset e Memória RAM, adicione outros recursos essenciais, como:
•Energia Elétrica para a fabricação.
•Mão-de-obra especializada.
•Capacidade de produção das máquinas.
•Exemplo de novos recursos: Chipset, Memória RAM, Energia Elétrica (kWh), Mão-de-obra (horas).'''

import sys
from config import setup_ampl

ampl = setup_ampl()

ampl.eval('''
    var componente_x >= 0;
    var componente_y >= 0;
    var componente_z >= 0;
    var componente_w >= 0;
    var componente_h >= 0;
    minimize z: 2*componente_x + 4.50*componente_y + 7*componente_z + 1.5*componente_w + 3.75*componente_h;
    subject to
        min_ram: 20*componente_x + 5*componente_y >= 80;
        min_chipset: 3*componente_x + 40*componente_y >= 25;
        min_energia_eletrica: 40*componente_x + 3*componente_y + 72*componente_z + 25*componente_w + 7*componente_h >=50;
        min_horas_produção: 1*componente_x + 8*componente_y + 32*componente_z + 43*componente_w + 29*componente_h>=74;
''')
ampl.solve()
print(f"custo mínimo: {ampl.getObjective('z').value()}")
print(f"componente_x = {ampl.getVariable('componente_x').value()}")
print(f"componente_y = {ampl.getVariable('componente_y').value()}")
print(f"componente_z = {ampl.getVariable('componente_z').value()}")
print(f"componente_w = {ampl.getVariable('componente_w').value()}")
print(f"componente_h = {ampl.getVariable('componente_h').value()}")
