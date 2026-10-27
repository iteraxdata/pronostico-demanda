# Pronóstico de demanda diaria

Proyecto de data science de [iterAX Data](https://iterax-data.pages.dev): **¿cuántas ventas habrá en los próximos días y qué día conviene reforzar inventario o turnos?**

> Estado: esqueleto. Por defecto usa **datos sintéticos**; sustitúyelos por datos reales (anonimizados) antes de sacar conclusiones.

## Qué hace el notebook

`notebooks/01_pronostico_demanda.ipynb` recorre el flujo completo:

1. **Carga y calidad:** nulos, fechas duplicadas, huecos; serie diaria limpia.
2. **Exploración:** tendencia, media móvil y patrón por día de la semana.
3. **Validación temporal:** entrena con el pasado y prueba con las últimas 8 semanas (nunca una división al azar).
4. **Línea base:** "el mismo día de la semana pasada".
5. **Modelo:** suavizado exponencial Holt-Winters (tendencia amortiguada + estacionalidad semanal).
6. **Métricas:** MAE y WAPE, con la mejora frente a la línea base.
7. **Pronóstico:** próximos 14 días y el día de mayor demanda esperada.
8. **Exportables:** `reports/forecast.html` (gráfico interactivo) y `reports/pronostico.csv`.

## Cómo ejecutarlo

Requiere Python 3.10 o superior. Probado con Python 3.12, pandas 3.1, numpy 2.5, statsmodels 0.15 y plotly 7.1 (ejecución completa del notebook sin errores ni avisos).

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate    |    macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt

python scripts/generate_sample_data.py     # datos sintéticos de ejemplo
jupyter lab notebooks/01_pronostico_demanda.ipynb
```

Para exportar el notebook como página HTML (por ejemplo, para el sitio):

```bash
jupyter nbconvert --to html notebooks/01_pronostico_demanda.ipynb --output-dir reports
```

## Estructura

```
.
├── data/                # aquí van tus CSV (no se versionan); ver data/README.md
├── notebooks/           # el análisis
├── reports/             # salidas: gráfico HTML, CSV de pronóstico, notebook en HTML
├── scripts/             # utilidades (generador de datos sintéticos)
└── requirements.txt
```

## Resultados

*(completar con los números reales del notebook: MAE y WAPE de la línea base vs. el modelo, mejora relativa, día pico y la decisión que habilita)*

## Limitaciones

- Con datos sintéticos los resultados **no** describen ningún negocio.
- El modelo no incorpora clima, promociones ni días festivos; son los siguientes pasos naturales.

## Licencia

*(por definir antes de hacer público el repositorio; sin licencia, el código queda con todos los derechos reservados)*

---

Hecho en Tampico, Tamaulipas · [iterAX Data](https://iterax-data.pages.dev)
