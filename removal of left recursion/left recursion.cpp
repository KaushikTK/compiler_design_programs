#include<stdio.h>  
#include<string.h>  

int main () {  
       char non_terminal;  
       char beta,alpha;  
       int num;  
       char production[10][10];  
       int index=3;
       printf("Number of productions: ");  
       scanf("%d",&num);  
       for(int i=0;i<num;i++){  
            scanf("%s",production[i]);  
       }  
       for(int i=0;i<num;i++){  
            printf("%s",production[i]);  
            non_terminal=production[i][0];  
            if(non_terminal==production[i][3]) {  
                 alpha=production[i][4];  
                 printf(" is left recursive.\n");  
                 while(production[i][index]!=0 && production[i][index]!='|')  
                      index++;  
                 if(production[i][index]!=0) {  
                      beta=production[i][index+1];  
                      printf("%c->%c%c\'",non_terminal,beta,non_terminal);  
                      printf("\n%c\'->%c%c\'|Epsilon\n\n",non_terminal,alpha,non_terminal);  
                 }  
                 else  
                      printf(" can't be reduced\n");  
            }  
            else  
                 printf(" is not left recursive.\n");  
            index=3;  
       }  
  }   
