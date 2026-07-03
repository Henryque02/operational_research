"""Alocação de produção entre equipes — maximização (PL).

Três tipos de produto podem ser fabricados por quatro equipes, cada uma com
tempo de produção próprio por tipo e um limite de horas disponíveis. Há também
uma produção mínima exigida por tipo de produto. O objetivo é maximizar o valor
total produzido. Enunciado completo em
``assets/team_production_statement.png``.

Notação: ``product_ij`` = unidades do produto tipo *i* fabricadas pela equipe *j*.
"""

from operational_research import setup_ampl


def main() -> None:
    ampl = setup_ampl()

    ampl.eval("""
        var product11 >= 0; var product12 >= 0; var product13 >= 0; var product14 >= 0;
        var product21 >= 0; var product22 >= 0; var product23 >= 0; var product24 >= 0;
        var product31 >= 0; var product32 >= 0; var product33 >= 0; var product34 >= 0;

        maximize z: 6*product11 + 4*product12 + 4*product13 + 7*product14
                  + 7*product21 + 10*product22 + 8*product23 + 10*product24
                  + 8*product31 + 10*product32 + 10*product33 + 11*product34;

        subject to
            team1_available_time: 9*product11 + 4*product21 + 9*product31 <= 1800;
            team2_available_time: 5*product12 + 10*product22 + 12*product32 <= 1800;
            team3_available_time: 3*product13 + 7*product23 + 15*product33 <= 1800;
            team4_available_time: 11*product14 + 12*product24 + 16*product34 <= 1800;
            min_product1: product11 + product12 + product13 + product14 >= 90;
            min_product2: product21 + product22 + product23 + product24 >= 160;
            min_product3: product31 + product32 + product33 + product34 >= 110;
        solve;
    """)

    print("=" * 50)
    totals = {1: 0.0, 2: 0.0, 3: 0.0}
    for team in range(1, 5):
        print(f"\nTeam {team}:")
        for product in range(1, 4):
            value = ampl.get_variable(f"product{product}{team}").value()
            totals[product] += value
            print(f"  Product type {product}: {value} units")

    print("\n" + "-" * 50)
    for product, total in totals.items():
        print(f"Total product {product}: {total} units")
    print(f"\nOptimal value of z: {ampl.get_objective('z').value()}")
    print("=" * 50 + "\n")


if __name__ == "__main__":
    main()
