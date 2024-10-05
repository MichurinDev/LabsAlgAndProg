program f1;

var  a, b, x, x_start, x_end, x_delta, iterator: Integer;

function f(x: Real): Real;
begin
  Result := Ln(1.2 * x + 2.3) + (Exp(3 * x) * Sinh(x));
end;

function g(x: Real): Real;
begin
  Result := Power(5, Power(x, 2) + 1) * Power(Power(x, 3.3) + Power(Abs(1 - x), 0.5), 0.5);
end;

function h(x: Real): Real;
begin
  Result := Power(1 + Power(Tan(x), 2), Arctan(x) + Ln(x) + 1);
end;

begin
  write('a = ');
  readln(a);
  write('b = ');
  readln(b);
  write('начало = ');
  readln(x_start);
  write('конец = ');
  readln(x_end);
  write('интервал = ');
  readln(x_delta);

  writeln('x', #9, '|', 'y');
  writeln('+-----------------------------+');

  // Способ 1
  iterator := 0;
  for x := x_start to x_end do
  begin
    if (iterator = 0) or (iterator mod x_delta = 0) then
      if x <= a then
        writeln(x, #9, '|', f(x))
      else if (a < x) and (x < b) then
        writeln(x, #9, '|', g(x))
      else if x >= b then
        writeln(x, #9, '|', h(x));
      iterator += 1
  end;

  writeln('+-----------------------------+');

  x := x_start;
  while x <= x_end do
  begin
    if x <= a then
      writeln(x, #9, '|', f(x))
    else if (a < x) and (x < b) then
      writeln(x, #9, '|', g(x))
    else if x >= b then
      writeln(x, #9, '|', h(x));
    x += x_delta;
  end;
  
  writeln('+-----------------------------+');
  
  //Способ 3
  x := x_start;
  repeat
    if x <= a then
      writeln(x, #9, '|', f(x))
    else if (a < x) and (x < b) then
      writeln(x, #9, '|', g(x))
    else if x >= b then
      writeln(x, #9, '|', h(x));
    x += x_delta;
  until x > x_end;
end.
