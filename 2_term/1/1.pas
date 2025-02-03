//Напишите программу, которая находит число различных перестановок слова,
//учитывая количество повторяющихся букв.
//Например, для слова "AAB" результат должен быть 3 (AAB, ABA, BAA).

uses Fact;

function count_symb_by_line(line, s: string): integer;
begin
  var i, count: integer;
  for i := 1 to Length(line) do begin
    if line[i] = s then
      count += 1;
  end;
  
  Result := count;
end;

function symb_in_line(line, s: string): boolean;
begin
  var i: integer;
  var answer: boolean;
  answer := false;
  
  for i := 1 to Length(line) do begin
    if line[i] = s then
      answer := true;
  end;
  
  Result := answer;
end;

function count_symb_in_line(line, s: string): integer;
begin
  var count, i: integer;
  
  for i := 1 to Length(line) do begin
    if line[i] = s then
      count += 1;
  end;
  Result := count;
end;

var line, used_symb: string;
var count_symb, answer, i: integer;

begin
  write('Введите последовательность: ');
  readln(line);
  
  answer := factor(Length(line));

  for i := 1 to Length(line) do begin
    if symb_in_line(used_symb, line[i]) = false then begin
      answer := answer div factor(count_symb_in_line(line, line[i]));
      used_symb += line[i];
    end;
  end;
  
  writeln(answer);
end.