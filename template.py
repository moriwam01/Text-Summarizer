import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format="[%(ascitime)s] %(message)s:")


project_name = "TextSummarizer"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
]
