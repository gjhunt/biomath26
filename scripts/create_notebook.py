"""Legacy entry point: refresh figures while preserving the editable notebook.

The notebook is now the source of truth; this script no longer recreates it.
"""
import runpy
from pathlib import Path
runpy.run_path(str(Path(__file__).with_name("create_figures.py")), run_name="__main__")
print("Notebook edits preserved; render with make.")
