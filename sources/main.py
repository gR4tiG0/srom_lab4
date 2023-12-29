#!/usr/bin/python3 
from compmath.gf import *
from random import getrandbits

def main() -> None:
    fld = GF()
    BITS = fld.m 
    print(len(bin(fld.matrix.getBase())[2:]))
    # A,B = getrandbits(BITS),getrandbits(BITS)
    A = 0x2a2d878f41e5c99f64fb7d2497aee5e0d2bc49e98d9abcb08c9599879c12a7e1f330a43b4594f270ef21b4f966c09e5acd06ee8a3
    B = 0x6df2d5505147c6aa31013f32bab48a91f8203f87c0d29f0fda3951f0bc26c73c7b8b81f8e54426219a31d098b7b85447c56afd486
    # A,B = 1,2
    # A,B = int('011',2),int('101',2)
    a,b = fld(A),fld(B)
    print(a,b)
    # print(bin(A)[2:].zfill(3),bin(B)[2:].zfill(3))
    # print(a)
    # print(bin(A)[2:])
    c = a+ b 
    print("a+b",c)
    c = a**2
    print("a**2",c)
    # matrix = bin(fld.matrix.getBase())[2:]
    # for i in range(len(matrix),-1,-fld.m):
        # print(matrix[i-fld.m:i][::-1])

    c = a*b
    print("a*b =",bin(c.getBase())[2:].zfill(fld.m))
    # matrix = bin(getMatrix(3).getBase())[2:]
    # for i in range(len(matrix),-1,-3):
        # print(matrix[i-3:i][::-1])

 # print(bin(matrix.getBase())[2:])
    # print(bin(c.getBase())[2:])
    # print(bin(rShiftBit(a).getBase())[2:])

if __name__ == "__main__":
    main()  
