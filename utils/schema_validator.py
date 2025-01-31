from jsonschema import validate, ValidationError

def validate_response_schema(response_data, schema):
    """Validate the response data against the provided schema variable."""
    try:
        validate(instance=response_data, schema=schema)  # Validate against the provided schema variable
        return True  # If validation passes
    except ValidationError as e:
        return f"Schema validation failed: {str(e)}"
