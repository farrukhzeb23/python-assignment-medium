import re


def validate_data(value, data_type):
    if not isinstance(value, str):
        return False

    if data_type.lower() == "integer":
        return validate_integer(value)
    elif data_type.lower() == "float":
        return validate_float(value)
    elif data_type.lower() == "email":
        return validate_email(value)
    else:
        raise ValueError(f"Unsupported data type: {data_type}")


def validate_integer(value):
    try:
        int(value)
        return True
    except ValueError:
        return False


def validate_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


def validate_email(value):
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(email_pattern, value))


print(f"Validating data types")

# Positive test cases
print(validate_data("123", "integer"))
print(validate_data("123.45", "float"))
print(validate_data("test@example.com", "email"))


# Negative test cases
print(validate_data("abc", "integer"))
print(validate_data("abc", "float"))
print(validate_data("invalid.email", "email"))