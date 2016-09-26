#!/usr/bin/env python
print("(+)     Your ideal weight!!!!!")
height = float(raw_input("Enter your height: "))
if height != 0:
    print("(+)  ok ")
    weight = (72.7 * height) - 58
    print("You ideal weight: %r") % (weight)
