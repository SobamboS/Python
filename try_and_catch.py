def add(a: float, b: float) -> float | None:
    try:
        return a/b
    except ZeroDivisionError:
        print("Can't divide with zero")
        return None
    except TypeError:
        print("")
print(add(1, 0))
