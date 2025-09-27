# Código Fuente

Esta carpeta contiene todo el código desarrollado para el TFM.

## Estructura

```
src/
├── data/               # Scripts para manejo de datos
│   ├── make_dataset.py
│   ├── clean_data.py
│   └── validate_data.py
├── features/           # Generación de características
│   └── build_features.py
├── models/             # Modelos de análisis
│   ├── train_model.py
│   └── predict_model.py
├── visualization/      # Código para visualizaciones
│   └── visualize.py
├── utils/              # Utilidades y funciones auxiliares
│   └── helpers.py
└── analysis/           # Análisis específicos del TFM
    └── functional_analysis.py
```

## Lenguajes y Herramientas

- Python para análisis estadístico y machine learning
- R para análisis de datos funcionales
- Jupyter Notebooks para análisis exploratorio
- Scripts de shell para automatización

## Estándares de Código

- Seguir PEP 8 para Python
- Documentar funciones con docstrings
- Incluir tests cuando sea apropiado
- Usar nombres descriptivos para variables y funciones

## Dependencias

Mantener archivos de dependencias actualizados:
- `requirements.txt` para Python
- `environment.yml` para conda
- `DESCRIPTION` para R