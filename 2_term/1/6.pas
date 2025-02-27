//Расстановки с условиями. Напишите программу, которая генерирует все возможные 
//перестановки чисел от 1 до n, при этом каждая перестановка должна удовлетворять 
//заданным условиям (например, числа не могут стоять на определенных позициях).

var
  n: integer;
  condition: Array of boolean;
  permutation: Array of integer;
  used: Array of boolean;

procedure GeneratePermutations(depth: integer);
var
  i: integer;

begin
  if depth = n then begin
    for i := 0 to n-1 do
      write(permutation[i], ' ');
    writeln;
  end
  else begin
    for i := 1 to n do begin
      if not used[i] then begin
        if true then begin
          used[i] := True;
          permutation[depth] := i;
          GeneratePermutations(depth + 1);
          used[i] := False; 
        end;
      end;
    end;
  end;
end;

begin
  write('Введите n (количество элементов): ');
  readln(n);

  SetLength(permutation, n);
  SetLength(used, n + 1);
  SetLength(condition, n + 1);

  for var i := 1 to n do
    condition[i] := True;

  condition[2] := False;
  
  GeneratePermutations(0);
end.