program f1;
var a, x, b, y: real;

function f (x, a, b: real): real;
  begin
  Result := ((b + Power(SIN(a * x),  2)) / (EXP(1) ** (-x / 2)))
  end;

begin
write('x = ');
readln(x);
write('a = ');
readln(a);
write('b = ');
readln(b);

y := f(x, a, b);
write('y = ');
writeln(y)
end.