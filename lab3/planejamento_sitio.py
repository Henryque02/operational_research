import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from config_solver import setup_ampl

# Modelo feito em classe, via funcao, pense nas vantagens.
def modelo1():
  ampl = setup_ampl('highs')
  # Modelo AMPL com parâmetros de produtividade
  # para cálculo dos kg/cultura no final
  modelo = """
  var area_trigo >=0;
  var area_arroz >=0;
  var area_milho >=0;
  maximize z: 2.16*area_trigo+1.26*area_arroz+0.812*area_milho;
  subject to
  area_minima_trigo: area_trigo>=400;
  area_minima_arroz: area_arroz>=800;
  area_minima_milho: area_milho>= 10000;
  area_maxima: area_trigo+area_arroz+area_milho <= 200000;
  quantidade_max_toneladas: 0.2*area_trigo+0.3*area_arroz+0.4*area_milho <= 60000;
  param ProdTrigo := 0.2;
  param ProdArroz := 0.3;
  param ProdMilho := 0.4;
  solve;
  display area_trigo, area_arroz, area_milho;
  display "Produção em kg:";
  display "kg_Trigo =", ProdTrigo * area_trigo;
  display "kg_Arroz =", ProdArroz * area_arroz;
  display "kg_Milho =", ProdMilho * area_milho;
  """
  ampl.eval(modelo)

modelo1()

##Modelo agora usando a quantidade em kg como variável de decisão
def modelo2():
    ampl = setup_ampl('highs')
    
    modelo = """
    var QT >= 0;  # Quantidade de trigo produzida (em kg)
    var QA >= 0;  # Quantidade de arroz produzida (em kg)
    var QM >= 0;  # Quantidade de milho produzida (em kg)

    maximize z: (2.16/0.2)*QT + (1.26/0.3)*QA + (0.812/0.4)*QM;

    subject to
        c1: QT >= 80;
        c2: QA >= 240;
        c3: QM >= 4000;
        c4: (QT/0.2) + (QA/0.3) + (QM/0.4) <= 200000;
        c5: QT + QA + QM <= 60000;

    solve;

    display QT, QA, QM;
    display "Lucro total =", (2.16/0.2)*QT + (1.26/0.3)*QA + (0.812/0.4)*QM;
    """

    ampl.eval(modelo)

modelo2()
