import pytest
from utils.endpoints import Endpoints
from utils.url_builder import URLBuilder
from utils.schema_validator import validate_response_schema
from data.schema.schema import *
from data.payload.postdata import *

@pytest.mark.Smoke
@pytest.mark.Regression
def test_TC03_Put_Endpoint(api_client):
    endpoint = URLBuilder.format(Endpoints.UPDATE_USER, user_id=2)
    response = api_client.put(endpoint, update_user_payload)

    response_data = response.json()
    assert response_data["name"] == "neo"
    assert response.status_code == 200, "API health check failed"
    # Validate the response schema using the SchemaValidator
    validation_result = validate_response_schema(response_data, updated_response_schema)
    assert validation_result is True, validation_result  # Assert validation result is True
    print("Health check passed.")