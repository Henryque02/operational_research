import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from config_solver import setup_ampl

ampl = setup_ampl()

ampl.eval('''
    var servico_padrao >= 0;
    var servico_premium >= 0;
    maximize z: 10*servico_padrao + 30*servico_premium;    
    subject to
        banca_reparo: servico_padrao + 2*servico_premium <= 24;
        banca_testes: 2*servico_padrao + 2*servico_premium <= 36;
        min_padrao: servico_padrao >= 4;
        min_premium::servico_premium >= 2;
        solve;
''')
ampl.solve()

print('servico_padrao:', ampl.get_variable('servico_padrao').value())
print('servico_premium:', ampl.get_variable('servico_premium').value())
