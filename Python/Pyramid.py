while True:
    z = int(input("Y: "))

    if 0 <= z <= 20:
        break

for x in range(z):

    print("-" * (z-x) + "*" * x + " " * x + "-" * (z-x))



# while True:
#     s = int(input("Y: "))
#     if (s >= 0 and s <= 12):
#         break

# for i in range(1, s, 1):

#     print("_" * (s - i), end="")
#     print("*" * (i), end="")
#     print(" " * (i), end="")
#     print("_" * (s - i), end="")
#     print("")
