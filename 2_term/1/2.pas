//Реализуйте алгоритм, который генерирует все возможные комбинации k элементов из n 
//различных элементов. Например, для n = 4 и k = 2 результатом должны быть комбинации: 
//(1,2), (1,3), (1,4), (2,3), (2,4), (3,4).

var
  n, k: integer;
  combination: Array of integer;

procedure GenerateCombinations(start: integer; depth: integer);
var
  i: integer;

begin
  if depth <> k then begin
    for i := start to n do begin
      combination[depth] := i;
      GenerateCombinations(i + 1, depth + 1);
    end;
  end
  else begin
    for i := 0 to k - 1 do begin
      write(combination[i] + ' ');
    end;
    writeln();
  end;
end;

begin
  Write('Введите n (количество элементов): ');
  ReadLn(n);
  
  Write('Введите k (количество выбираемых элементов): ');
  ReadLn(k);

  SetLength(combination, k);
  GenerateCombinations(1, 0);
end.
