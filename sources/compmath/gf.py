#main file for compmath lib, implemetation of operation in normal basis
from typing import Any
from compmath.helper import *
from math import log2
import ctypes
BASE = 64

lib = ctypes.CDLL('compmath/gflib.so')


def mCheck(i:int,j:int,p:int) -> bool:
    i,j = 2**i,2**j
    if (i+j)%p == 1 or (i-j)%p == 1 or (-i+j)%p == 1 or (-i-j)%p == 1:
        return True 
    else:
        return False 

def getMatrix(m:int):
    p = m*2 + 1 
    word_num = (m//64 + 1)
    res = []
    for i in range(m):
        tmp = 0
        for j in range(m):
            if mCheck(i,j,p):
                tmp ^= 1 << (m - j - 1)
        tmp = parse(tmp)
        while len(tmp) < word_num:
            tmp += [0]
        res += tmp
    # print("matrix",res[:70])
    return GFelement(res,m,0)


class GF:
    def __init__(self, m=419) -> Any:
        # if check(m):
        if True:
            self.m = m
            self.p = 2**m
            self.matrix = getMatrix(m)
        else:
            raise ValueError("Invalid value for creating GF.")
    def __call__(self, n) -> Any:
        tmp = GFelement(n, self.m, self.matrix)      
        return tmp
    
def parse(n:int) -> list:
    res = []
    m = 2**BASE
    while n:
        res += [n % m]
        n = n // m 
    return res


class GFelement:
    def __init__(self, number, m, matrix):
        word_num = m//64 + 1
        if isinstance(number, int):
            if number == 0: words = [0]
            elif number == 1: words = [1]
            else: words = parse(number)
            
        elif isinstance(number, list):
            # while number[-1] == 0 and len(number) > 3:
                # number.pop()
            words = number
        else:
            raise ValueError("Invalid input")
        self.m = m
        self.words = words
        while len(self.words) < word_num:
            self.words += [0]
        self.l = self.bitLen()
        self.matrix = matrix

    def bitLen(self):
        if set(self.words) == {0}:
            return 0
        c = 0
        while self.words[-1-c] == 0: c += 1
        msb = self.words[-1-c]
        bitsize = 0
        while msb > 0:
            msb >>= 1
            bitsize += 1
        return (len(self.words) - 1 - c)*64 + bitsize


    def isnull(self):
        if set(self.words) == {0}:
            return True 
        return False

    def getBase(self) -> int:
        res = 0
        for elem in self.words[::-1]:
            res = (res * 2**BASE) + elem
        return res
    def __repr__(self):
        return hex(self.getBase())
    
    def __str__(self):
        return hex(self.getBase())

    def __add__(self, other):
        res_ = []
        for i in range(max(len(self.words), len(other.words))):
            if i >= len(self.words): a = 0
            elif i >= len(other.words): b = 0
            else:
                a,b = self.words[i],other.words[i]
                res_ += [a^b]
        return GFelement(res_,self.m,self.matrix)

    def lshB(self):
        self_D = list(self.words+[0])
        size = len(self_D)
        self_c = (ctypes.c_uint64 * size)(*self_D)
        lib.lshiftB(self_c,size)
        result = list(self_c)
        while len(result) > 1 and result[-1] == 0:
            result.pop()
        return GFelement(result,self.m,self.matrix)
    
    def rshB(self):
        self_D = list(self.words+[0])
        size = len(self_D)
        self_c = (ctypes.c_uint64 * size)(*self_D)
        lib.rshiftB(self_c,size)
        result = list(self_c)
        while len(result) > 1 and result[-1] == 0:
            result.pop()
        return GFelement(result,self.m,self.matrix)
     
    def cycleBL(self):
        self_D = list(self.words)
        size = len(self_D)
        self_c = (ctypes.c_uint64 * size)(*self_D)
        lib.cycleBL(self_c,size,self.m)
        result = list(self_c)
        while len(result) > 1 and result[-1] == 0:
            result.pop()
        return GFelement(result,self.m,self.matrix)
    
    def cycleBR(self):
        self_D = list(self.words)
        size = len(self_D)
        self_c = (ctypes.c_uint64 * size)(*self_D)
        lib.cycleBR(self_c,size,self.m)
        result = list(self_c)
        while len(result) > 1 and result[-1] == 0:
            result.pop()
        return GFelement(result,self.m,self.matrix)
     
    def __pow__(self, n):
        if n == 2:
            return self.cycleBR()

    def __mul__(self,other):
        a_ = list(self.words)
        b_ = list(other.words)
        m = list(self.matrix.words)
        assert len(a_) == len(b_)
        size = len(a_)
        mSize = len(m)
        a_c = (ctypes.c_uint64 * size)(*a_)
        b_c = (ctypes.c_uint64 * size)(*b_)
        m_c = (ctypes.c_uint64 * mSize)(*m)
        res = (ctypes.c_uint64 * size)()
        lib.gfmul(res,a_c,b_c,m_c,size,mSize,self.m)
        res = list(res)
        return GFelement(res,self.m,self.matrix)

