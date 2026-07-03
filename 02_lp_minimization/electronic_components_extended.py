"""Versão estendida do problema dos componentes eletrônicos (PL, minimização).

Extensão proposta em aula sobre o problema base (``electronic_components.py``):

1. Mais variáveis — cinco componentes (X, Y, Z, W e H) em vez de dois.
2. Mais restrições — além de Chipset e Memória RAM, entram Energia Elétrica
   (kWh) e Mão-de-obra (horas de produção).

O objetivo continua sendo minimizar o custo total de produção atendendo às
demandas mínimas de cada recurso.
"""

from operational_research import setup_ampl


def main() -> None:
    ampl = setup_ampl()

    ampl.eval("""
        var component_x >= 0;
        var component_y >= 0;
        var component_z >= 0;
        var component_w >= 0;
        var component_h >= 0;
        minimize z: 2*component_x + 4.50*component_y + 7*component_z
                  + 1.5*component_w + 3.75*component_h;
        subject to
            min_ram: 20*component_x + 5*component_y >= 80;
            min_chipset: 3*component_x + 40*component_y >= 25;
            min_electric_energy: 40*component_x + 3*component_y + 72*component_z
                               + 25*component_w + 7*component_h >= 50;
            min_labor_hours: 1*component_x + 8*component_y + 32*component_z
                           + 43*component_w + 29*component_h >= 74;
    """)

    ampl.solve()
    print(f"Minimum cost: {ampl.get_objective('z').value()}")
    for var in ("component_x", "component_y", "component_z", "component_w", "component_h"):
        print(f"{var} = {ampl.get_variable(var).value()}")


if __name__ == "__main__":
    main()
