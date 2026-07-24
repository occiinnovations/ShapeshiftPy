import numpy
import matplotlib.pyplot as plt

# Shape selection
shape = input(
    "Welcome to WatchCat! Please select a shape to draw (R for rectangle, C for circle, S for square, P for pentagon): ")

if shape == "R" or shape == "C" or shape == "S" or shape == "P":
    print("You have selected a valid shape.")
else:
    print("Invalid shape selection. Please choose R, C, S, or P.")
    exit()

# Rectangle
if shape == "R":
    x1 = float(
        input("Enter the x-coordinate of the rectangle's bottom-left corner:"))
    y1 = float(
        input("Enter the y-coordinate of the rectangle's bottom-left corner: "))

    width = float(
        input("Enter the width of the rectangle: "))
    height = float(
        input("Enter the height of the rectangle. It cannot be equal to the width: "))

    if height == width:
        print("The height cannot be equal to the width. Please enter a valid height. Infinite possibilities and you choose the single one that makes it a square.")
        exit()

    back_corner_x = (x1 + width)
    back_corner_y = (y1 + height)
    bottom_right_x = (x1 + width)

    rectangle = [(x1, y1), (back_corner_x, back_corner_y),
                 (x1, back_corner_y), (bottom_right_x, y1)]

    plt.plot(rectangle)

    plt.xlim(0, 20)
    plt.ylim(0, 20)

    plt.show()

# Circle
if shape == "C":
    x = float(input("Enter a value for x: "))
    y = float(input("Enter a value for y: "))
    r = float(input("Enter a value for r: "))
    h = float(input("Enter a value for h: "))
    k = float(input("Enter a value for k: "))

    circle = [(x-h)**2 + (y-k)**2 - r**2]

    plt.plot(circle)

# Square
if shape == "S":
    print("You have selected a square. Please enter the coordinates of the bottom-left corner and the side length.")

    x = float(input("Enter the x-coordinate of the square's bottom-left corner: "))
    y = float(input("Enter the y-coordinate of the square's bottom-left corner: "))
    side_length = float(
        input("Enter the side length of the square. A square's width and length are equal: "))

    square = [(x, y), (x + side_length, y), (x + side_length,
                                             y + side_length), (x, y + side_length)]

    plt.plot(square)

# Pentagon
if shape == "P":
    print("You have selected a pentagon. Please enter the coordinates of the five corners in order.")
    x1 = float(input("Enter the x-coordinate of the first corner: "))
    x2 = float(input("Enter the x-coordinate of the second corner: "))
    x3 = float(input("Enter the x-coordinate of the third corner: "))
    x4 = float(input("Enter the x-coordinate of the fourth corner: "))
    x5 = x1
    y1 = float(input("Enter the y-coordinate of the first corner: "))
    y2 = float(input("Enter the y-coordinate of the second corner: "))
    y3 = float(input("Enter the y-coordinate of the third corner: "))
    y4 = float(input("Enter the y-coordinate of the fourth corner: "))
    y5 = y1

    x = [x1, x2, x3, x4, x5]
    y = [y1, y2, y3, y4, y5]

    plt.plot(x, y, marker='o')

    plt.xlim(0, 20)
    plt.ylim(0, 20)

    plt.show()
