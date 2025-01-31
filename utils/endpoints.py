class Endpoints:
    USERS = "users"
    LOGIN = "auth/login"
    HEALTH_CHECK = "users?page={page}"
    INVALID = "test/invalid_endpoint"
    CREATE_USER = "users"
    UPDATE_USER = "users/{user_id}"
    DELETE_USER = "users/{user_id}"
