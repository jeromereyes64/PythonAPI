import pytest
from data.schema.schema import create_response_schema
from utils.schema_validator import validate_response_schema
from utils.endpoints import Endpoints
from utils.url_builder import URLBuilder
from data.payload.postdata import *


@pytest.mark.Regression
def test_TC01_Health_Check(api_client):
    """Test to verify API is reachable."""
    endpoint = URLBuilder.format(Endpoints.HEALTH_CHECK, page=2)
    response = api_client.get(endpoint)
    assert response.status_code == 200, "API health check failed"
    print("Health check passed.")

@pytest.mark.Regression
def test_TC02_Login(api_client):
    """Test to verify user login functionality."""
    # Create an instance of the DataPayload class to load the payload
    """Use this if you want payload to come from a file"""
    #payload = DataPayload(file_path="data/payload/postdata.json").get_payload()

    response = api_client.post(Endpoints.USERS, create_user_payload)

    ## Parse the response data
    response_data = response.json()
    assert response.status_code == 201, "Create Failed"
    # Validate the response schema using the SchemaValidator
    validation_result = validate_response_schema(response_data, create_response_schema)
    assert validation_result is True, validation_result  # Assert validation result is True


@pytest.mark.Smoke
@pytest.mark.Regression
def test_TC03_Invalid_Endpoint(api_client):
    """Test to verify API handles invalid endpoints correctly."""
    response = api_client.get(Endpoints.INVALID)
    assert response.status_code == 404, "Invalid endpoint did not return 404"
    print("Invalid endpoint correctly handled.")
