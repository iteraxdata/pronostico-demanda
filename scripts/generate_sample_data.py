"""Genera datos SINTÉTICOS de ventas diarias para probar el notebook.

No son datos reales de ningún negocio: sirven para ejecutar el flujo completo
(limpieza -> exploración -> modelo -> pronóstico) sin exponer información de clientes.

Uso:
    python scripts/generate_sample_data.py
"""
from pathlib import Path

import numpy as np
import pandas as pd

SEED = 42
DAYS = 730  # dos años de historia diaria


def main() -> None:
    rng = np.random.default_rng(SEED)
    fechas = pd.date_range("2024-01-01", periods=DAYS, freq="D")

    base = 100.0
    tendencia = np.linspace(0, 25, DAYS)  # crecimiento suave
    factor_semana = np.array([0.85, 0.90, 1.00, 1.15, 1.30, 1.45, 1.10])  # lun..dom
    estacional = factor_semana[fechas.day_of_week.to_numpy()]
    anual = 1 + 0.08 * np.sin(2 * np.pi * fechas.day_of_year.to_numpy() / 365.25)
    ruido = rng.normal(0, 6, DAYS)

    ventas = (base + tendencia) * estacional * anual + ruido

    # algunos días atípicos (promociones / eventos)
    idx = rng.choice(DAYS, size=8, replace=False)
    ventas[idx] *= rng.uniform(1.25, 1.5, size=8)
    ventas = np.clip(ventas, 0, None).round(2)

    df = pd.DataFrame({"fecha": fechas, "ventas": ventas})

    destino = Path(__file__).resolve().parents[1] / "data" / "ventas_ejemplo.csv"
    destino.parent.mkdir(exist_ok=True)
    df.to_csv(destino, index=False)
    print(f"Listo: {destino} ({len(df)} filas, SINTÉTICO)")


if __name__ == "__main__":
    main()
