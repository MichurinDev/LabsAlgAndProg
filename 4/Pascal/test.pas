program test;

uses Lenght;

var
  s1: string;
  s2: string;
  temp_str: string;
  i: integer;
  count: integer;

function count_by_symbol(str: string; symb: char): integer;
  var 
    i: integer;
    s: string;
    counter: integer;
  
  begin
    i := 1;
    for i := 1 to len(str) do begin
      if str[i] = symb then
        counter += 1
    end;

  Result := counter;
end;

begin
Write('Введите первую строку: ');
ReadLn(s1);
Write('Введите вторую строку: ');
ReadLn(s2);

i := 0;

if len(s1) = len(s2) then begin
  for i := 1 to len(s1) do begin
    if count_by_symbol(s1, s1[i]) = count_by_symbol(s2, s1[i]) then begin
      if s1[i] not in temp_str then
        temp_str += s1[i];
      count += 1;
    end;
  end;
end;

if (count = len(s1)) then
  writeln('Аннограмма')
else
  writeln('Не аннограмма');

end.