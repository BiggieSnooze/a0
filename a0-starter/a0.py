# a0.py

# Starter code for assignment 0 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Andrew Huynh
# huynha15@uci.edu
# 16106034

n = int(input())
corner = "+"
middle = "-"
wall = "|"
space = " "
front = "  "

i = 0

for i in range(0, n + 1):
    if n > 1 and i == 1:
        print(f"{corner}{middle}{corner}")
        print(f"{wall}{space}{wall}")
        print(f"{corner}{middle}{corner}{middle}{corner}")
    elif n == 1 and i == 1:
        print(f"{corner}{middle}{corner}")
        print(f"{wall}{space}{wall}")
        print(f"{corner}{middle}{corner}")
    elif n > 1 and i == n:
        print(f"{front * (i - 1)}{wall}{space}{wall}")
        print(f"{front * (i - 1)}{corner}{middle}{corner}")
    elif  n > 1 and i != (n + 1) and i != 0:
        print(f"{front * (i - 1)}{wall}{space}{wall}")
        print(f"{front * (i - 1)}{corner}{middle}{corner}{middle}{corner}")
    
    i += 1
