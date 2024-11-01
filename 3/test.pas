program f1;
begin
  var a, b, counter, i, j, del_c: integer;
  var flag: boolean;
 
  Write('Введите начало интервала: ');
  ReadLn(a);
  Write('Введите конец интервала: ');
  ReadLn(b);
  
  i := a;
  counter := 0;

  while i <= b do begin
    del_c := 0;
    flag := true;

    for j := 1 to Round(Power(i, 0.5)) do begin
      if (j <> 1) or (j <> i) then
        flag := false;
    end;

    if flag = false then begin
      counter += 1;
      WriteLn(i)
    end;
    i += 1;
  end;
  WriteLn(counter);

//  for i := 3 to end_num do
//  begin
//    if i mod 3 = 0 then begin
//      if sum + i <= 200 then begin
//        sum += i;
//        counter += 1;
//      end;
//    end;
//  end;
//  writeln(sum, ' ', counter);
//  
//  counter := 0;
//  sum := 0;
//  i := 3;
//
//  while sum + i <= 200 do
//  begin
//    if i mod 3 = 0 then begin
//      sum += i;
//      counter += 1;
//    end;
//    i += 1;
//  end;
//  writeln(sum, ' ', counter);
//  
//  counter := 0;
//  i := 3;
//  sum := 0;
//  repeat
//    if i mod 3 = 0 then begin
//      sum += i;
//      counter += 1;
//    end;
//    i += 1;
//  until sum + i > 200;
//  
//  writeln(sum, ' ', counter);
end.