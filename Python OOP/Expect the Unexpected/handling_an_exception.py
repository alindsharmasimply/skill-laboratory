def handler() -> None:
    try:
        raise Exception("Will always be raised")
    except Exception as e:
        print(f"I caught an exception {e}")
    print("Executed after the exception")


handler()


def funny_division(x: int) -> str | float:
    try:
        if x == 13:
            raise ValueError()
        return 100 / x
    except ZeroDivisionError:
        return "Zero is not a good idea"
    except TypeError:
        return "Only integers are allowed"
    except ValueError:
        return "Not 13"


# for value in [0, "Rahul", 50]:
#     funny_division(value)
