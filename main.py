import turtle as t
global scr, pen


def init():
    global scr, pen
    t.title("Circle Of Squares")
    t.bgcolor("green")
    scr = t.getscreen()
    pen = t.Turtle()
    pen.speed(float(3.5))
    pen.pensize(float(2.5))


def main():
    init()
    shape = int(input("What shape would you like to draw?\n"
                      "[1. Square][2. Triangle][3. Circle]\n"
                      "[4. Circle Of Squares][5. Circle Of Triangles][6. Circle Of Circles]\n"
                      "[9. Exit] > "))
    try:
        if shape == 1:
            square(50)
            clear_screen = int(input("Would you like to clear the screen? [1. Yes][2. No] > "))
            if clear_screen == 1:
                clear()
            else:
                pass
            main()
        elif shape == 2:
            triangle(50)
            clear_screen = int(input("Would you like to clear the screen? [1. Yes][2. No] > "))
            if clear_screen == 1:
                clear()
            else:
                pass
            main()
        elif shape == 3:
            circle(50)
            clear_screen = int(input("Would you like to clear the screen? [1. Yes][2. No] > "))
            if clear_screen == 1:
                clear()
            else:
                pass
            main()
        elif shape == 4:
            circle_sqr(24, 50)
            clear_screen = int(input("Would you like to clear the screen? [1. Yes][2. No] > "))
            if clear_screen == 1:
                clear()
            else:
                pass
            main()
        elif shape == 5:
            circle_tri(24, 50)
            clear_screen = int(input("Would you like to clear the screen? [1. Yes][2. No] > "))
            if clear_screen == 1:
                clear()
            else:
                pass
            main()
        elif shape == 6:
            circle_circle(24, 25)
            clear_screen = int(input("Would you like to clear the screen? [1. Yes][2. No] > "))
            if clear_screen == 1:
                clear()
            else:
                pass
            main()
        elif shape == 9:
            quit()
        else:
            print(f"{shape} was not an option. Please Try Again.")
            main()
    except ValueError as err:
        print(err)
        print("Enter a whole number. 1 or 2")
        main()


def clear():
    t.clearscreen()


def square(size):
    pen.lt(90)
    for i in range(4):
        pen.fd(size)
        pen.rt(90)


def triangle(size):
    pen.lt(60)
    for i in range(3):
        pen.rt(120)
        pen.fd(size)


def circle(size):
    t.circle(size)


def circle_sqr(num, size):
    pen.lt(90)
    for n in range(num):
        for i in range(4):
            pen.rt(90)
            pen.fd(size)
        pen.rt(15)
        pen.bk(size)
    pen.lt(15)


def circle_tri(num, size):
    pen.lt(60)
    for n in range(num):
        for i in range(3):
            pen.rt(120)
            pen.fd(size)
        pen.rt(15)
        pen.bk(size)
    pen.lt(15)


def circle_circle(num, size):
    pen.lt(90)
    for n in range(num):
        pen.circle(size)
        pen.rt(15)
        pen.bk(size)
    pen.lt(15)


if __name__ == '__main__':
    main()


