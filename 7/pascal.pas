uses Lenght;

var
  f: TextFile;
  dates: array of String;
  line: String;
  minYear, maxYear, maxMonth, maxDay: Integer;
  springDates: array of String;
  listForMaxYear, listForMaxMonth, listForMaxDay: array of String;
  i, count: Integer;

begin
  AssignFile(f, 'data.txt');
  Reset(f);
  
  count := 0;
  while not Eof(f) do
  begin
    ReadLn(f, line);
    SetLength(dates, count + 1);
    dates[count] := line;
    count += 1;
  end;
  
  CloseFile(f);

  minYear := MaxInt;
  for i := 0 to len_arr(dates) - 1 do
  begin
    if StrToInt(Copy(dates[i], 7, 4)) < minYear then
      minYear := StrToInt(Copy(dates[i], 7, 4));
  end;

  WriteLn('a) ', minYear);

  for i := 0 to len_arr(dates) - 1 do
  begin
    if (Copy(dates[i], 4, 2) = '03') or (Copy(dates[i], 4, 2) = '04') or (Copy(dates[i], 4, 2) = '05') then
    begin
      SetLength(springDates, len_arr(springDates) + 1);
      springDates[len_arr(springDates) - 1] := dates[i];
    end;
  end;

  WriteLn('b) ', String.Join(', ', springDates));

  maxYear := -1;
  for i := 0 to len_arr(dates) - 1 do
    if StrToInt(Copy(dates[i], 7, 4)) > maxYear then
      maxYear := StrToInt(Copy(dates[i], 7, 4));

  for i := 0 to len_arr(dates) - 1 do
    if StrToInt(Copy(dates[i], 7, 4)) = maxYear then
    begin
      SetLength(listForMaxYear, len_arr(listForMaxYear) + 1);
      listForMaxYear[len_arr(listForMaxYear) - 1] := dates[i];
    end;

  maxMonth := -1; 
  for i := 0 to len_arr(listForMaxYear) - 1 do
    if StrToInt(Copy(listForMaxYear[i], 4, 2)) > maxMonth then
      maxMonth := StrToInt(Copy(listForMaxYear[i], 4, 2));

   for i := 0 to len_arr(listForMaxYear) - 1 do
     if StrToInt(Copy(listForMaxYear[i], 4, 2)) = maxMonth then
     begin
       SetLength(listForMaxMonth, len_arr(listForMaxMonth) + 1);
       listForMaxMonth[len_arr(listForMaxMonth) - 1] := listForMaxYear[i];
     end;

   maxDay := -1; 
   for i := 0 to len_arr(listForMaxMonth) - 1 do 
     if StrToInt(Copy(listForMaxMonth[i], 1, 2)) > maxDay then 
       maxDay := StrToInt(Copy(listForMaxMonth[i],1,2));

   for i :=0 to len_arr(listForMaxMonth) - 1 do 
     if StrToInt(Copy(listForMaxMonth[i],1,2)) = maxDay then 
     begin 
       SetLength(listForMaxDay, len_arr(listForMaxDay) +1); 
       listForMaxDay[len_arr(listForMaxDay) - 1] := listForMaxMonth[i]; 
     end;

   WriteLn('c) ', listForMaxDay[0]);
end.