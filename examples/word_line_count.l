%{
    /*Definitions*/
    int charcount = 0;
    int linecount = 0;
%}

%%
.   {charcount++;}
\n  {linecount++; charcount++;}
%%

int main(){
    yylex();
    printf("The number of characters are %d, and the number of lines are %d", charcount, linecount);
    return 0;
}
