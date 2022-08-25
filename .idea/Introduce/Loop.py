# The provided code stub reads and integer, , from STDIN. For all non-negative integers , print i2.

if __name__ == '__main__':
    print('Input number to loop: ')
    n = int(input())

    for i in range (0, 20):
        if i < n:
            print(i*i)
            i = i+1
        else:
            i = i+1