#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* alloc_memory() {
  char* str = strdup("Hello World");
  printf("Memory allocated....\n");
  return str;
}

void free_memory(char* ptr) {
  free(ptr);
  printf("Memory deallocated...\n");
}