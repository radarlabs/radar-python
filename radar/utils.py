def obj_to_dict(obj):
    """Recursively convert object instance to dictionary"""
    SKIP_KEYS = ["_requester", "_radar", "raw_json"]
    if type(obj) is dict:
        res = {}
        for k, v in obj.items():
            if k in SKIP_KEYS:
                continue
            res[k] = obj_to_dict(v)
        return res
    elif type(obj) is list:
        return [obj_to_dict(item) for item in obj]
    elif hasattr(obj, "__dict__"):
        return obj_to_dict(vars(obj))
    else:
        return obj


def remove_none_values(data={}):
    """Returns dictionary with None values removed"""
    return {k: v for k, v in data.items() if v is not None}
