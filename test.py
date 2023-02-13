from typing import Optional

class Person:
    name: Optional[str] = None

def some_func(attr: str) -> None:
    print(attr)

test = Person()
#test.name = "Hello"
some_func(test.name)

def say_my_name(a_name) -> str:
    return f"Hello {a_name}"