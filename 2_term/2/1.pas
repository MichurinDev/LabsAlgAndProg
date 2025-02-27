//Найти произведение элементов массива, имеющих нечетное значение.

var
  input: Array of integer;
  output, i, num: integer;

begin
  SetLength(input, 7);
  output := 1;

  Randomize;

  for i := 0 to High(input) do begin
    num := Random(100);
    input[i] := num;
    
    if (num mod 2 <> 0) then begin
      output := output * num;
    end;
  end;
  
  write('Исходный массив: ');
  writeln(String.Join(', ', input));
  writeln('Произведение нечётных чисел массива: ', output);
end.