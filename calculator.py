import math
import numpy
import re as regex

sanetize = lambda a : float(a)
functions = {
    # Programming functions
    'abs': lambda a : abs(sanetize(a)),
    'floor': lambda a : math.floor(sanetize(a)),
    'ceil': lambda a : math.ceil(sanetize(a)),
    'round': lambda a : math.floor(sanetize(a) + 0.5),
    
    # Logarithmic functions
    'log': lambda a : math.log10(sanetize(a)),
    'ln': lambda a : math.log(sanetize(a)),
    'exp': lambda a : math.exp(sanetize(a)),

    # Trigonometric functions
    'rad': lambda a : math.radians(sanetize(a)),
    'deg': lambda a : math.degrees(sanetize(a)),
    'sin': lambda a : math.sin(sanetize(a)),
    'asin': lambda a : math.asin(sanetize(a)),
    'cos': lambda a : math.cos(sanetize(a)),
    'acos': lambda a : math.acos(sanetize(a)),
    'tan': lambda a : math.tan(sanetize(a)),
    'atan': lambda a : math.atan(sanetize(a))
}

symbols = {
    '%': lambda a, b : sanetize(a) % sanetize(b),
    '\\': lambda a, b : sanetize(a) ** (1.0 / sanetize(b)),
    '^': lambda a, b : sanetize(a) ** sanetize(b),
    '/': lambda a, b : sanetize(a) / sanetize(b),
    '*': lambda a, b : sanetize(a) * sanetize(b),
    '-': lambda a, b : sanetize(a) - sanetize(b),
    '+': lambda a, b : sanetize(a) + sanetize(b),
    '=': lambda a, b : 1 if sanetize(a) == sanetize(b) else 0,
    '!': lambda a, b : 0 if sanetize(a) == sanetize(b) else 1,
    '<': lambda a, b : 1 if sanetize(a) < sanetize(b) else 0,
    '>': lambda a, b : 1 if sanetize(a) > sanetize(b) else 0
}

def format(text):
    return regex.findall(
        # Locate a number or
        "((?<![0-9])[-]?[0-9]*[.]?[0-9]+|" +

        # a symbol or,
        "[><!=+\-*/^\\\\%]|" +

        # a function.
        "[a-z]+)"
    , text)

def calc(text):
    split = format(text)
    array = numpy.array(split)

    # Iterate over functions available.
    for function in functions:
        count = split.count(function)
        for _ in range(count):
            # Find all function indices.
            indices = numpy.where(array == function)[0]

            for index in indices:
                    result = functions[function](split[index + 1])
                    text = text.replace(function + " " + split[index + 1], str(result)).replace(function + split[index + 1], str(result))
            split = format(text)
            array = numpy.array(split)

    # Iterate over symbols available.
    for symbol in symbols:
        count = split.count(symbol)
        for _ in range(count):
            # Find all symbol indices.
            indices = numpy.where(array == symbol)[0]

            for index in indices:
                result = symbols[symbol](split[index - 1], split[index + 1])
                text = text.replace(split[index - 1] + " " + symbol + " " + split[index + 1], str(result)).replace(split[index - 1] + symbol + split[index + 1], str(result))
            split = format(text)
            array = numpy.array(split)

    return text

def main():
    while True:
        text = "".join(input(">> ").split())
        if text.upper() == "EXIT": break

        for _ in range(text.count("(")):
            start = text.rfind("(") + 1
            result = text[start:text.find(")", start)]
            text = text.replace("(" + result + ")", ("*" if text[start - 2].isdigit() else "") + str(calc(result)))
        print(calc(text))

if __name__ == "__main__":
    main()
