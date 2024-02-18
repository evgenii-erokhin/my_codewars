# Implement a function that accepts 3 integer values a, b, c. The function should return true if a triangle can be built with the sides of given length and false in any other case.
#
# (In this case, all triangles must have surface greater than 0 to be accepted).
#
# Examples:
#
# Input -> Output
# 1,2,2 -> true
# 4,2,3 -> true
# 2,2,2 -> true
# 1,2,3 -> false
# -5,1,3 -> false
# 0,2,3 -> false
# 1,2,9 -> false

def is_triangle(a: int, b: int, c: int) -> bool:
    """Determine if three sides of given lengths can form a triangle.

        Args:
            a (int): First side length
            b (int): Second side length
            c (int): Third side lenght

        Returns:
            bool: True if the three sides given can form a triangle.
    """
    return True if a + b > c and a + c > b and b + c > a else False


if __name__ == '__main__':
    print(is_triangle(1, 2, 2))  # -> True
