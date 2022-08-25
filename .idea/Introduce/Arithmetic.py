# The provided code stub reads two integers from STDIN,  and . Add code to print three lines where:
#
# The first line contains the sum of the two numbers.
# The second line contains the difference of the two numbers (first - second).
# The third line contains the product of the two numbers.

if __name__ == '__main__':
    print('Input number for a:')
    a = int(input())
    print('Input number for b:')
    b = int(input())

    total = a + b
    diff = a - b
    multi = a * b

    print(total)
    print(diff)
    print(multi)