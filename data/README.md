# Datos

Esta carpeta **no versiona archivos de datos** (`.gitignore` los excluye) para evitar publicar información real por accidente.

## Formato esperado

Un CSV con una fila por día:

| columna | tipo | descripción |
|---|---|---|
| `fecha` | fecha (`AAAA-MM-DD`) | un registro por día |
| `ventas` | número | ventas del día (en tu moneda o unidades) |

## Datos de ejemplo (sintéticos)

```bash
python scripts/generate_sample_data.py
```

Crea `data/ventas_ejemplo.csv` con 730 días **sintéticos**. Sirven para probar el flujo; no representan a ningún negocio.

## Usar datos reales

1. Guarda tu archivo aquí como `data/ventas.csv` con las columnas de arriba.
2. En el notebook cambia `DATA_PATH` a `../data/ventas.csv`.
3. **Anonimiza** antes de publicar resultados (sin nombres de clientes, sin ubicaciones exactas, sin montos identificables) y confirma por escrito que el dueño de los datos autoriza su uso.
