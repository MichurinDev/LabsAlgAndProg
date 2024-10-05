program f1;
var a, b, c: boolean;

//Задание 1
function f (x: real): real;
  begin
    if x < 5 then
      Result := 16 * Power(x, 4) - 16
    else if (x >= 5.0) and (x <= 20.0) then
      Result := 2 * Power(x, 7)  + x ** 2 - 321
    else
      Result := x / 19 - Power(x, 2) + 5
  end;

begin
write('x = ');
readln(x);
y := f(x);
writeln(y);

//Задание 2
write('a = ');
readln(a);
write('b = ');
readln(b);
write('c = ');
readln(c);

writeln(a and b and c);
writeln(a or b or c);
writeln(a or b and c);
writeln(a and b or c);

writeln(not a and b and c);
writeln(a and not b and c);
writeln(a and b and not c);
writeln(not a and not b and c);
writeln(a and not b and not c);
writeln(not a and b and not c);
writeln(not a and not b and not c);

writeln(not a or b or c);
writeln(a or not b or c);
writeln(a or b or not c);
writeln(not a or not b or c);
writeln(a or not b or not c);
writeln(not a or b or not c);
writeln(not a or not b or not c);

writeln(not a or b and c);
writeln(a or not b and c);
writeln(a or b and not c);
writeln(not a or not b and c);
writeln(a or not b and not c);
writeln(not a or b and not c);
writeln(not a or not b and not c);

writeln(not a and b or c);
writeln(a and not b or c);
writeln(a and b or not c);
writeln(not a and not b or c);
writeln(a and not b or not c);
writeln(not a and b or not c);
writeln(not a and not b or not c);
end.