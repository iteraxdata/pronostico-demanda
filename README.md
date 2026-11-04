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

## Segundo notebook: mejoras al pronóstico

`notebooks/02_mejoras_pronostico.ipynb` retoma el anterior y responde cuatro preguntas:

1. **Validación walk-forward:** ¿la mejora se sostiene en 8 ventanas del tiempo o fue suerte de una sola prueba?
2. **Festivos y promociones:** ¿cuánto baja el error al agregar los días festivos de México (`holidays`) y las promociones como variables?
3. **Más modelos:** línea base, Holt-Winters, SARIMA y árboles de decisión con y sin eventos (`scikit-learn`).
4. **Rango del pronóstico:** un intervalo del 80 % calibrado con errores pasados y comprobado en ventanas que no se usaron para calibrar.

Usa un conjunto de datos sintético distinto, con el efecto de festivos y promociones incluido a propósito:

```bash
python scripts/generate_sample_data_eventos.py
jupyter lab notebooks/02_mejoras_pronostico.ipynb
```

Con esos datos el modelo de árboles con eventos obtuvo el menor error y el rango del 80 % cubrió el 74 % de los valores de validación. Como el efecto está sembrado en los datos, esto demuestra la técnica, no que los festivos o promociones ayuden en un negocio real: con datos reales se mide igual y el resultado puede ser otro.

## Cómo ejecutarlo

Requiere Python 3.10 o superior. Probado con Python 3.12, pandas 3.1, numpy 2.5, statsmodels 0.15 y plotly 7.1 (ejecución completa del notebook sin errores ni avisos).

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate    |    macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt

python scripts/generate_sample_data.py     # datos sintéticos de ejemplo
jupyter lab notebooks/01_pronostico_demanda.ipynb
```

Para exportar el notebook ejecutado como página HTML con sus gráficos interactivos (por ejemplo, para el sitio), indica el renderizador de Plotly; sin él, la exportación omite los gráficos:

```bash
# macOS/Linux
PLOTLY_RENDERER=notebook_connected jupyter nbconvert --to html --execute notebooks/01_pronostico_demanda.ipynb --output-dir reports --output notebook.html
```

```powershell
# Windows (PowerShell)
$env:PLOTLY_RENDERER = "notebook_connected"
jupyter nbconvert --to html --execute notebooks/01_pronostico_demanda.ipynb --output-dir reports --output notebook.html
```

Los gráficos se cargan desde el CDN de Plotly, así que el HTML necesita conexión a internet al abrirse.

## Estructura

```
.
├── data/                # aquí van tus CSV (no se versionan); ver data/README.md
├── notebooks/           # el análisis
├── reports/             # salidas: gráfico HTML, CSV de pronóstico, notebook en HTML
├── scripts/             # generadores de datos sintéticos (básico y con festivos/promociones)
└── requirements.txt
```

## Resultados

*(completar con los números reales del notebook: MAE y WAPE de la línea base vs. el modelo, mejora relativa, día pico y la decisión que habilita)*

## Limitaciones

- Con datos sintéticos los resultados **no** describen ningún negocio.
- El modelo no incorpora clima, promociones ni días festivos; son los siguientes pasos naturales.

## Licencia

[MIT](LICENSE) © 2026 iterAX Data. La licencia cubre el **código** de este repositorio. Los datos que uses con él siguen siendo de sus dueños: no los publiques sin autorización.

---

Hecho en Tampico, Tamaulipas · [iterAX Data](https://iterax-data.pages.dev)
