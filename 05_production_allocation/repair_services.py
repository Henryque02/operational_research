"""Mix de serviços de reparo — maximização de receita (PL).

Uma oficina oferece serviço padrão e serviço premium, ambos consumindo horas
das bancadas de reparo e de testes, com mínimos contratuais de cada serviço.
O objetivo é maximizar a receita. Enunciado completo em
``assets/repair_services_statement.png``.
"""

from operational_research import setup_ampl


def main() -> None:
    ampl = setup_ampl()

    ampl.eval("""
        var standard_service >= 0;
        var premium_service >= 0;
        maximize z: 10*standard_service + 30*premium_service;
        subject to
            repair_bench: standard_service + 2*premium_service <= 24;
            testing_bench: 2*standard_service + 2*premium_service <= 36;
            min_standard: standard_service >= 4;
            min_premium: premium_service >= 2;
        solve;
    """)

    print(f"standard_service = {ampl.get_variable('standard_service').value()}")
    print(f"premium_service = {ampl.get_variable('premium_service').value()}")
    print(f"Maximum revenue: {ampl.get_objective('z').value()}")


if __name__ == "__main__":
    main()
