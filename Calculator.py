#
# Copyright 2019 CoolJWB
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import math
import re
def calc(eq):
    try:
        x = eq.split()
        res = ""

        rad = x.count("rad")
        for amount in range(rad):
            for length in range(len(x)):
                if x[length] == "rad":
                    mem = math.radians(float(x[length + 1]))
                    substr = "rad " + x[length + 1]
                    res = eq.replace(substr, str(mem))
                    eq = res
            x = eq.split()

        deg = x.count("deg")
        for amount in range(deg):
            for length in range(len(x)):
                if x[length] == "deg":
                    mem = math.degrees(float(x[length + 1]))
                    substr = "deg " + x[length + 1]
                    res = eq.replace(substr, str(mem))
                    eq = res
            x = eq.split()

        ln = x.count("ln")
        for amount in range(ln):
            for length in range(len(x)):
                if x[length] == "ln":
                    mem = math.log(float(x[length + 1]))
                    substr = "ln " + x[length + 1]
                    res = eq.replace(substr, str(mem))
                    eq = res
            x = eq.split()
            
        log = x.count("log")
        for amount in range(log):
            for length in range(len(x)):
                if x[length] == "log":
                    mem = math.log10(float(x[length + 1]))
                    substr = "log " + x[length + 1]
                    res = eq.replace(substr, str(mem))
                    eq = res
            x = eq.split()
        
        atan = x.count("atan")
        for amount in range(atan):
            for length in range(len(x)):
                if x[length] == "atan":
                    mem = math.atan(float(x[length + 1]))
                    substr = "atan " + x[length + 1]
                    res = eq.replace(substr, str(mem))
                    eq = res
            x = eq.split()
        
        acos = x.count("acos")
        for amount in range(acos):
            for length in range(len(x)):
                if x[length] == "acos":
                    mem = math.acos(float(x[length + 1]))
                    substr = "acos " + x[length + 1]
                    res = eq.replace(substr, str(mem))
                    eq = res
            x = eq.split()
        
        asin = x.count("asin")
        for amount in range(asin):
            for length in range(len(x)):
                if x[length] == "asin":
                    mem = math.asin(float(x[length + 1]))
                    substr = "asin " + x[length + 1]
                    res = eq.replace(substr, str(mem))
                    eq = res
            x = eq.split()
        
        tan = x.count("tan")
        for amount in range(tan):
            for length in range(len(x)):
                if x[length] == "tan":
                    mem = math.tan(math.radians(float(x[length + 1])))
                    substr = "tan " + x[length + 1]
                    res = eq.replace(substr, str(mem))
                    eq = res
            x = eq.split()
        
        cos = x.count("cos")
        for amount in range(cos):
            for length in range(len(x)):
                if x[length] == "cos":
                    mem = math.cos(math.radians(float(x[length + 1])))
                    substr = "cos " + x[length + 1]
                    res = eq.replace(substr, str(mem))
                    eq = res
            x = eq.split()
        
        sin = x.count("sin")
        for amount in range(sin):
            for length in range(len(x)):
                if x[length] == "sin":
                    mem = math.sin(math.radians(float(x[length + 1])))
                    substr = "sin " + x[length + 1]
                    res = eq.replace(substr, str(mem))
                    eq = res
            x = eq.split()
        
        ntr = x.count("//")
        for amount in range(ntr):
            for length in range(len(x)):
                if x[length] == "//":
                    mem = math.pow(float(x[length - 1]), 1 / float(x[length + 1]))
                    substr = x[length - 1] + " // " + x[length + 1]
                    res = eq.replace(substr, str(mem))
                    eq = res
            x = eq.split()
        
        pwr = x.count("**")
        for amount in range(pwr):
            for length in range(len(x)):
                if x[length] == "**":
                    mem = float(x[length - 1]) ** float(x[length + 1])
                    substr = x[length - 1] + " ** " + x[length + 1]
                    res = eq.replace(substr, str(mem))
                    eq = res
            x = eq.split()
        
        div = x.count("/")
        for amount in range(div):
            for length in range(len(x)):
                if x[length] == "/":
                    mem = float(x[length - 1]) / float(x[length + 1])
                    substr = x[length - 1] + " / " + x[length + 1]
                    res = eq.replace(substr, str(mem))
                    eq = res
            x = eq.split()

        mul = x.count("*")
        for amount in range(mul):
            for length in range(len(x)):
                if x[length] == "*":
                    mem = float(x[length - 1]) * float(x[length + 1])
                    substr = x[length - 1] + " * " + x[length + 1]
                    res = eq.replace(substr, str(mem))
                    eq = res
            x = eq.split()
        
        sub = x.count("-")
        for amount in range(sub):
            for length in range(len(x)):
                if x[length] == "-":
                    mem = float(x[length - 1]) - float(x[length + 1])
                    substr = x[length - 1] + " - " + x[length + 1]
                    res = eq.replace(substr, str(mem))
                    eq = res
            x = eq.split()

        add = x.count("+")
        for amount in range(add):
            for length in range(len(x)):
                if x[length] == "+":
                    mem = float(x[length - 1]) + float(x[length + 1])
                    substr = x[length - 1] + " + " + x[length + 1]
                    res = eq.replace(substr, str(mem))
                    eq = res
            x = eq.split()

        com = x.count("==")
        for amount in range(com):
            for length in range(len(x)):
                if x[length] == "==":
                    mem = (float(x[length - 1]) == float(x[length + 1]))
                    substr = x[length - 1] + " == " + x[length + 1]
                    res = eq.replace(substr, str(mem))
                    eq = res
            x = eq.split()

        lar = x.count(">")
        for amount in range(lar):
            for length in range(len(x)):
                if x[length] == ">":
                    mem = (float(x[length - 1]) > float(x[length + 1]))
                    substr = x[length - 1] + " > " + x[length + 1]
                    res = eq.replace(substr, str(mem))
                    eq = res
            x = eq.split()

        les = x.count("<")
        for amount in range(les):
            for length in range(len(x)):
                if x[length] == "<":
                    mem = (float(x[length - 1]) < float(x[length + 1]))
                    substr = x[length - 1] + " < " + x[length + 1]
                    res = eq.replace(substr, str(mem))
                    eq = res
            x = eq.split()
            
        return eq
    except IndexError:
        print("Error: Incorrect numin.")
    except ValueError:
        print("Error: Incorrect numbers.")

