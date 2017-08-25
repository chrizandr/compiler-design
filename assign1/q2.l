%{
    #include<iostream>
    #include<sstream>
    #include<string>
    using namespace std;

    string day="";
    string month="";
    string year="";
    int separator_count=0;

    string get_year(char* s){
        int year, d1, d2;
        d1 = (int) s[0] - 48;
        d2 = (int) s[1] - 48;
        year = d1 * 10 + d2;
        if(year <= 17)
        {
          year = year + 2000;
        }
        else
        {
          year = year + 1900;
        }
        stringstream year_string;
        year_string << year;
        return year_string.str();
    }

    string print_date(int separator_count, string day, string month, string year){
        if(separator_count >= 2 && day != "" && month != "" && year != "")
        {
            return  day + "/" + month + "/" + year;
        }
        return  "Not valid date format";

    }

%}

%%
[1-9]                               day=string("0")+yytext;
[/|\-|\.|,| ]                       separator_count++;
[0-9][0-9]                          {if(separator_count==0)day=yytext;
                                     if(separator_count==1 && month!="")day=yytext;
                                     if(separator_count==1 && month=="")month=yytext;
                                     if(separator_count==2)year=get_year(yytext);}
[jJ][a][n]([u][a][r][y])?           month="01";
[fF][e][b]([r][u][a][r][y])?        month="02";
[Mm][a][r]([c][h])?                 month="03";
[aA][p][r]([i][l])?                 month="04";
[mM][a][y]                          month="05";
[Jj][u][n]([e])?                    month="06";
[jJ][u][l]([y])?                    month="07";
[Aa][u][g]([u][s][t])?              month="08";
[sS][e][p]([t][e][m][b][e][r])?     month="09";
[Oo][c][t]([o][b][e][r])?           month="10";
[Nn][o][v]([e][m][b][e][r])?        month="11";
[Dd][e][c]([e][m][b][e][r])?        month="12";
[1-9][0-9][0-9][0-9]                year=yytext;
.                                   ;
\n                                 {cout << print_date(separator_count, day, month, year) << endl;
                                    day="";year="";month="";separator_count=0;}
<<EOF>>                            return 0;
%%

int main(void)
{
    yylex();
    return 0;
}
