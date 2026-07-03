"""Mix ótimo de produção de alumínio — maximização de lucro (PL).

Enunciado: A Alumeo fabrica chapas e barras de alumínio. A capacidade máxima de
produção estimada são 800 chapas ou 600 barras por dia. A demanda máxima diária
são 550 chapas e 580 barras. O lucro por tonelada é $40 por chapa e $35 por
barra. Determine o mix ótimo de produção diária.
"""

from operational_research import setup_ampl


def main() -> None:
    ampl = setup_ampl()

    ampl.eval("""
        var sheet >= 0;
        var bar >= 0;
        maximize z: 40*sheet + 35*bar;
        subject to
            sheet_demand: sheet <= 550;
            bar_demand: bar <= 580;
            max_production_capacity: bar <= 600 - 0.75*sheet;
    """)

    ampl.solve()
    print(f"Optimal profit: {ampl.get_objective('z').value()}")
    print(f"sheet = {ampl.get_variable('sheet').value()}")
    print(f"bar = {ampl.get_variable('bar').value()}")


if __name__ == "__main__":
    main()
