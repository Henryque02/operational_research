import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config_solver import setup_ampl

def modelo():
    ampl = setup_ampl()

    modelo = """
    var Onibus1 >=0;
    var Onibus2 >=0;
    var Onibus3 >=0;
    var Onibus4 >=0;
    var Onibus5 >=0;
    var Onibus6 >=0;
    minimize z: Onibus1 + Onibus2 + Onibus3 + Onibus4 + Onibus5 + Onibus6;
    subject to
        00_04: Onibus1 + Onibus6 >=4;
        04_08: Onibus1 + Onibus2 >=8;
        08_12: Onibus2 + Onibus3 >=10;
        12_16: Onibus3 + Onibus4 >=7;
        16_20: Onibus4 + Onibus5 >=12;
        20_00: Onibus5 + Onibus6 >=4;
        solve;
    """
    ampl.eval(modelo)

    onibus = []
    for i in range(1, 7):
        horario = ampl.get_variable(f'Onibus{i}').value()
        onibus.append(horario)
        print(f"A quantidade de Ônibus para atender o {i}º horário será: {horario} ônibus")
    print("A quantidade total de ônibus será",ampl.get_objective('z').value())
modelo()