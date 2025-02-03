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
    for i := 0 to n - 1 do
      Write(permutation[i], ' ');
    Writeln;
    Exit;
  end;

  for i := 1 to n do
  begin
    if not used[i] then begin]
      if (depth = i - 1) and condition[i] then
        Continue;

      used[i] := True;
      permutation[depth] := i;
      GeneratePermutations(depth + 1);
      used[i] := False; 
    end;
  end;
end;

begin
  Write('Введите n (количество элементов): ');
  ReadLn(n);

  SetLength(permutation, n);
  SetLength(used, n + 1); // Массив для отслеживания использованных чисел
  SetLength(condition, n + 1); // Массив условий

  { Пример условий: числа не могут стоять на своих позициях }
  for var i := 1 to n do
    condition[i] := True; // Изначально все условия активны

  { Устанавливаем условия для конкретных позиций }
  condition[2] := False; // Например, число не может стоять на второй позиции

  Writeln('Все возможные перестановки чисел от 1 до ', n, ' с заданными условиями:');
  
  GeneratePermutations(0); // Начинаем с глубины 0

end.
