import sys

if sys.version_info >= (3, 0):
    from pathlib import Path
else:
    from pathlib2 import Path

# Constants
VEP_PLUGIN_COMMIT = "3be3889"
VEP_VERSION = "87.24"
ROOT = Path('resources').resolve()
VEP_ROOT = ROOT / 'vep'
BIN = (ROOT / 'usr' / 'bin')
VEP_BIN = VEP_ROOT / 'vep.pl'
PLUGIN_ROOT = ROOT / 'vep_plugins'
VEP_CACHE = ROOT / 'vep_cache'
