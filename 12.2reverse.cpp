#include <stdio.h>
#include<bits/stdc++.h>
using namespace std;
// Promila Agarwal
// K & R method 
void reverse(char p[])
{
  char *end = p;
  int length = strlen(p);
  int i, c, j;
  for (i= 0, j = length-1; i < j; i++, j--){
  	c = p[i];
  	p[i] = p[j];
  	p[j] = c;
  }
}
// Book method
void reverseCtc(char *str) {
 char * end = str;
 char tmp;
 if (str) {
   while (*end) {
    ++end;
   
    }
  --end;
  while (str < end) {
   		tmp = *str;
  		*str++ = *end;
  		*end-- = tmp;
  	}
  }
}

int main()
{
  char *str1 = (char*)malloc(200 * sizeof(char));
   scanf("%[^\n]s", str1); 
  reverse(str1);
  printf("%s\n",str1);
  reverseCtc(str1);
  printf(str1);
  return 0;
}
