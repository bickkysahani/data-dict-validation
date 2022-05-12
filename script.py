


def validate(d, rules):
    for k, v in d.items():
        if not rules.get(k, lambda x: False)(v):
            return False
    return True

#rules for validation
validations = {
    "A": lambda x: isinstance(x, str) and len(x) > 0 and len(x) < 100,
    "B": lambda x: isinstance(x, int) and 1 <= x <= 20,
    "C": lambda x: isinstance(x, float) and 1.0 <= x <= 100.0,
    "D": lambda x: isinstance(x, bool) and x in [True, False]
}


d1 = {"A":"some_string",
     "B":12,
     "C":83.0,
     "D":False,
     }

print(validate(d1, validations))
