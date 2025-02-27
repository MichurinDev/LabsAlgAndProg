//Сумма подмножеств. Дано множество чисел. Найдите все подмножества этого множества, 
//сумма элементов которых равна заданному числу.

var
  nums: Array of integer;
  target: integer;
  n: integer;

procedure FindSubsets(index: integer; currentSum: integer; subset: Array of integer; count: integer);
var
  i: integer;

begin
  if currentSum = target then begin
    for i := 0 to count - 1 do
      Write(subset[i], ' ');
    Writeln;
  end;

  for i := index to n - 1 do begin
    if currentSum + nums[i] <= target then begin
      subset[count] := nums[i];
      FindSubsets(i + 1, currentSum + nums[i], subset, count + 1);
    end;
  end;
end;

var
  subset: array of Integer;
  i: integer;

begin
  Write('Введите количество элементов: ');
  ReadLn(n);
  SetLength(nums, n);

  WriteLn('Введите ' + n + ' чисел:');
  for i := 0 to n - 1 do
    Read(nums[i]);

  Write('Введите целевую сумму: ');
  ReadLn(target);

  SetLength(subset, n);
  
  Writeln('Найденные подмножества с суммой ' + target + ':');
  FindSubsets(0, 0, subset, 0);
end.
