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

# Main calculator function
def calc(eq):
    try:
        eqSplit = eq.split()
        res = ""

        rad = eqSplit.count("rad")
        for amount in range(rad):
            for length in range(len(eqSplit)):
                if eqSplit[length] == "rad":
                    mem = math.radians(float(eqSplit[length + 1]))
                    substr = "rad " + eqSplit[length + 1]
                    res = eq.replace(substr, str(mem))
                    eq = res
            eqSplit = eq.split()

        deg = eqSplit.count("deg")
        for amount in range(deg):
            for length in range(len(eqSplit)):
                if x[length] == "deg":
                    mem = math.degrees(float(eqSplit[length + 1]))
                    substr = "deg " + eqSplit[length + 1]
                    res = eq.replace(substr, str(mem))
                    eq = res
            eqSplit = eq.split()

        ln = eqSplit.count("ln")
        for amount in range(ln):
            for length in range(len(eqSplit)):
                if eqSplit[length] == "ln":
                    mem = math.log(float(eqSplit[length + 1]))
                    substr = "ln " + eqSplit[length + 1]
                    res = eq.replace(substr, str(mem))
                    eq = res
            eqSplit = eq.split()
            
        log = eqSplit.count("log")
        for amount in range(log):
            for length in range(len(eqSplit)):
                if eqSplit[length] == "log":
                    mem = math.log10(float(eqSplit[length + 1]))
                    substr = "log " + eqSplit[length + 1]
                    res = eq.replace(substr, str(mem))
                    eq = res
            eqSplit = eq.split()
        
        atan = eqSplit.count("atan")
        for amount in range(atan):
            for length in range(len(eqSplit)):
                if x[length] == "atan":
                    mem = math.atan(float(eqSplit[length + 1]))
                    substr = "atan " + eqSplit[length + 1]
                    res = eq.replace(substr, str(mem))
                    eq = res
            eqSplit = eq.split()
        
        acos = eqSplit.count("acos")
        for amount in range(acos):
            for length in range(len(eqSplit)):
                if eqSplit[length] == "acos":
                    mem = math.acos(float(eqSplit[length + 1]))
                    substr = "acos " + eqSplit[length + 1]
                    res = eq.replace(substr, str(mem))
                    eq = res
            eqSplit = eq.split()
        
        asin = eqSplit.count("asin")
        for amount in range(asin):
            for length in range(len(eqSplit)):
                if eqSplit[length] == "asin":
                    mem = math.asin(float(eqSplit[length + 1]))
                    substr = "asin " + eqSplit[length + 1]
                    res = eq.replace(substr, str(mem))
                    eq = res
            eqSplit = eq.split()
        
        tan = eqSplit.count("tan")
        for amount in range(tan):
            for length in range(len(eqSplit)):
                if eqSplit[length] == "tan":
                    mem = math.tan(math.radians(float(eqSplit[length + 1])))
                    substr = "tan " + eqSplit[length + 1]
                    res = eq.replace(substr, str(mem))
                    eq = res
            eqSplit = eq.split()
        
        cos = eqSplit.count("cos")
        for amount in range(cos):
            for length in range(len(eqSplit)):
                if eqSplit[length] == "cos":
                    mem = math.cos(math.radians(float(eqSplit[length + 1])))
                    substr = "cos " + eqSplit[length + 1]
                    res = eq.replace(substr, str(mem))
                    eq = res
            eqSplit = eq.split()
        
        sin = eqSplit.count("sin")
        for amount in range(sin):
            for length in range(len(eqSplit)):
                if eqSplit[length] == "sin":
                    mem = math.sin(math.radians(float(eqSplit[length + 1])))
                    substr = "sin " + eqSplit[length + 1]
                    res = eq.replace(substr, str(mem))
                    eq = res
            eqSplit = eq.split()
        
        ntr = eqSplit.count("//") + eqSplit.count("√")
        for amount in range(ntr):
            for length in range(len(eqSplit)):
                mem = 0
                substr = ""
                if eqSplit[length] == "//":
                    mem = math.pow(float(eqSplit[length - 1]), 1 / float(eqSplit[length + 1]))
                    substr = eqSplit[length - 1] + " // " + eqSplit[length + 1]
                    
                else if eqSplit[length] == "√":
                    mem = math.pow(float(eqSplit[length - 1]), 1 / float(eqSplit[length + 1]))
                    substr = eqSplit[length - 1] + " √ " + eqSplit[length + 1]
                    
            res = eq.replace(substr, str(mem))
            eq = res        
            eqSplit = eq.split()
        
        pwr = eqSplit.count("**")
        for amount in range(pwr):
            for length in range(len(eqSplit)):
                if eqSplit[length] == "**":
                    mem = float(eqSplit[length - 1]) ** float(eqSplit[length + 1])
                    substr = eqSplit[length - 1] + " ** " + eqSplit[length + 1]
                    res = eq.replace(substr, str(mem))
                    eq = res
            eqSplit = eq.split()
        
        div = eqSplit.count("/")
        for amount in range(div):
            for length in range(len(eqSplit)):
                if eqSplit[length] == "/":
                    mem = float(eqSplit[length - 1]) / float(eqSplit[length + 1])
                    substr = eqSplit[length - 1] + " / " + eqSplit[length + 1]
                    res = eq.replace(substr, str(mem))
                    eq = res
            eqSplit = eq.split()

        mul = eqSplit.count("*")
        for amount in range(mul):
            for length in range(len(eqSplit)):
                if eqSplit[length] == "*":
                    mem = float(eqSplit[length - 1]) * float(eqSplit[length + 1])
                    substr = eqSplit[length - 1] + " * " + eqSplit[length + 1]
                    res = eq.replace(substr, str(mem))
                    eq = res
            eqSplit = eq.split()
        
        sub = eqSplit.count("-")
        for amount in range(sub):
            for length in range(len(eqSplit)):
                if eqSplit[length] == "-":
                    mem = float(eqSplit[length - 1]) - float(eqSplit[length + 1])
                    substr = eqSplit[length - 1] + " - " + eqSplit[length + 1]
                    res = eq.replace(substr, str(mem))
                    eq = res
            eqSplit = eq.split()

        add = eqSplit.count("+")
        for amount in range(add):
            for length in range(len(eqSplit)):
                if eqSplit[length] == "+":
                    mem = float(eqSplit[length - 1]) + float(eqSplit[length + 1])
                    substr = eqSplit[length - 1] + " + " + eqSplit[length + 1]
                    res = eq.replace(substr, str(mem))
                    eq = res
            eqSplit = eq.split()

        com = eqSplit.count("==")
        for amount in range(com):
            for length in range(len(eqSplit)):
                if eqSplit[length] == "==":
                    mem = (float(eqSplit[length - 1]) == float(eqSplit[length + 1]))
                    substr = eqSplit[length - 1] + " == " + eqSplit[length + 1]
                    res = eq.replace(substr, str(mem))
                    eq = res
            eqSplit = eq.split()

        lar = eqSplit.count(">")
        for amount in range(lar):
            for length in range(len(eqSplit)):
                if eqSplit[length] == ">":
                    mem = (float(eqSplit[length - 1]) > float(eqSplit[length + 1]))
                    substr = eqSplit[length - 1] + " > " + eqSplit[length + 1]
                    res = eq.replace(substr, str(mem))
                    eq = res
            eqSplit = eq.split()

        les = eqSplit.count("<")
        for amount in range(les):
            for length in range(len(eqSplit)):
                if eqSplit[length] == "<":
                    mem = (float(eqSplit[length - 1]) < float(eqSplit[length + 1]))
                    substr = eqSplit[length - 1] + " < " + eqSplit[length + 1]
                    res = eq.replace(substr, str(mem))
                    eq = res
            eqSplit = eq.split()
            
        return eq
    except IndexError:
        print("Error: Incorrect numin.")
    except ValueError:
        print("Error: Incorrect numbers.")

run = 1
while run == 1:
    numin = input("> ")
    raw = ""
    subStr = ""

    if(str(numin).lower() == "exit".lower()):
        run = 0
        break

    # Show calculator help
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

    # Reformat input    
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

    # Calculate parenthesises
    parenthesis = numin.count("(")
    for a in range(parenthesis):
        if not ((numin.rfind("(") - 1) < 0) and str(numin[numin.rfind("(") - 1]).isdigit():
            substr = numin[(numin.rfind("(") + 1):numin.find(")", numin.rfind("(") - 1)]
            numin = numin.replace("(" + substr + ")", " * " + str(calc(substr)))
        else:    
            substr = numin[(numin.rfind("(") + 1):numin.find(")", numin.rfind("("))]
            numin = numin.replace("(" + substr + ")", str(calc(substr)))         
    numin = calc(numin)
    print("Answer: " + str(numin))
