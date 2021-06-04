# include <stdio.h>
# include <conio.h>
# include <string>
# include <ctype.h>
#include <iostream>
using namespace std;

int ret[100];
static int pos=0;
static int sc=0;
void nfa(int st,int p,char *s)
{    int i,sp,fs[15],fsc=0;
	sp=st;pos=p;sc=st;
	while(*s)
	{if(isalpha(*s))
	    {ret[pos++]=sp;
		ret[pos++]=*s;
		ret[pos++]=++sc;}
	if(*s=='.')
		{sp=sc;
		 ret[pos++]=sc;
		 ret[pos++]=69;
		 ret[pos++]=++sc;
		 sp=sc;}
	if(*s=='|')
		{sp=st;
		 fs[fsc++]=sc;}
	if(*s=='*')
		{ret[pos++]=sc;
		 ret[pos++]=69;
		 ret[pos++]=sp;
		 ret[pos++]=sp;
		 ret[pos++]=69;
		 ret[pos++]=sc;
		 }
	 if (*s=='(')
		{char ps[50];
		 int i=0,flag=1;
		 s++;
		   while(flag!=0)
			{ps[i++]=*s;
			 if (*s=='(')
				flag++;
			 if (*s==')')
				flag--;
			 s++;}
			 ps[--i]='\0';
			 nfa(sc,pos,ps);
			 s--;
		}
	 s++;
	}
	sc++;
	  for(i=0;i<fsc;i++)
		 {ret[pos++]=fs[i];
		  ret[pos++]=69;
		  ret[pos++]=sc;
		 }
		  ret[pos++]=sc-1;
		  ret[pos++]=69;
		  ret[pos++]=sc;
}


int main()
{    int i;
	char inp[10];
	printf("enter the regular expression :");
	cin>>inp;
	nfa(1,0,&inp[0]);
	int max = -1;
	for(i=0;i<pos;i=i+3)
	    if(ret[i]>ret[i+2]) max = ret[i];
	    else max = ret[i+2];
	string trans_table[max+1][max+1];
	for(i=0;i<max+1;i++)
	{for(int j=0;j<max+1;j++) trans_table[i][j]=(char)32;
	}
	int asc = 49;
	int asc2 = 49;
	for(i=1;i<max+1;i++){trans_table[0][i]=(char)asc;asc++;}
	for(i=1;i<max+1;i++){trans_table[i][0]=(char)asc2; asc2++;}
	
	
	for(i=0;i<pos;i=i+3)
	{
	    string x = trans_table[ret[i]][ret[i+2]];
        x = x + (char)ret[i+1] + '/';
        trans_table[ret[i]][ret[i+2]] = x;
 	}
	    
	for(i=0;i<max+1;i++)
	{
	    for(int j=0;j<max+1;j++)cout<<trans_table[i][j]<<"          ";
	    cout<<"\n";
	}
	
	for(int i=0;i<pos;i=i+3)
	{
	    cout<<ret[i]<<"--"<<(char)ret[i+1]<<"-->"<<ret[i+2]<<"\n";
	}
	return 0;
}
