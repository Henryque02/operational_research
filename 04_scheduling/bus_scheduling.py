"""Programação de frota de ônibus — cobertura de turnos (PL).

Minimizar o número total de ônibus necessários para cobrir a demanda mínima em
seis janelas de 4 horas ao longo do dia, sabendo que cada ônibus opera por dois
turnos consecutivos. Enunciado completo em
``assets/bus_scheduling_statement.png``.

Este é o clássico problema de *shift scheduling* com sobreposição de turnos:
cada restrição soma os dois grupos de ônibus ativos naquela janela.
"""

from operational_research import setup_ampl


def main() -> None:
    ampl = setup_ampl()

    ampl.eval("""
        var bus1 >= 0;
        var bus2 >= 0;
        var bus3 >= 0;
        var bus4 >= 0;
        var bus5 >= 0;
        var bus6 >= 0;
        minimize z: bus1 + bus2 + bus3 + bus4 + bus5 + bus6;
        subject to
            shift_00_04: bus1 + bus6 >= 4;
            shift_04_08: bus1 + bus2 >= 8;
            shift_08_12: bus2 + bus3 >= 10;
            shift_12_16: bus3 + bus4 >= 7;
            shift_16_20: bus4 + bus5 >= 12;
            shift_20_00: bus5 + bus6 >= 4;
        solve;
    """)

    for i in range(1, 7):
        value = ampl.get_variable(f"bus{i}").value()
        print(f"Buses starting at shift {i}: {value}")
    print(f"Total number of buses: {ampl.get_objective('z').value()}")


if __name__ == "__main__":
    main()
