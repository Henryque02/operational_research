"""Produção de amostras para testes — maximização (PL).

Amostras resistentes e frágeis produzidas a partir de dois estoques de material
(A e B), com mínimos por tipo de amostra e uma razão de massa 3:1 exigida pelo
enunciado. Enunciado completo em ``assets/sample_testing_statement.png``.

.. todo::
    A restrição de razão 3:1 de massa ainda não foi modelada — o modelo está
    incompleto e a solução atual NÃO reflete o enunciado. Consultar
    ``assets/sample_testing_statement.png`` e adicionar a restrição
    ``mass_ratio_3_to_1`` abaixo.
"""

from operational_research import setup_ampl


def main() -> None:
    ampl = setup_ampl()

    ampl.eval("""
        var resistant_sample_a >= 0;
        var resistant_sample_b >= 0;
        var fragile_sample_a >= 0;
        var fragile_sample_b >= 0;
        maximize z: resistant_sample_a + fragile_sample_a
                  + resistant_sample_b + fragile_sample_b;
        subject to
            stock_a: resistant_sample_a + 2*fragile_sample_a <= 24;
            stock_b: 2*resistant_sample_a + 2*fragile_sample_a <= 36;
            min_resistant: resistant_sample_a >= 4;
            min_fragile: fragile_sample_a >= 2;
        solve;
    """)
    # TODO: adicionar a restrição mass_ratio_3_to_1 conforme o enunciado.

    for var in (
        "resistant_sample_a",
        "fragile_sample_a",
        "resistant_sample_b",
        "fragile_sample_b",
    ):
        print(f"{var} = {ampl.get_variable(var).value()}")
    print(f"Optimal value of z: {ampl.get_objective('z').value()}")


if __name__ == "__main__":
    main()
