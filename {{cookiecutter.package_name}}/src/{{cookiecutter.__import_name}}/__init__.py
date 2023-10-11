"""{{ cookiecutter.package_short_description }}"""

from importlib_metadata import PackageNotFoundError, version

try:
    __version__ = version("{{ cookiecutter.__import_name }}")
except PackageNotFoundError as error:
    raise ModuleNotFoundError( # noqa: TRY003, EM101
        "Unable to determine version of package."
    ) from error
