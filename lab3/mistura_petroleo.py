import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from config_solver import setup_ampl

def modelo():
    ampl = setup_ampl('highs')
    modelo = """
    var Xs1 >=0; var Xs2 >=0; var Xs3 >=0; var Xs4 >=0;
    var Xz1 >=0; var Xz2 >=0; var Xz3 >=0; var Xz4 >=0;
    var Xa1 >=0; var Xa2 >=0; var Xa3 >=0; var Xa4 >=0;
    maximize z: 35*(Xs1+Xs2+Xs3+Xs4) + 28*(Xz1+Xz2+Xz3+Xz4) + 22*(Xa1+Xa2+Xa3+Xa4) - 19*(Xs1+Xz1+Xa1) - 24*(Xs2+Xz2+Xa2) - 20*(Xs3+Xz3+Xa3) - 27*(Xs4+Xz4+Xa4);
    subject to
        disponibilidade_max_p1: Xs1+Xz1+Xa1 <=3500;
        disponibilidade_max_p2: Xs2+Xz2+Xa2 <=2200;
        disponibilidade_max_p3: Xs3+Xz3+Xa3 <=4200;
        disponibilidade_max_p4: Xs4+Xz4+Xa4 <=1800;
        EspecificacaoS1: 0.3*(Xs1+Xs2+Xs3+Xs4) >= Xs1; 
        EspecificacaoS2: 0.4*(Xs1+Xs2+Xs3+Xs4) <= Xs2; 
        EspecificacaoS3: 0.5*(Xs1+Xs2+Xs3+Xs4) >= Xs3;
        EspecificacaoZ1: 0.3*(Xz1+Xz2+Xz3+Xz4) >= Xz1;
        EspecificacaoZ2: 0.1*(Xz1+Xz2+Xz3+Xz4) <= Xz2;
        EspecificacaoA: 0.7*(Xa1+Xa2+Xa3+Xa4) <= Xa1;
    solve;
    """
    ampl.eval(modelo)   

    petroleos = []
    for i in range(1, 5):
        total = (ampl.get_variable(f'Xs{i}').value() + 
                 ampl.get_variable(f'Xz{i}').value() + 
                 ampl.get_variable(f'Xa{i}').value())
        petroleos.append(total)
        print(f"Petróleo {i}: {total} barris")

    print("-"*50)
    print("GASOLINA PRODUZIDA:")
    
    gasolina_super = sum(ampl.get_variable(f'Xs{i}').value() for i in range(1, 5))
    gasolina_azul = sum(ampl.get_variable(f'Xz{i}').value() for i in range(1, 5))
    gasolina_amarela = sum(ampl.get_variable(f'Xa{i}').value() for i in range(1, 5))

    print(f"Gasolina Super azul: {gasolina_super:,.2f} barris")
    print(f"Gasolina Azul: {gasolina_azul:,.2f} barris")
    print(f"Gasolina Amarela: {gasolina_amarela:,.2f} barris")
    print(f"O lucro total maximo é de R${ampl.get_objective('z').value()}")
modelo()