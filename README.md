# Lab12 - Big Data

Análisis de citas médicas con pandas y SQL Server.

## Archivos

- `script_!2.py` - Genera 5000 registros ficticios de citas médicas
- `sript_3.py` - Consulta SQL y calcula KPI de cancelaciones
- `citas_bigdata.csv` - Datos generados

## Requisitos

```bash
pip install pandas pyodbc sqlalchemy faker
```

## Uso

1. Generar datos:
```bash
python script_!2.py
```

2. Consultar KPIs:
```bash
python sript_3.py
```

## Configuración

Editar variables en `sript_3.py`:
```python
USER = "sa"
PASSWORD = "tu_password"
SERVER = "localhost"
DATABASE = "ClinicaBigData"
```
