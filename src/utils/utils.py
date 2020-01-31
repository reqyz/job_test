def gentle_convert(val, to_type: type):
    if not isinstance(val, to_type):
        try:
            return to_type(val)
        except Exception:
            pass
    return val
