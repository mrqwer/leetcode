def isPowerOfTwo(n: int) -> bool:
    k = n
    i = 0
    while k:
        i+=1
        k//=2
    return n==2**(i-1)

print(isPowerOfTwo(1024))

"""
def isPowerOfTwo(n: int) -> bool:
    return False if n < 0 else bin(n).count('1') == 1
"""
