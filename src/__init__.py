from ._metadata import __version__, within_flit
import importlib
import subprocess
import warnings

from pathlib import Path
basedir = Path(__file__).parent

if not within_flit():  # see function docstring on why this is there
    # the actual API
    # (start with settings as several tools are using it)
    from . import tools as tl
    from . import preprocessing as pp
    from . import plotting as pl
    from . import utilities as ut

    from anndata import AnnData, concat
    from anndata import (
        read_h5ad,
        read_csv,
        read_excel,
        read_hdf,
        read_loom,
        read_mtx,
        read_text,
        read_umi_tools,
    )

    # has to be done at the end, after everything has been imported
    import sys
    sys.modules.update(
        {
            f"{__name__}.{m}": globals()[m]
            for m in ["tl", "pp", "pl", "ut"]
        }
    )
    del sys


