//Рекурсивная функция на Pascal
//Принимает - строку с цифрами
//Возвращает - сумма цифр

uses Lenght;

function f(line: string): integer;
begin
  var n, code: integer;
  if len(line) = 1 then begin
    Val(line, n, code);
    Result := n;
  end
  else begin
    Val(line[1], n, code);
    Result := n + f(line[2:])
  end;
end;

begin
  var n: string;
  write('Введите число: ');
  readln(n);
  writeln(f(n));
end.