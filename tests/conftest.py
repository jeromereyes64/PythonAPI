import pytest
import json
from src.api_client import APIClient

def pytest_addoption(parser):
    """Allows the user to select the test environment (qa/uat)"""
    parser.addoption("--env", action="store", default="qa", help="Environment to run tests against (qa/uat)")


@pytest.fixture(scope="session")
def config(pytestconfig):
    """Loads the selected environment's configuration from config.json"""
    env = pytestconfig.getoption("--env") or "qa"
    with open("utils/config.json", "r") as file:
        configs = json.load(file)

    if env not in configs:
        raise ValueError(f"Invalid environment: {env}. Use 'qa' or 'uat'.")

    return configs[env]


@pytest.fixture(scope="session")
def api_client(config):
    """Initialize API client with environment's base URL and token"""
    return APIClient(base_url=config["base_url"], auth_token=config["auth_token"])