from jinja2 import Environment, PackageLoader, select_autoescape
from pytest import fixture

@fixture
def jinja_environment():
    return Environment(
        loader=PackageLoader("testAssets"),
        autoescape=select_autoescape()
    )
