# Data Quality CI

Proyecto de ejemplo que demuestra CI/CD para validación de calidad de datos usando GitHub Actions.

## Estructura

- `data/raw/`: Datos CSV de ejemplo
- `src/`: Código de validación usando pandera
- `tests/`: Pruebas de validación
- `.github/workflows/`: Workflow de GitHub Actions

## Uso

```bash
pip install -r requirements.txt
pytest tests/
```
