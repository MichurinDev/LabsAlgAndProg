program f1;
begin
  var num, divide, num_temp, i, sum, a: integer;
 
  Write('Введите число: ');
  ReadLn(num);
  
  num_temp := num;
  
  i := 1;
  divide := 1;

  while num_temp > 0 do begin
    a := num_temp mod (10 * i);
    num_temp := num_temp div 10;
    sum += a;
    divide *= a;
  end;

  writeln('Сумма: ', sum, '; Произведение: ', divide);

  sum := 0;
  i := 1;
  num_temp := num;
  divide := 1;

  repeat
    a := num_temp mod (10 * i);
    num_temp := num_temp div 10;
    sum += a;
    divide *= a;
  until num_temp <= 0;

  writeln('Сумма: ', sum, '; Произведение: ', divide);
end.