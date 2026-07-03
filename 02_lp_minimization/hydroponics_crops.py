"""Planejamento de água e fertilizantes para culturas — minimização de custo (PL).

Enunciado: A empresa ModernHorti, próxima ao aeroporto de New Jersey, está
cultivando cinco tipos diferentes de hortaliças em estufas gigantes via
hidroponia e iluminação artificial: Culturas A, B, C, D e E. Para garantir o
crescimento adequado dessas culturas, a estufa precisa usar dois recursos
principais: Água e Fertilizantes. Cada cultura tem uma necessidade mínima
desses recursos, e o objetivo da estufa é minimizar o custo total de irrigação
e fertilização, garantindo que as necessidades mínimas de cada cultura sejam
atendidas. A tabela em ``assets/hydroponics_crops_table.png`` resume a
quantidade de cada recurso necessária para irrigar uma unidade de cada cultura,
bem como o custo por unidade de irrigação.
"""

from operational_research import setup_ampl

CROPS = ("crop_a", "crop_b", "crop_c", "crop_d", "crop_e")


def main() -> None:
    ampl = setup_ampl()

    ampl.eval("""
        var crop_a >= 0;
        var crop_b >= 0;
        var crop_c >= 0;
        var crop_d >= 0;
        var crop_e >= 0;

        minimize z: crop_a + 2.5*crop_b + 1.8*crop_c + 2*crop_d + 3*crop_e;
        subject to
            min_water_liters: 10*crop_a + 60*crop_b + 30*crop_c + 15*crop_d + 70*crop_e >= 500;
            min_fertilizer_kg: 5*crop_a + 10*crop_b + 8*crop_c + 4*crop_d + 12*crop_e >= 100;
    """)

    ampl.solve()
    print(f"Minimum cost: {ampl.get_objective('z').value()}")
    for crop in CROPS:
        print(f"{crop} = {ampl.get_variable(crop).value()}")


if __name__ == "__main__":
    main()
