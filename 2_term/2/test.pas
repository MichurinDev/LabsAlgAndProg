//Генерируем массив (кол-во от польщователя). Вывд: ср. арифм и сколько чисел больше него

var
  input: Array of Integer;
  n, i, avg, sum, num, count: integer;

begin
  write('Введите кол-во элементов: ');
  readln(n);
  
  SetLength(input, n);

  Randomize;

  for i := 0 to High(input) do begin
    num := Random(100);
    input[i] := num;
    sum += num;
  end;
  
  writeln('Исходный массив: ', input);
  
  avg := sum div Length(input);
  writeln('Ср. арифм.: ', avg);
  
  for i := 0 to High(input) do begin
    if input[i] > avg then
      count += 1;
  end;
  
  writeln('Кол-во n > avg: ', count)
end.