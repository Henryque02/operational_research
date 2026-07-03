"""Problema de mistura (blending) de petróleo — maximização de lucro (PL).

Quatro tipos de petróleo bruto são combinados para produzir três tipos de
gasolina (Super, Azul e Amarela), cada uma com especificações de composição
mínimas/máximas por tipo de petróleo. O objetivo é maximizar o lucro
(receita das gasolinas menos custo dos petróleos) respeitando a
disponibilidade de cada petróleo e as especificações de mistura.

Enunciado completo em ``assets/petroleum_blending_statement.png``.

Notação: ``xs_i`` / ``xz_i`` / ``xa_i`` = barris do petróleo *i* usados na
gasolina Super / Azul (blue) / Amarela (yellow).
"""

from operational_research import setup_ampl


def main() -> None:
    ampl = setup_ampl("highs")

    ampl.eval("""
        var xs1 >= 0; var xs2 >= 0; var xs3 >= 0; var xs4 >= 0;
        var xz1 >= 0; var xz2 >= 0; var xz3 >= 0; var xz4 >= 0;
        var xa1 >= 0; var xa2 >= 0; var xa3 >= 0; var xa4 >= 0;

        maximize z: 35*(xs1+xs2+xs3+xs4) + 28*(xz1+xz2+xz3+xz4) + 22*(xa1+xa2+xa3+xa4)
                  - 19*(xs1+xz1+xa1) - 24*(xs2+xz2+xa2) - 20*(xs3+xz3+xa3) - 27*(xs4+xz4+xa4);
        subject to
            max_availability_crude1: xs1+xz1+xa1 <= 3500;
            max_availability_crude2: xs2+xz2+xa2 <= 2200;
            max_availability_crude3: xs3+xz3+xa3 <= 4200;
            max_availability_crude4: xs4+xz4+xa4 <= 1800;
            super_spec_crude1: 0.3*(xs1+xs2+xs3+xs4) >= xs1;
            super_spec_crude2: 0.4*(xs1+xs2+xs3+xs4) <= xs2;
            super_spec_crude3: 0.5*(xs1+xs2+xs3+xs4) >= xs3;
            blue_spec_crude1: 0.3*(xz1+xz2+xz3+xz4) >= xz1;
            blue_spec_crude2: 0.1*(xz1+xz2+xz3+xz4) <= xz2;
            yellow_spec_crude1: 0.7*(xa1+xa2+xa3+xa4) <= xa1;
        solve;
    """)

    print("-" * 50)
    print("CRUDE OIL USED:")
    for i in range(1, 5):
        total = (
            ampl.get_variable(f"xs{i}").value()
            + ampl.get_variable(f"xz{i}").value()
            + ampl.get_variable(f"xa{i}").value()
        )
        print(f"Crude {i}: {total:,.2f} barrels")

    print("-" * 50)
    print("GASOLINE PRODUCED:")
    super_gas = sum(ampl.get_variable(f"xs{i}").value() for i in range(1, 5))
    blue_gas = sum(ampl.get_variable(f"xz{i}").value() for i in range(1, 5))
    yellow_gas = sum(ampl.get_variable(f"xa{i}").value() for i in range(1, 5))

    print(f"Super gasoline:  {super_gas:,.2f} barrels")
    print(f"Blue gasoline:   {blue_gas:,.2f} barrels")
    print(f"Yellow gasoline: {yellow_gas:,.2f} barrels")
    print(f"Maximum total profit: R$ {ampl.get_objective('z').value():,.2f}")


if __name__ == "__main__":
    main()
