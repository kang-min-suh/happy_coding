struct fns {
    int*(*fn)(int*); 
} mine; 

int* dummy(int *d) {
    return d+1; 
}

int main() {
    struct fns mine; 
    int n[] = {16, 32}; 
    mine.fn = dummy; 
    printtf("%x", *mine.fin(n)); 
    return 0; 
}