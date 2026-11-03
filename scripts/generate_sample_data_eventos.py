"""Genera datos SINTÉTICOS de ventas diarias con días festivos de México y promociones.

Igual que generate_sample_data.py, no son datos de ningún negocio. Aquí el efecto de
los festivos (+25 %) y de las promociones (+30 %) está incluido a propósito, para
practicar cómo medir si agregarlos como variables mejora el pronóstico. En datos
reales el efecto puede ser mayor, menor o inexistente: por eso se mide.

Uso:
    python scripts/generate_sample_data_eventos.py
"""
from pathlib import Path

import holidays
import numpy as np
import pandas as pd

SEED = 7
DAYS = 1095  # tres años de historia diaria
EFECTO_FESTIVO = 1.25
EFECTO_PROMO = 1.30
N_PROMOS = 40


def main() -> None:
    rng = np.random.default_rng(SEED)
    fechas = pd.date_range("2023-01-01", periods=DAYS, freq="D")

    base = 100.0
    tendencia = np.linspace(0, 35, DAYS)
    factor_semana = np.array([0.85, 0.90, 1.00, 1.15, 1.30, 1.45, 1.10])  # lun..dom
    estacional = factor_semana[fechas.day_of_week.to_numpy()]
    anual = 1 + 0.08 * np.sin(2 * np.pi * fechas.day_of_year.to_numpy() / 365.25)
    ruido = rng.normal(0, 6, DAYS)

    ventas = (base + tendencia) * estacional * anual + ruido

    festivos = holidays.country_holidays("MX", years=sorted(set(fechas.year)))
    es_festivo = np.array([d.date() in festivos for d in fechas])
    ventas[es_festivo] *= EFECTO_FESTIVO

    promo = np.zeros(DAYS, dtype=int)
    promo[rng.choice(DAYS, size=N_PROMOS, replace=False)] = 1
    ventas[promo == 1] *= EFECTO_PROMO

    ventas = np.clip(ventas, 0, None).round(2)
    df = pd.DataFrame({"fecha": fechas, "ventas": ventas, "promo": promo})

    destino = Path(__file__).resolve().parents[1] / "data" / "ventas_ejemplo_eventos.csv"
    destino.parent.mkdir(exist_ok=True)
    df.to_csv(destino, index=False)
    print(f"Listo: {destino} ({len(df)} filas, {int(es_festivo.sum())} festivos, {int(promo.sum())} promos, SINTÉTICO)")


if __name__ == "__main__":
    main()
