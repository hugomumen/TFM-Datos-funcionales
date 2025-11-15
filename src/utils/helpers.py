"""
Utilidades auxiliares para el análisis de datos funcionales.

Este módulo contiene funciones comunes utilizadas a lo largo del proyecto.
"""

import numpy as np
import pandas as pd
from typing import Union, List, Tuple
import matplotlib.pyplot as plt
import seaborn as sns


def setup_plotting_style():
    """
    Configurar el estilo por defecto para las visualizaciones.
    """
    plt.style.use('seaborn-v0_8')
    sns.set_palette("husl")
    plt.rcParams['figure.figsize'] = (10, 6)
    plt.rcParams['font.size'] = 12


def load_functional_data(filepath: str) -> pd.DataFrame:
    """
    Cargar datos funcionales desde archivo.
    
    Args:
        filepath: Ruta al archivo de datos
        
    Returns:
        DataFrame con los datos cargados
    """
    try:
        if filepath.endswith('.csv'):
            return pd.read_csv(filepath)
        elif filepath.endswith('.xlsx'):
            return pd.read_excel(filepath)
        else:
            raise ValueError("Formato de archivo no soportado")
    except Exception as e:
        print(f"Error al cargar datos: {e}")
        return None


def validate_functional_data(data: pd.DataFrame) -> dict:
    """
    Validar la calidad de los datos funcionales.
    
    Args:
        data: DataFrame a validar
        
    Returns:
        Diccionario con estadísticas de validación
    """
    validation_stats = {
        'shape': data.shape,
        'missing_values': data.isnull().sum().sum(),
        'duplicates': data.duplicated().sum(),
        'dtypes': data.dtypes.to_dict(),
        'memory_usage': data.memory_usage(deep=True).sum()
    }
    
    return validation_stats


def print_project_info():
    """
    Imprimir información del proyecto.
    """
    print("="*50)
    print("TFM - Análisis de Datos Funcionales")
    print("="*50)
    print("Utilidades auxiliares cargadas correctamente")
    print("Para más información, consulte la documentación")
    print("="*50)


if __name__ == "__main__":
    print_project_info()