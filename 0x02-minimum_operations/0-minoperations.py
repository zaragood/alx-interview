#!/usr/bin/python3
"""Minimum Operations
Algorithm
"""

def minOperations(n):
    """
    Calculates the fewest number of operations needed to result in exactly n H characters in the file.

    Args:
        n (int): The target number of H characters.

    Returns:
        int: The fewest number of operations needed to reach n H characters. If n is impossible to achieve, returns 0.
    """
    if n <= 1:
        return 0
    
    operations = 0
    factor = 2
    
    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1
    
    return operations
