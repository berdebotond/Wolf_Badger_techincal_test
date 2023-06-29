from flask_dance.contrib.github import github


def check_auth() -> bool:
    """
    Check if the user is authenticated
    :return: bool
    """
    if not github.authorized:
        return False
    return True


#json schema
user_schema_update = {
    "type": "object",
    "properties": {
        "login": {
            "type": "string",
            "minLength": 1,
            "maxLength": 80
        },
        "name": {
            "type": "string",
            "minLength": 1,
            "maxLength": 80
        },
        "email": {
            "type": "string",
            "format": "email",
            "minLength": 1,
            "maxLength": 120
        },
        "location": {
            "type": "string",
            "maxLength": 120
        }
    },
    "required": [],
    "additionalProperties": False,
}
# json schema for user
user_schema_create = {
    "type": "object",
    "properties": {
        "login": {
            "type": "string",
            "minLength": 1,
            "maxLength": 80
        },
        "name": {
            "type": "string",
            "minLength": 1,
            "maxLength": 80
        },
        "email": {
            "type": "string",
            "format": "email",
            "minLength": 1,
            "maxLength": 120
        },
        "location": {
            "type": "string",
            "maxLength": 120
        }
    },
    "required": ["name", "email"],
    "additionalProperties": False,
}
