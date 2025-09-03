'''Planejamento de Uso de Água e Fertilizantes para Várias Culturas
A empresa ModernHorti próxima ao aeroporto de New Jersey está cultivando cinco tipos diferentes de
hortaliças em estufas gigantes via hidroponia e iluminação artificial: Cultura A, Cultura B, Cultura C,
Cultura D e Cultura E. Para garantir o crescimento adequado dessas culturas, a estufa precisa usar dois
recursos principais: Água e Fertilizantes. Cada cultura tem uma necessidade mínima desses recursos, e o
objetivo da estufa é minimizar o custo total de irrigação e fertilização, garantindo que as necessidades mínimas
de cada cultura sejam atendidas.
A tabela em anexo resume a quantidade de cada recurso necessária para irrigar uma unidade de cada cultura, bem
como o custo por unidade de irrigação'''

import sys
from config import setup_ampl

ampl = setup_ampl()

ampl.eval('''
    var CulturaA >= 0 integer;
    var CulturaB >= 0 integer;
    var CulturaC >= 0 integer;
    var CulturaD >= 0 integer;
    var CulturaE >= 0 integer;

    minimize z: CulturaA + 2.5*CulturaB + 1.8*CulturaC + 2*CulturaD + 3*CulturaE;
    subject to
        min_litros_agua: 10*CulturaA + 60*CulturaB + 30*CulturaC + 15*CulturaD + 70*CulturaE >= 500;
        min_fertilizante_kg: 5*CulturaA + 10*CulturaB + 8*CulturaC + 4*CulturaD + 12*CulturaE >= 100;
''')
ampl.solve()
print(f"resultado: {ampl.getObjective('z').value()}")
print(f"CulturaA = {ampl.getVariable('CulturaA').value()}")
print(f"CulturaB = {ampl.getVariable('CulturaB').value()}")
print(f"CulturaC = {ampl.getVariable('CulturaC').value()}")
print(f"CulturaD = {ampl.getVariable('CulturaD').value()}")
print(f"CulturaE = {ampl.getVariable('CulturaE').value()}")