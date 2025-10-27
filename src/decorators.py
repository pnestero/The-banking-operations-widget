from functools import wraps
from typing import Any, Callable


def log(filename: str | None = None) -> Callable:
    """Декоратор для записи результата в консоль или в указанный файл, если таковой задан"""

    def my_decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
                if filename is None:
                    print(f"{func.__name__} ok")
                else:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(f"{func.__name__} ok\n")
                return result
            except Exception as e:
                if filename is None:
                    print(f"{func.__name__} error: {e.__class__.__name__}: {e}. Inputs: {args}, {kwargs}")
                else:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(f"{func.__name__} error: {str(e)}. Inputs: {args}, {kwargs}\n")
                raise

        return wrapper

    return my_decorator
