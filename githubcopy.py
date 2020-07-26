from shutil import copytree, rmtree
from pathlib import Path

BUILT_HTML = Path(__file__).parent / "build/html"
DOCS = Path(__file__).parent / "docs"

rmtree(DOCS)
copytree(BUILT_HTML, DOCS)