"""
GRIP++ vendorized package.

This package intentionally does not export everything at top-level to avoid
exposing implementation details. Use imports such as `from grip.model import Model`.
"""
__all__ = [
    "model",
    "xin_feeder_baidu",
    "data_process",
    "layers",
]

__version__ = "0.0.1"
