"""
Script simple para verificar la estructura del proyecto.
No requiere dependencias externas.
"""

import os
import sys
from pathlib import Path


def check_project_structure():
    """
    Verificar que la estructura del proyecto esté completa.
    """
    print("🔍 Verificando estructura del proyecto TFM...")
    print("="*50)
    
    required_dirs = [
        'docs', 'data', 'src', 'results', 'literature',
        'docs/thesis', 'docs/notes', 'docs/presentations', 'docs/meetings',
        'data/raw', 'data/processed', 'data/external', 'data/interim',
        'src/data', 'src/features', 'src/models', 'src/visualization', 'src/utils', 'src/analysis',
        'results/figures', 'results/tables', 'results/models', 'results/reports', 'results/logs',
        'literature/papers', 'literature/books', 'literature/bibliography', 'literature/reviews', 'literature/summaries'
    ]
    
    required_files = [
        'README.md', 'SETUP.md', '.gitignore', 'requirements.txt',
        'src/utils/helpers.py', 'literature/bibliography/references.bib',
        'results/logs/experiment_log.md', 'docs/notes/template_nota.md'
    ]
    
    # Verificar directorios
    print("📁 Verificando directorios:")
    all_dirs_ok = True
    for dir_path in required_dirs:
        if os.path.exists(dir_path) and os.path.isdir(dir_path):
            print(f"  ✅ {dir_path}")
        else:
            print(f"  ❌ {dir_path} - FALTANTE")
            all_dirs_ok = False
    
    print("\n📄 Verificando archivos clave:")
    all_files_ok = True
    for file_path in required_files:
        if os.path.exists(file_path) and os.path.isfile(file_path):
            print(f"  ✅ {file_path}")
        else:
            print(f"  ❌ {file_path} - FALTANTE")
            all_files_ok = False
    
    # Resumen
    print("\n" + "="*50)
    if all_dirs_ok and all_files_ok:
        print("🎉 ¡Estructura del proyecto verificada correctamente!")
        print("📋 El repositorio está listo para comenzar el trabajo del TFM.")
        print("\n📖 Próximos pasos:")
        print("  1. Leer SETUP.md para configurar el entorno")
        print("  2. Instalar dependencias: pip install -r requirements.txt")
        print("  3. Comenzar a subir datos a data/raw/")
        print("  4. Documentar avances en docs/notes/")
        return True
    else:
        print("⚠️  Hay elementos faltantes en la estructura del proyecto.")
        return False


if __name__ == "__main__":
    success = check_project_structure()
    sys.exit(0 if success else 1)