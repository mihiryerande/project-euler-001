# Problem 1:
#     Multiples of 3 or 5
#
# Description:
#     If we list all the natural numbers below 10
#       that are multiples of 3 or 5,
#       we get 3, 5, 6 and 9.
#     The sum of these multiples is 23.
#     
#     Find the sum of all the multiples of 3 or 5 below 1000.

def mult_sum(n: int, x: int) -> int:
    """
    Returns the sum of all multiples of x which are less than n.

    Args:
        n (int): Natural number
        x (int): Natural number

    Returns:
        (int): Sum of all natural numbers less than n which are multiples of x

    Raises:
        AssertError: if incorrect params are given
    """
    assert type(n) == int and n > 0  # `n` is a natural number
    assert type(x) == int and x > 0  # `x` is a natural number

    nx = (n - 1) // x
    return int(x * (nx * (nx + 1) / 2))


def main(n: int) -> int:
    """
    Returns the sum of all natural numbers less than n which are multiples of 3 or 5.

    Args:
        n (int): Natural number

    Returns:
        (int): Sum of all natural numbers less than n which are multiples of 3 or 5

    Raises:
        AssertError: if incorrect params are given
    """
    assert type(n) == int and n > 0

    # Calculate sum of multiples of 3
    s3 = mult_sum(n, 3)

    # Calculate sum of multiples of 5
    s5 = mult_sum(n, 5)

    # Calculate sum of multiples of 15
    s15 = mult_sum(n, 15)

    # Use inclusion-exclusion to get final sum
    return s3 + s5 - s15


if __name__ == '__main__':
    num = int(input('Enter a natural number: '))
    ans = main(num)
    print('Sum of multiples of 3 and 5 below {}:\n{}'.format(num, ans))
