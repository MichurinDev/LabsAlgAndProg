//Дан одномерный массив Х1, Х2, …, Хn . Все ли элементы массива больше 3?

var
  input: Array of integer;
  i, num: integer;
  flag: boolean;

begin
  SetLength(input, 7);
  flag := true;

  Randomize;

  for i := 0 to High(input) do begin
    num := Random(100);
    input[i] := num;
    
    if (num <= 3) then
      flag := false;
  end;
  
  write('Исходный массив: ');
  writeln(String.Join(', ', input));
  
  if flag then
    writeln('Да, все')
  else
    writeln('Нет, не все');
end.