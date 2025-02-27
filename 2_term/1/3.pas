//Разделение на подмножества. Реализуйте алгоритм, который проверяет, может ли 
//заданный набор чисел быть разделен на две подгруппы с одинаковой суммой.

var
  nums: Array of integer;
  n, totalSum, targetSum: integer;
  dp: Array of boolean;

function CanPartition: boolean;
var
  i, j: integer;
begin
  totalSum := 0;
  
  for i := 0 to n - 1 do
    totalSum := totalSum + nums[i];

  if totalSum mod 2 = 0 then begin
    targetSum := totalSum div 2;
    
    SetLength(dp, targetSum + 1);
    dp[0] := True;
  
    for i := 0 to n - 1 do
      for j := targetSum downto nums[i] do
        dp[j] := dp[j] or dp[j - nums[i]];
  
    Result := dp[targetSum];
   end;
end;

begin
  write('Введите количество элементов: ');
  readln(n);
  
  SetLength(nums, n);
  
  WriteLn('Введите ' + n + ' чисел:');
  for var i := 0 to n - 1 do
    Read(nums[i]);

  if CanPartition then writeln('Возможно')
  else writeln('Невозможно');
end.
