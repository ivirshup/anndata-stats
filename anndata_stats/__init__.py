from importlib.metadata import version

from ._core.grouped_stats import CountMeanVar, GroupBy

__all__ = ["GroupBy", "CountMeanVar"]

__version__ = version("anndata-stats")
