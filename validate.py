def validate_int(i):
    if isinstance(i, int) and 1 <= i <= 20:
        return True
    return False


def validate_str(s):
    if isinstance(s, str) and len(s) > 0 and len(s) < 100:
        return True
    return False


def validate_float(f):
    if isinstance(f, float) and 1.0 <= f <= 100.0:
        return True
    return False


def validate_bool(b):
    if isinstance(b, bool) and b in [True, False]:
        return True
    return False


validators = {
    "i": validate_int,
    "f": validate_float,
    "s": validate_str,
    "b": validate_bool
}


def validate(d, rules):
    for k, v in d.items():
        # if not rules.get(k, lambda x: False)(v):
        #     return False
        # print(k, v)
        if isinstance(v, str):
            if not validators["s"](v):
                return False
        elif isinstance(v, float):
            if not validators["f"](v):
                return False
        elif isinstance(v, bool):
            if not validators["b"](v):
                return False
        elif isinstance(v, int):
            if not validators["i"](v):
                return False
    return True

# def validate_args(func):
#     def wrapper(*args, **kwargs):
#         for k,v in kwargs.items():
#             res = validators.get(k, lambda x: x)(v)
#             return res
#     return wrapper

# @validate_args
# def func1(d):
#     print("func1 called")


d1 = {"s": "some_string",
      "i": 12,
      "f": 83.0,
      "a": 9,
      "b": False,
      'x1': 'x1',
      }

print(validate(d1, validators))