exit = 0
while exit == 0:
    numin = input("> ")
    raw = ""
    subStr = ""

    if(str(numin).lower() == "exit".lower()):
        exit = 1
        break

    if(str(numin).lower() == "help".lower()):
        print("Mathematical: ")
        print("Num + Num2   -   Addition")
        print("Num - Num2   -   Subtraction")
        print("Num * Num2   -   Multiplication")
        print("Num / Num2   -   Division")
        print("Num ** Num2   -  Power")
        print("Num // Num2  -   Nth Root")
        print("sin(Num)     -   Sine")
        print("cos(Num)     -   Cosine")
        print("tan(Num)     -   Tangent")
        print("asin(Num)    -   Arcsine")
        print("acos(Num)    -   Arccosine")
        print("atan(Num)    -   Arctangent")
        print("log(Num)     -   Logarithm")
        print("deg(Num)     -   Degrees")
        print("\nLogical: ")
        print("Num == Num2  -   Equals")
        print("Num > Num2   -   Larger")
        print("Num < Num2   -   Less")
        continue
        
    numin = numin.replace("sin(", "sin (")
    numin = numin.replace("cos(", "cos (")
    numin = numin.replace("tan(", "tan (")
    numin = numin.replace("asin(", "asin (")
    numin = numin.replace("acos(", "acos (")
    numin = numin.replace("atan(", "atan (")
    numin = numin.replace("log(", "log (")
    numin = numin.replace("ln(", "ln (")
    numin = numin.replace("deg(", "deg (")
    numin = numin.replace("rad(", "rad (")
    numin = numin.replace("Pi", "3.14159265358979323846264338327950288419716939937")
    numin = numin.replace("e", "2.71828182845904523536028747135266249775724709369995")

    parenthesis = numin.count("(")
    for a in range(parenthesis):
        if not ((numin.rfind("(") - 1) < 0) and str(numin[numin.rfind("(") - 1]).isdigit():
            substr = numin[(numin.rfind("(") + 1):numin.find(")")]
            numin = numin.replace("(" + substr + ")", " * " + str(calc(substr)))
        else:    
            substr = numin[(numin.rfind("(") + 1):numin.find(")")]
            numin = numin.replace("(" + substr + ")", str(calc(substr)))         
    numin = calc(numin)
    print("Answer: " + str(numin))
