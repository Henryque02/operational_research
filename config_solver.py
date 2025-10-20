#Importações e configuração
import os, sys, subprocess
from amplpy import AMPL

#Criar instância AMPL e configurar solver
def setup_ampl(solver='cbc'):
    # Adicionar módulos AMPL ao PATH
    caminho_mod = subprocess.check_output(
        [sys.executable, "-m", "amplpy.modules", "path"]
    ).decode().strip()
    os.environ["PATH"] += os.pathsep + caminho_mod
    
    # Criar instância e configurar solver
    ampl = AMPL()
    ampl.option['solver'] = solver
    print(f"AMPL configurado com solver {solver.upper()}")
    return ampl