#!/usr/bin/python3 
from compmath.gf import *
from random import getrandbits
import time 

def main() -> None:
    fld = GF()
    BITS = fld.m 
    # print(len(bin(fld.matrix.getBase())[2:]))
    A = 0x2a2d878f41e5c99f64fb7d2497aee5e0d2bc49e98d9abcb08c9599879c12a7e1f330a43b4594f270ef21b4f966c09e5acd06ee8a3
    B = 0x6df2d5505147c6aa31013f32bab48a91f8203f87c0d29f0fda3951f0bc26c73c7b8b81f8e54426219a31d098b7b85447c56afd486
    # time_start = time.time()
    # for _ in range(1):
    # A,B = getrandbits(BITS),getrandbits(BITS)
    # B,A = int('011',2),int('101',2)
        # a,b = fld(A),fld(B)
        # a*b 
    # time_end = time.time()
    # print(f"[!] Time elapsed: {(time_end - time_start)/1}")
    
    A,B = B,A
    # A,B = 1,2
    # A = 123
    # print("A bit len", A.bit_length())
    # print("A before", bin(A)[2:])
    a,b = fld(A),fld(B)
    print(a,b)
    # print("A after", bin(A >> 1)[2:])
    # ab = bin(a.cycleBR().getBase())[2:]
    # print("a bit len",len(ab))
    # print("a after", ab)
    # print(fld(A >> 1).words)
    # print(a.cycleBL().words)


    # print(a,b)
    # c = a+ b 
    # print("a+b",c)
    # c = a**2
    # print("a**2",c)
    # print("trace",a.trace())
    c = a*b
    print("a*b =",c)
    # print(c.words)
    # C = 0x021216A71F68045FE74AC144D7225ED60E2F0EBDB421FEE060ABC4D842FEE07370CB426CB82779C38AA4FE58A2988C217751813A5F
    # print(fld(C).words)
    



if __name__ == "__main__":
    main()  
