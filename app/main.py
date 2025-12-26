from typing import Callable


def cache(func: Callable) -> Callable:
    def wrapper(*args):
        if args in wrapper.cache_dict:
            print("Getting from cache")
            return wrapper.cache_dict[args]
        else:
            print("Calculating new result")
            result = func(*args)
            wrapper.cache_dict[args] = result
            return result

    wrapper.cache_dict = {}
    return wrapper
