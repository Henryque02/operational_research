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
    area_maxima: area_trigo + area_arroz + area_milho <= 200000;
    quantidade_max_toneladas: 0.2*area_trigo + 0.3*area_arroz + 0.4*area_milho <= 60000;
  solve;
  """

  ampl.eval(modelo)

 #Obtém os valores das variáveis
  area_trigo = ampl.get_variable('area_trigo').value()
  area_arroz = ampl.get_variable('area_arroz').value()
  area_milho = ampl.get_variable('area_milho').value()
  lucro = ampl.get_objective('z').value()
  
  # Parâmetros de produtividade
  ProdTrigo, ProdArroz, ProdMilho = 0.2, 0.3, 0.4
  
  # Visualização formatada
  print("\n" + "="*50)
  print("RESULTADOS DO MODELO 1")
  print(f"Área de Trigo: {area_trigo} m²")
  print(f"Área de Arroz: {area_arroz} m²")
  print(f"Área de Milho: {area_milho} m²")

  print(f"Área Total: {area_trigo + area_arroz + area_milho} m²")
  print("-"*50)
  print("PRODUÇÃO EM KG:")
  print(f"Trigo: {ProdTrigo * area_trigo} kg")
  print(f"Arroz: {ProdArroz * area_arroz} kg")
  print(f"Milho: {ProdMilho * area_milho} kg")
  print(f"Lucro maximo é de R$ {lucro} ")
  print("="*50 + "\n")

modelo1()

##Modelo agora usando a quantidade em kg como variável de decisão
def modelo2():
    ampl = setup_ampl('highs')
    
    modelo = """
    var quantidade_trigo >= 0;
    var quantidade_arroz >= 0;
    var quantidade_milho >= 0;

    maximize z: 10.8*quantidade_trigo + 4.2*quantidade_arroz + 2.03*quantidade_milho;

    subject to
        quantidade_min_trigo: quantidade_trigo >= 80;
        quantidade_min_arroz: quantidade_arroz >= 240;
        quantidade_min_milho: quantidade_milho >= 4000;
        area_total: (quantidade_trigo/0.2) + (quantidade_arroz/0.3) + (quantidade_milho/0.4) <= 200000;
        producao_max: quantidade_trigo + quantidade_arroz + quantidade_milho <= 60000;

    solve;
    """

    ampl.eval(modelo)

    quantidade_trigo = ampl.get_variable('quantidade_trigo').value()
    quantidade_arroz = ampl.get_variable('quantidade_arroz').value()
    quantidade_milho = ampl.get_variable('quantidade_milho').value()
    lucro = ampl.get_objective('z').value()
    print("\n" + "="*50)
    print("RESULTADOS DO MODELO 2")
    print(f"quantidade de Trigo: {quantidade_trigo} kg")
    print(f"quantidade de Arroz: {quantidade_arroz} kg")
    print(f"quantidade de Milho: {quantidade_milho} kg")

    print(f"Produção total: {quantidade_trigo + quantidade_arroz + quantidade_milho} kg")
    print("-"*50)
    print("área em m²:")
    print(f"Trigo: {quantidade_trigo/0.2} m²")
    print(f"Arroz: {quantidade_arroz/0.3} m²")
    print(f"Milho: {quantidade_milho/0.4} m²")
    print(f"Lucro maximo é de R$ {lucro} ")
    print("="*50 + "\n")

modelo2()
