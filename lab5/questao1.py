import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from config_solver import setup_ampl

def modelo():
    ampl = setup_ampl()
    # produto_ij: tipo i fabricado pela empresa j
    modelo = """
    var produto11 >= 0; var produto12 >= 0; var produto13 >= 0; var produto14 >= 0;
    var produto21 >= 0; var produto22 >= 0; var produto23 >= 0; var produto24 >= 0;
    var produto31 >= 0; var produto32 >= 0; var produto33 >= 0; var produto34 >= 0;
    
    maximize z: 6*produto11 + 4*produto12 + 4*produto13 + 7*produto14
              + 7*produto21 + 10*produto22 + 8*produto23 + 10*produto24 
              + 8*produto31 + 10*produto32 + 10*produto33 + 11*produto34;
    
    subject to
        tempo_disponivel_equipe1: 9*produto11 + 4*produto21 + 9*produto31 <= 1800;
        tempo_disponivel_equipe2: 5*produto12 + 10*produto22 + 12*produto32 <= 1800;
        tempo_disponivel_equipe3: 3*produto13 + 7*produto23 + 15*produto33 <= 1800;
        tempo_disponivel_equipe4: 11*produto14 + 12*produto24 + 16*produto34 <= 1800;
        min_produto1: produto11 + produto12 + produto13 + produto14 >= 90;
        min_produto2: produto21 + produto22 + produto23 + produto24 >= 160;
        min_produto3: produto31 + produto32 + produto33 + produto34 >= 110;
    
    solve;
    """
    
    ampl.eval(modelo)
    
    print("="*50)
    
    total_produto1 = 0
    total_produto2 = 0
    total_produto3 = 0
    
    for j in range(1, 5):
        p1j = ampl.get_variable(f'produto1{j}').value()
        p2j = ampl.get_variable(f'produto2{j}').value()
        p3j = ampl.get_variable(f'produto3{j}').value()

        total_produto1 += p1j
        total_produto2 += p2j
        total_produto3 += p3j

        print(f"\nEquipe {j}:")
        print(f"  Produto tipo 1: {p1j} unidades")
        print(f"  Produto tipo 2: {p2j} unidades")
        print(f"  Produto tipo 3: {p3j} unidades")

    print("\n" + "-"*50)
    print(f"Total Produto 1: {total_produto1} unidades")
    print(f"Total Produto 2: {total_produto2} unidades")
    print(f"Total Produto 3: {total_produto3} unidades")
    print(f"\nValor ótimo de z: {ampl.get_objective('z').value()}")
    print("="*50 + "\n")

modelo()