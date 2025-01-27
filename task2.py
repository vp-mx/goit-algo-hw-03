import turtle
from typing import Any


def koch_curve(t: turtle.Turtle, order: int, size: float) -> None:
    """
    Recursively draws a Koch curve.

    :param: t (turtle.Turtle): The turtle object used for drawing.
    :param: order (int): The recursion level.
    :param: size (float): The length of the curve.
    """
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size / 3)
            t.left(angle)


def koch_snowflake(t: turtle.Turtle, order: int, size: float) -> None:
    """
    Draws a Koch snowflake by combining three Koch curves.

    :param: t (turtle.Turtle): The turtle object used for drawing.
    :param: order (int): The recursion level.
    :param: size (float): The length of each side of the snowflake.
    """
    for _ in range(3):
        koch_curve(t, order, size)
        t.right(120)


def draw_koch_snowflake(order: int, size: float = 300) -> None:
    """
    Sets up the turtle graphics window and initiates the drawing of the Koch snowflake.

    :param: order (int): The recursion level.
    :param: size (float, optional): The length of each side of the snowflake. Defaults to 300.
    """
    window: Any = turtle.Screen()
    window.bgcolor("white")

    t: turtle.Turtle = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-size / 2, size / 3)
    t.pendown()

    koch_snowflake(t, order, size)
    window.mainloop()


if __name__ == "__main__":
    try:
        order: int = int(input("Enter the recursion level for the Koch snowflake: "))
        draw_koch_snowflake(order)
    except ValueError:
        print("Invalid input. Please enter a valid integer for the recursion level.")
