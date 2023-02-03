import pytest
from src.report.f1_report import app_f1


@pytest.fixture
def app():
    yield app_f1

@pytest.fixture()
def client(app):
    return app.test_client()

@pytest.fixture
def runner(app):
    return app.test_cli_runner()
