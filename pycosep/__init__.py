from importlib.metadata import version, PackageNotFoundError

try:
    __version__ = version("pycosep")
except PackageNotFoundError:
    # package is not installed
    pass
