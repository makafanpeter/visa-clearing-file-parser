# pragma: no cover
# Ensure local src package is imported during tests for accurate coverage
import sys
from pathlib import Path

# Prepend the src directory to sys.path so that `import visa_clearing` resolves to local code
project_root = Path(__file__).resolve().parents[1]
src_path = project_root / 'src'
if str(src_path) not in sys.path:
    sys.path.insert(0, str(src_path))
