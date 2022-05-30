from importlib.metadata import version

from ._core.grouped_stats import GroupBy

__all__ = ["GroupBy"]

__version__ = version("anndata-stats")
