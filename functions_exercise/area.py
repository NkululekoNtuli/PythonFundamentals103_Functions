import math
"""
    Calculate the area of a rectangle.

    Args:
        length (float): The length of the rectangle.
        width (float): The width of the rectangle.

    Returns:
        float: The area of the rectangle, which is the product of its length and width.

    Example:
        To calculate the area of a rectangle with a length of 5 units and a width of 3 units:
        >>> rectangle_area(5, 3)
"""
def area_rect(lenth, width):
    area = lenth * width
    return(area)


"""
    Calculate the area of a circle.

    Args:
        radius (float): The radius of the circle.

    Returns:
        float: The area of the circle, which is calculated as pi times the square of the radius.

    Example:
        To calculate the area of a circle with a radius of 4 units:
        >>> circle_area(4)
        50.26548245743669
"""
def area_circ(radius):
    area = math.pi * radius ** 2
    return(area)