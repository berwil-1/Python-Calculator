# Simple Python calculator
## What is this?
This is a tiny calculator with 100 lines of code made to be small, simple and effective.
It started as a discussion between me and a friend that turned into a small Java project but was later remade into Python to work for a school project in 2019.
In 2022 I decided to rework the poorly written code for a smaller and more clean look with better flexibility. It still doesn't have much in terms of functionality but works as a basic calculator should, with features listed below.

## How does it work?
The calculator begins with stepping into the innermost parenthesis and extracting the problem inside.
By then looping over all available functions/symbols and evaluating them step by step it can then replace the result with the problem in the original string.
Doing this iteratively will slowly make the problem easier until the problem exists of basic operators (add, subtract, etc).

## What can it do 👀
**Logic operators (1: true 0: false)**
- a = b : Equal
- a ! b : Not equal
- a < b : Lower
- a > b : Larger

**Basic operators**
- a + b : Addition
- a - b : Subtraction
- a * b : Multiplication
- a / b : Division
- a ^ n : Power of N
- a \ n : Root of N
- a % b : Modulus

**Functions**
- abs(a) : Absolute value, returns value as non-negative
- floor(a) : Round number down
- ceil(a) : Round number up
- round(a) : Round number up/down
- log(a) : Common logarithm in base 10
- ln(a) : Natural logarithm in base e
- exp(n) : Function for e to the power of n
- rad(θ) : Angle in degrees to radians
- deg(θ) : Angle in radians to degrees
- sin(θ) : The sine of angle theta
- cos(θ) : The cosine of angle theta
- tan(θ) : The tangent of angle theta
- asin(θ) : Inverse sine of angle theta
- acos(θ) : Inverse cosine of angle theta
- atan(θ) : Inverse tangent of angle theta

## Can I use it for my own project?
Yes you can use this for commercial use since this is licensed with [Apache License 2.0](https://tldrlegal.com/license/apache-license-2.0-(apache-2.0)).
You can try it out directly here: https://repl.it/@CoolJWB/Python-Calculator
