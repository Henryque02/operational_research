"""Mix ótimo de produção — maximização de lucro (PL).

Enunciado: Uma empresa fabrica dois produtos, A e B. O volume de vendas de A é de
no mínimo 80% do total de vendas de ambos (A e B). Contudo, a empresa não pode
vender mais do que 100 unidades de A por dia. Ambos os produtos usam uma
matéria-prima cuja disponibilidade máxima diária é 240 lb. As taxas de utilização
da matéria-prima são 2 lb por unidade de A e 4 lb por unidade de B. Os lucros
unitários para A e B são $20 e $50, respectivamente. Determine o mix de produto
ótimo para a empresa.
"""

from operational_research import setup_ampl


def main() -> None:
    ampl = setup_ampl()

    ampl.eval("""
        var product_a >= 0;
        var product_b >= 0;
        maximize z: 20*product_a + 50*product_b;
        subject to
            raw_material_availability: 2*product_a + 4*product_b <= 240;
            sales_volume_ratio: product_a >= 4*product_b;
            max_sales_a: product_a <= 100;
    """)

    ampl.solve()
    print(f"Optimal profit: {ampl.get_objective('z').value()}")
    print(f"product_a = {ampl.get_variable('product_a').value()}")
    print(f"product_b = {ampl.get_variable('product_b').value()}")


if __name__ == "__main__":
    main()
