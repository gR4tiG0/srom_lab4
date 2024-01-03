#include <cstdint>
#include <inttypes.h>
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

extern "C" {
  void prArr(uint64_t* num, int size) {
        for (int i = 0; i<size;i++){
            printf("%lu ",num[i]);
        }
        printf("\n");
    }
  void lshiftB(uint64_t* number, int size) {
        for (int i = size - 1; i > 0; i--){
            number[i] = (number[i] << 1) | (number[i-1] >> ((8*64)-1));
        }
        number[0] <<= 1;
    }
    void rshiftB(uint64_t* number, int size) {
        for (int i = 0; i < size - 1; i++) {
            number[i] = (number[i] >> 1) | (number[i+1] << ((8*64) - 1));
        }
        number[size-1] >>= 1;
    }
  void cycleBL(uint64_t* number, int size, int bitSize) {
        uint64_t c = number[size-1] & (((uint64_t) 1 << (bitSize%64)) - 1);
        c = c >> ((bitSize%64) - 1);
        // printf("input ");
        // prArr(number,size);
        // printf("c %i\n",c);
        
        number[size-1] = (number[size-1] << 1) | (number[size-2] >> ((8*64)-1));
        
        // printf("bitSize %i\n",bitSize%64);
        // printf("%lu\n",((uint64_t)1 << (bitSize % 64)) - 1);

        number[size-1] = number[size-1] & (((uint64_t)1 << (bitSize%64)) - 1);
        for (int i = size - 2; i > 0; i--){
            number[i] = (number[i] << 1) | (number[i-1] >> ((8*64)-1));
        }
        // THIS NEED TO BE RETURNED I THINK
        number[0] <<= 1;
        // printf("befire c ");
        // prArr(number,size);
        if (c) {
          // number[0] ^= (1 << (bitSize-1) % 64);
          number[0] ^= c;
        }
        // printf("inside cycle ");
        // prArr(number,size);
    }
  void cycleBR(uint64_t* number, int size, int bitSize) {
        uint64_t c = number[0] & 1;
        for (int i = 0; i < size - 1; i++) {
            number[i] = (number[i] >> 1) | (number[i+1] << ((8*64) - 1));
        }
        number[size-1] >>= 1;
        if (c) {
          number[size-1] ^= ((uint64_t)1 << ((bitSize%64)-1));
        }
    }
  int trace(uint64_t* n, int size){
    int res = 0;
    for (int i = 0; i < size; i++){
      uint64_t tmp = n[i];
      while (tmp){
        res = (res + tmp%2)%2;
        tmp = tmp/2;
      }
    }
    return res;
  }
  void andw(uint64_t* a, uint64_t* b, uint64_t* res, int size) {
    // prArr(a, size);
    for (int i = 0; i < size; i++) {
      res[i] = a[i] & b[i];
    }
  }

  void gfmul(uint64_t* res, uint64_t* a, uint64_t* b, uint64_t* matrix, int size, int msize, int bitsize) {
    // prArr(matrix,msize);
        // printf("size %i\n",size);
    // prArr(tmp,size);
    for (int i = 0; i < bitsize; i++) {
      // printf("a ");
      // prArr(a,size);
      // printf("b ");
      // prArr(b,size);
      uint64_t* tmp = (uint64_t*)calloc(size, sizeof(uint64_t));
      uint64_t* tmpres = (uint64_t*)calloc(size, sizeof(uint64_t));
      for (int j = 0; j < bitsize; j++) {
        andw((matrix+(j*7)),b,tmp,size);
        // printf("b in for ");
        // prArr(b,size);
        // printf("matrix ");
        // prArr((matrix+j),size);
        // printf("tmp in for ");
        // prArr(tmp,size);  
        // printf("trace1: %i\n",trace(tmp,size));
        if (trace(tmp,size)) {
          // printf("log %i\n",(uint64_t)1 << ((bitsize - 1 - j)%64));
          
          tmpres[(bitsize - 1 - j)/64] ^= (uint64_t)1 << ((bitsize - 1 - j)%64);

          // tmpres[(j)/64] ^= (uint64_t)1 << ((bitsize - 1 - j)%64);

          // printf("tmpres in cycle, tmpres[2]: %i\n",tmpres[2]);
          // prArr(tmpres,size);
        }
      } 
      // printf("tmpres ");
      // prArr(tmpres,size);
      // prArr(a,size);
      andw(tmpres,a,tmp,size);
      // printf("a after andw ");
      // prArr(a,size);
      // printf("tmpres after andw ");

      // prArr(tmpres,size);
      // printf("trace2 %i\n",trace(tmp,size));
      if (trace(tmp,size)) {
        res[(bitsize - 1 - i)/64] ^= (uint64_t)1 << ((bitsize - 1 - i)%64);
      }
      // printf("a before cycle ");
      // prArr(a,size);
      cycleBL(a,size,bitsize);
      // printf("a after cycle ");
      // prArr(b,size);
      cycleBL(b,size,bitsize);
      // prArr(b,size);
      delete tmp;
      delete tmpres;
    }
  }
  
}
