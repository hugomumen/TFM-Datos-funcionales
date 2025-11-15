# Resultados

Esta carpeta contiene todos los resultados generados durante el desarrollo del TFM.

## Estructura

```
results/
├── figures/            # Gráficos y visualizaciones
│   ├── exploratory/    # Análisis exploratorio
│   ├── models/         # Resultados de modelos
│   └── final/          # Figuras para la tesis
├── tables/             # Tablas de resultados
├── models/             # Modelos entrenados guardados
├── reports/            # Reportes de análisis
└── logs/               # Logs de experimentos
```

## Organización de Archivos

### Figuras
- Usar nombres descriptivos: `distribution_dataset1.png`
- Mantener versiones en alta resolución para la tesis
- Organizar por tema o capítulo

### Tablas
- Formato CSV para facilidad de lectura
- Incluir metadatos sobre cómo se generaron
- Versiones en LaTeX para inclusión en tesis

### Modelos
- Guardar modelos entrenados con pickle/joblib
- Incluir parámetros y métricas de evaluación
- Documentar versión de datos utilizada

## Versionado de Resultados

- Usar fechas en nombres de archivos cuando sea relevante
- Mantener un log de experimentos importantes
- Backup de resultados críticos

## Formatos Recomendados

- PNG/PDF para figuras
- CSV para tablas
- JSON para metadatos y configuraciones