program f1;

var
  country, city, surname1, surname2, city1, city2, city3, s1, s2: string;
  counter: Integer;

begin    
  // Задача 1
  WriteLn('Задача 1');
  Write('Введите страну: ');
  ReadLn(country);
  Write('Введите город: ');
  ReadLn(city);
  WriteLn('Столица государства ', country, ' — город ', city);

  // Задача 2
  writeln('Задача 2');
  write('Введите фамилию: ');
  readln(surname1);
  write('Введите фамилию: ');
  readln(surname2);

  if length(surname1) > length(surname2) then
    writeln(surname1, ' длинее')
  else
    writeln(surname2, ' длинее');

  // Задача 3
  writeln;
  writeln('Задача 3');
  write('Введите город: ');
  readln(city1);
  write('Введите город: ');
  readln(city2);
  write('Введите город: ');
  readln(city3);

  if length(city1) > length(city2) then
  begin
    if length(city1) > length(city3) then
      writeln('Самое длинное ', city1)
    else
      writeln('Самое длинное ', city3);
  end
  else
  begin
    if length(city2) > length(city3) then
      writeln('Самое длинное ', city2)
    else
      writeln('Самое длинное ', city3);
  end;

  if length(city1) < length(city2) then
  begin
    if length(city1) < length(city3) then
      writeln('Самое короткое ', city1)
    else
      writeln('Самое короткое ', city3);
  end
  else
  begin
    if length(city2) < length(city3) then
      writeln('Самое короткое ', city2)
    else
      writeln('Самое короткое ', city3);
  end;
  
  // Задача 4
  writeln('Задача 4');
  write('Введите первую страну: ');
  readln(s1);
  write('Введите вторую страну: ');
  readln(s2);

  s1 := s2;
  s2 := s1;

  writeln('Первая страна: ', s1);
  writeln('Вторая страна: ', s2);
end.