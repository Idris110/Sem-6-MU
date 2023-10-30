%{
void display(int);
%}

%%
[a|e|i|o|u]+ {
	int flag=1;
	display(flag);
	return;
	}
.+ {
	int flag=0;
	display(flag);
	return;
}
%%
void display(int flag)
{
	if(flag==0)
		printf("\nVowel\n");
	else
		printf("\nNot a vowel\n");
}

void main()
{
	printf("Enter a word : ");
	yylex();
}
