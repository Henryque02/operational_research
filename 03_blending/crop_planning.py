"""Planejamento agrícola de um sítio — dois modelos equivalentes (PL).

Alocação de área entre trigo, arroz e milho para maximizar o lucro, sujeita a
áreas mínimas por cultura, área total disponível e limite de produção em
toneladas. Enunciado completo em ``assets/crop_planning_statement.png``.

O mesmo problema é modelado de duas formas equivalentes — um exercício de
modelagem para mostrar que a escolha da variável de decisão muda o modelo,
mas não a solução ótima:

* ``area_model``     — variável de decisão: área plantada (m²) por cultura.
* ``quantity_model`` — variável de decisão: quantidade produzida (kg) por
  cultura, convertendo área via produtividade (kg/m²).
"""

from operational_research import setup_ampl

# Produtividade (kg por m²)
WHEAT_YIELD, RICE_YIELD, CORN_YIELD = 0.2, 0.3, 0.4


def area_model() -> None:
    """Modelo 1: decide a área plantada por cultura."""
    ampl = setup_ampl("highs")

    ampl.eval("""
        var wheat_area >= 0;
        var rice_area >= 0;
        var corn_area >= 0;

        maximize z: 2.16*wheat_area + 1.26*rice_area + 0.812*corn_area;

        subject to
            min_wheat_area: wheat_area >= 400;
            min_rice_area: rice_area >= 800;
            min_corn_area: corn_area >= 10000;
            max_total_area: wheat_area + rice_area + corn_area <= 200000;
            max_total_tons: 0.2*wheat_area + 0.3*rice_area + 0.4*corn_area <= 60000;
        solve;
    """)

    wheat = ampl.get_variable("wheat_area").value()
    rice = ampl.get_variable("rice_area").value()
    corn = ampl.get_variable("corn_area").value()
    profit = ampl.get_objective("z").value()

    print("\n" + "=" * 50)
    print("MODEL 1 RESULTS (decision variable: area)")
    print(f"Wheat area: {wheat:,.2f} m²")
    print(f"Rice area:  {rice:,.2f} m²")
    print(f"Corn area:  {corn:,.2f} m²")
    print(f"Total area: {wheat + rice + corn:,.2f} m²")
    print("-" * 50)
    print("PRODUCTION (kg):")
    print(f"Wheat: {WHEAT_YIELD * wheat:,.2f} kg")
    print(f"Rice:  {RICE_YIELD * rice:,.2f} kg")
    print(f"Corn:  {CORN_YIELD * corn:,.2f} kg")
    print(f"Maximum profit: R$ {profit:,.2f}")
    print("=" * 50 + "\n")


def quantity_model() -> None:
    """Modelo 2: decide a quantidade produzida (kg) por cultura."""
    ampl = setup_ampl("highs")

    ampl.eval("""
        var wheat_qty >= 0;
        var rice_qty >= 0;
        var corn_qty >= 0;

        maximize z: 10.8*wheat_qty + 4.2*rice_qty + 2.03*corn_qty;

        subject to
            min_wheat_qty: wheat_qty >= 80;
            min_rice_qty: rice_qty >= 240;
            min_corn_qty: corn_qty >= 4000;
            max_total_area: (wheat_qty/0.2) + (rice_qty/0.3) + (corn_qty/0.4) <= 200000;
            max_production: wheat_qty + rice_qty + corn_qty <= 60000;
        solve;
    """)

    wheat = ampl.get_variable("wheat_qty").value()
    rice = ampl.get_variable("rice_qty").value()
    corn = ampl.get_variable("corn_qty").value()
    profit = ampl.get_objective("z").value()

    print("\n" + "=" * 50)
    print("MODEL 2 RESULTS (decision variable: quantity)")
    print(f"Wheat: {wheat:,.2f} kg")
    print(f"Rice:  {rice:,.2f} kg")
    print(f"Corn:  {corn:,.2f} kg")
    print(f"Total production: {wheat + rice + corn:,.2f} kg")
    print("-" * 50)
    print("AREA (m²):")
    print(f"Wheat: {wheat / WHEAT_YIELD:,.2f} m²")
    print(f"Rice:  {rice / RICE_YIELD:,.2f} m²")
    print(f"Corn:  {corn / CORN_YIELD:,.2f} m²")
    print(f"Maximum profit: R$ {profit:,.2f}")
    print("=" * 50 + "\n")


if __name__ == "__main__":
    area_model()
    quantity_model()
