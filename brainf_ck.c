#include<stdio.h>


int main() {
    char data[65000];
    int ptr = 0;
    
    for (int i=0; i<65000; i++) {
        data[i] = 0;
    }
    
    // +++>++<[->+<]>.
    data[ptr]++;    
    data[ptr]++;    
    data[ptr]++;    
    ptr++;
    data[ptr]++;    
    data[ptr]++;    
    ptr--;

    while (data[ptr] != 0) {
        data[ptr]--;
        ptr++;
        data[ptr]++;
        ptr--;   
    }
    
    ptr++;
    putchar(data[ptr] + 48);
    printf("\n");

    return 0;
}
