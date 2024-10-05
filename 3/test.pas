program f1;
begin
  var counter, i, end_num, sum: integer;
 
  counter := 0;
  end_num := 100;
  s
  for i := 3 to end_num do
  begin
    if i mod 3 = 0 then begin
      if sum + i <= 200 then begin
        sum += i;
        counter += 1;
      end;
    end;
  end;
  writeln(sum, ' ', counter);
  
  counter := 0;
  sum := 0;
  i := 3;

  while sum + i <= 200 do
  begin
    if i mod 3 = 0 then begin
      sum += i;
      counter += 1;
    end;
    i += 1;
  end;
  writeln(sum, ' ', counter);
  
  counter := 0;
  i := 3;
  sum := 0;
  repeat
    if i mod 3 = 0 then begin
      sum += i;
      counter += 1;
    end;
    i += 1;
  until sum + i > 200;
  
  writeln(sum, ' ', counter);
end.