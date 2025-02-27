//Написать функцию, печатающую все целые числа от a до b включительно
//(a ≤ b, не забудьте это проверить)

program f1;
 
procedure f(a: integer; b: integer);
begin
  var i: integer;
  
  if (a <= b) then begin
    for i := a to b do
      writeln(i);
  end;
end;

procedure f_rec(a: integer; b: integer);
begin
  var i: integer;
  
  if (a <= b) then begin
    writeln(a);
    f_rec(a+1, b);
  end;
end;

begin
  f(1, 5);
  writeln('---');
  f_rec(1, 5);
end.