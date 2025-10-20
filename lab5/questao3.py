import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from config_solver import setup_ampl

ampl = setup_ampl()

ampl.eval('''
    var amostra_resistenteA>= 0;
    var amostra_resistenteB>= 0;
    var amostra_fragilA >= 0;
    var amostra_fragilB>= 0;
    maximize z: amostra_resistenteA + amostra_fragilA + amostra_resistenteB + amostra_fragilB;    
    subject to
        estoqueA: amostra_resistenteA + 2*amostra_fragilA <= 24;
        estoqueB: 2*amostra_resistenteA + 2*amostra_fragilA <= 36;
        min_amostra_resistente: amostra_resistenteA >= 4;
        min_amostra_fragil: amostra_fragilA >= 2;
        razao_3:1_massa: ;
        min_amostra_fragil: amostra_fragilA >= 2;
        solve;
''')
ampl.solve()

print('servico_padrao:', ampl.get_variable('servico_padrao').value())
print('servico_premium:', ampl.get_variable('servico_premium').value())
