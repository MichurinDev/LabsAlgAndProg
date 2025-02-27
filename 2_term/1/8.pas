//Монеты разной стоимости. Дано n различных монет. Напишите программу для подсчета
//количества способов, которыми можно набирать сумму S, используя данные монеты.
function countways(coins: array of integer; n: integer; S: integer): integer;
var
  dp: array of integer;
  i, j: integer;

begin
  setlength(dp, S + 1);
  dp[0] := 1;

  for i := 0 to n - 1 do
    for j := S downto coins[i] do
    begin
      dp[j] := dp[j] + dp[j - coins[i]];
    end;

  countWays := dp[S];
end;

var 
   coins: array of Integer;
   n, s, i: integer;

begin
  write('Введите количество монет: ');
  readln(n); 
  setlength(coins, n);
  
  writeln('Введите номиналы монет:');
  for i := 0 to n - 1 do
    read(coins[i]);
  
  write('Введите общую сумму монет: ');
  readln(s);
  
  writeln('Количество способов: ', countways(coins, n, s));
end.
