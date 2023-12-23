#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def tag_decorator(tag):
    def decorator(func):
        def wrapper(string):
            result = func(string)
            return f"<{tag}>{result}</{tag}>"

        return wrapper

    return decorator


@tag_decorator(tag="div")
def lowercase(string):
    return string.lower()


if __name__ == '__main__':
    result = lowercase(input("Введите строку: "))
    print(result)



