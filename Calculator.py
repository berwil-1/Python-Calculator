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

# -*- coding: cp1252 -*-
import math
import re

def calc(eq):
    try:
        x = eq.split()
        res = ""

        log = x.count("log")
        for amount in range(log):
            for lenght in range(len(x)):
                if x[lenght] == "log":
                    mem = math.log10(float(x[lenght + 1]))
                    substr = "log " + x[lenght + 1]
                    res = eq.replace(substr, str(mem))
                    eq = res
            x = eq.split()
        
        atan = x.count("atan")
        for amount in range(atan):
            for lenght in range(len(x)):
                if x[lenght] == "atan":
                    mem = math.atan(math.degrees(float(x[lenght + 1])))
                    substr = "atan " + x[lenght + 1]
                    res = eq.replace(substr, str(mem))
                    eq = res
            x = eq.split()
        
        acos = x.count("acos")
        for amount in range(acos):
            for lenght in range(len(x)):
                if x[lenght] == "acos":
                    mem = math.acos(math.degrees(float(x[lenght + 1])))
                    substr = "acos " + x[lenght + 1]
                    res = eq.replace(substr, str(mem))
                    eq = res
            x = eq.split()
        
        asin = x.count("asin")
        for amount in range(asin):
            for lenght in range(len(x)):
                if x[lenght] == "asin":
                    mem = math.asin(math.degrees(float(x[lenght + 1])))
                    substr = "asin " + x[lenght + 1]
                    res = eq.replace(substr, str(mem))
                    eq = res
            x = eq.split()
        
        tan = x.count("tan")
        for amount in range(tan):
            for lenght in range(len(x)):
                if x[lenght] == "tan":
                    mem = math.tan(math.radians(float(x[lenght + 1])))
                    substr = "tan " + x[lenght + 1]
                    res = eq.replace(substr, str(mem))
                    eq = res
            x = eq.split()
        
        cos = x.count("cos")
        for amount in range(cos):
            for lenght in range(len(x)):
                if x[lenght] == "cos":
                    mem = math.cos(math.radians(float(x[lenght + 1])))
                    substr = "cos " + x[lenght + 1]
                    res = eq.replace(substr, str(mem))
                    eq = res
            x = eq.split()
        
        sin = x.count("sin")
        for amount in range(sin):
            for lenght in range(len(x)):
                if x[lenght] == "sin":
                    mem = math.sin(math.radians(float(x[lenght + 1])))
                    substr = "sin " + x[lenght + 1]
                    res = eq.replace(substr, str(mem))
                    eq = res
            x = eq.split()
        
        sqrt = x.count("//")
        for amount in range(sqrt):
            for lenght in range(len(x)):
                if x[lenght] == "//":
                    mem = math.pow(float(x[lenght - 1]), 1 / float(x[lenght + 1]))
                    substr = x[lenght - 1] + " // " + x[lenght + 1]
                    res = eq.replace(substr, str(mem))
                    eq = res
            x = eq.split()
        
        sqr = x.count("^")
        for amount in range(sqr):
            for lenght in range(len(x)):
                if x[lenght] == "^":
                    mem = math.pow(float(x[lenght - 1]), float(x[lenght + 1]))
                    substr = x[lenght - 1] + " ^ " + x[lenght + 1]
                    res = eq.replace(substr, str(mem))
                    eq = res
            x = eq.split()
        
        div = x.count("/")
        for amount in range(div):
            for lenght in range(len(x)):
                if x[lenght] == "/":
                    mem = float(x[lenght - 1]) / float(x[lenght + 1])
                    substr = x[lenght - 1] + " / " + x[lenght + 1]
                    res = eq.replace(substr, str(mem))
                    eq = res
            x = eq.split()

        mul = x.count("*")
        for amount in range(mul):
            for lenght in range(len(x)):
                if x[lenght] == "*":
                    mem = float(x[lenght - 1]) * float(x[lenght + 1])
                    substr = x[lenght - 1] + " * " + x[lenght + 1]
                    res = eq.replace(substr, str(mem))
                    eq = res
            x = eq.split()
        
        sub = x.count("-")
        for amount in range(sub):
            for lenght in range(len(x)):
                if x[lenght] == "-":
                    mem = float(x[lenght - 1]) - float(x[lenght + 1])
                    substr = x[lenght - 1] + " - " + x[lenght + 1]
                    res = eq.replace(substr, str(mem))
                    eq = res
            x = eq.split()

        add = x.count("+")
        for amount in range(add):
            for lenght in range(len(x)):
                if x[lenght] == "+":
                    mem = float(x[lenght - 1]) + float(x[lenght + 1])
                    substr = x[lenght - 1] + " + " + x[lenght + 1]
                    res = eq.replace(substr, str(mem))
                    eq = res
            x = eq.split()

        com = x.count("==")
        for amount in range(com):
            for lenght in range(len(x)):
                if x[lenght] == "==":
                    mem = (float(x[lenght - 1]) == float(x[lenght + 1]))
                    substr = x[lenght - 1] + " == " + x[lenght + 1]
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
        break;

    if(str(numin).lower() == "help".lower()): 
        print("Num + Num2   -   Addition")
        print("Num - Num2   -   Subtraction")
        print("Num * Num2   -   Multiplication")
        print("Num / Num2   -   Division")
        print("Num ^ Num2   -   Square")
        print("Num // Num2  -   Square root")
        print("sin(Num)     -   Sine")
        print("cos(Num)     -   Cosine")
        print("tan(Num)     -   Tangent")
        print("asin(Num)    -   Arcsine")
        print("acos(Num)    -   Arccosine")
        print("atan(Num)    -   Arctangent")
        print("log(Num)     -   Logarithm")
        continue
        
    numin = numin.replace("sin(", "sin (")
    numin = numin.replace("cos(", "cos (")
    numin = numin.replace("tan(", "tan (")
    numin = numin.replace("asin(", "asin (")
    numin = numin.replace("acos(", "acos (")
    numin = numin.replace("atan(", "atan (")
    numin = numin.replace("log(", "log (")
    numin = numin.replace("Pi", "3.14159265358979323846264338327950288419716939937")

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
