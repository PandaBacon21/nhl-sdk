


# Test cases to cover:

# Happy path
    # 200 OK + JSON body → {success: True, data: ...} (and whatever else you standardize: status_code, error, meta, etc.)


# Non-200 responses
    # 404/500 → {success: False, error: ...} and no crashes

# Timeouts / connection errors
    # requests exceptions → {success: False, error: ...} and includes something helpful (message, exception_type)

# Non-JSON response
    # HTML or empty body → {success: False, error: ...} (or data = raw text, whichever you chose—just be consistent)

# Rate limiting / retry behavior (if you have it)
    # 429 with Retry-After handling (even if you don’t retry yet, ensure you surface it predictably)

# Query params / headers passing
    # If you support params, headers, base_url, etc., verify they’re passed to session.get() correctly

# URL building
# Base + path joining edge cases (/v1 + /players vs v1/players)