//Даны два целых числа a и b. Написать функцию, которая выводит все числа от a 
//до b включительно, в порядке возрастания, если a<b, или в порядке убывания в 
//противном случае.

procedure f(a: integer; b: integer);
begin
  var i: integer;

  if (a < b) then
    for i := a to b do
      writeln(i)
  else
    for i := a downto b do
      writeln(i);
end;

procedure f_rec(a: integer; b: integer);
begin
  var i: integer;
  
  if (a <= b) then begin
    if (a = b) then
      writeln(a)
    else begin
      writeln(a);
      f_rec(a+1, b);
    end;
  end
  else begin
    if (a = b) then
      writeln(a)
    else begin
      writeln(a);
      f_rec(a-1, b);
    end;
  end;
end;

begin
  f(1, 5);
  writeln('---');
  f(5, 1);
  writeln('---');
  f_rec(1, 5);
  writeln('---');
  f_rec(5, 1);
end.
