#Importações e configuração
from amplpy import AMPL

#Criar instância AMPL e configurar solver
def setup_ampl(solver ='cbc'):
    ampl = AMPL()
    ampl.option['solver'] = solver
    print(f"AMPL configurado com solver {solver.upper()}")
    return ampl

