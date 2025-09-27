# Datos

Esta carpeta contiene todos los conjuntos de datos utilizados en el TFM.

## Estructura

- `raw/` - Datos originales sin procesar
- `processed/` - Datos procesados y limpios
- `external/` - Datos de fuentes externas
- `interim/` - Datos intermedios durante el procesamiento

## Organización de Archivos

```
data/
├── raw/                # Datos originales
│   ├── dataset1/
│   └── dataset2/
├── processed/          # Datos procesados
│   ├── clean_data/
│   └── features/
├── external/           # Referencias externas
└── interim/            # Datos temporales
```

## Buenas Prácticas

1. **Nunca modificar datos raw/** - Mantener siempre los datos originales
2. **Documentar el origen** - Incluir información sobre la fuente de datos
3. **Scripts de procesamiento** - Guardar en `src/data/` los scripts de limpieza
4. **Metadatos** - Incluir archivos README.md para describir cada dataset

## Formatos Recomendados

- CSV para datos tabulares
- JSON para datos estructurados
- HDF5 o Parquet para datasets grandes
- Documentar formato y esquema en archivos README.md