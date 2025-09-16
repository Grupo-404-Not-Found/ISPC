# SmartHome (TDD) — Programación I

Proyecto de ejemplo para la Evidencia: **implementación de clases con TDD** (Red→Green→Refactor), alineadas al UML.

## Estructura
```
smarthome_tdd/
├─ src/smarthome/
│  ├─ __init__.py
│  ├─ modelo.py
│  └─ automatizaciones.py
├─ tests/
│  ├─ test_modelo.py
│  └─ test_automatizaciones.py
├─ requirements.txt
└─ README.md
```

## Cómo ejecutar
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# Linux/Mac:
source .venv/bin/activate

pip install -r requirements.txt
pytest -q
```

## Flujo TDD sugerido (commits)
1) RED: agregar tests vacíos o con expectativas (fallan)  
2) GREEN: implementar lo mínimo para pasar los tests  
3) REFACTOR: limpiar código manteniendo tests en verde
