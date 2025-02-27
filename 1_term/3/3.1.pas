program f1;
var x, num: real;
var i, j: integer;

function f (x: real): real;
  begin
    Result := (sin(x) / ln(Power(x, 2))) + (cos(x) / ln(Abs(x)))
  end;

begin
writeln('x', #9, '|', 'y');
writeln('+-----------------------------+');
  
//Способ 1
for i := 2 to 2 do
begin
  for j := 0 to 10 do
  begin
    num := (i * 10 + j) / 10;
    writeln(num, #9, '|', f(num))
  end;
end;

writeln('---------------');

//Способ 2
x := 2;
while x < 3.1 do
begin
  writeln(x, #9, '|', f(x));
  x += 0.1;
end;

writeln('---------------');

//Способ 3
x := 2;
repeat
  writeln(x, #9, '|', f(x));
  x += 0.1;
until x > 3.1;

end.