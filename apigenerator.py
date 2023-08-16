api_keys = {}

def generate_api_key():
    import secrets
    return secrets.token_urlsafe(16)

def generate_new_api_key():
    api_key = generate_api_key()
    api_keys[api_key] = "hello"
    return api_key

def get_hello_message(api_key):
    if api_key in api_keys:
        return api_keys[api_key]
    else:
        return "Invalid API key"
