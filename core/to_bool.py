

def _to_bool(value: int | bool | None) -> bool | None:
    if value is None:
        return None
    return bool(value)