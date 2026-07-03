"""Otimização de recursos para produção de equipamentos — minimização de custo (PL).

Enunciado: Uma empresa de tecnologia precisa produzir dois tipos de componentes
eletrônicos: Componente X e Componente Y, utilizando dois recursos escassos:
Chipset e Memória RAM. O objetivo é minimizar os custos de produção garantindo
que as demandas mínimas de chipset e memória sejam atendidas. A tabela em
``assets/electronic_components_table.png`` resume a quantidade de cada recurso
necessária para produzir uma unidade de cada componente, assim como o custo de
produção de cada um.
"""

from operational_research import setup_ampl


def main() -> None:
    ampl = setup_ampl()

    ampl.eval("""
        var component_x >= 0;
        var component_y >= 0;
        minimize z: 2*component_x + 4.50*component_y;
        subject to
            min_ram: 20*component_x + 5*component_y >= 80;
            min_chipset: 3*component_x + 40*component_y >= 25;
    """)

    ampl.solve()
    print(f"Minimum cost: {ampl.get_objective('z').value()}")
    print(f"component_x = {ampl.get_variable('component_x').value()}")
    print(f"component_y = {ampl.get_variable('component_y').value()}")


if __name__ == "__main__":
    main()
