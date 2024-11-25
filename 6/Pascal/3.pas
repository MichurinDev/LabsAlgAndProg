// Разработайте функцию, которая принимает целочисленный аргумент n и выводит 
// числа от 1 до n.

procedure f(n: integer);
begin
  var i: integer;
  
  for i := 1 to n do
    writeln(i)
end;

procedure f_rec(n: integer);
begin
  if n > 0 then begin
    f_rec(n-1);
    writeln(n);
  end;
end;

begin
f(5);
writeln('---');
f_rec(5);
end.
