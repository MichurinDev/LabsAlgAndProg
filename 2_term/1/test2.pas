uses Fact;

var
  teams: Array of string;
  i, j, k: integer;
 
begin
  SetLength(teams, 8);
  for i := 0 to High(teams) do
    teams[i] := IntToStr(i+1);
  writeln('I | II | III');
  
  for i := 0 to High(teams) do
    for j := 0 to High(teams) do
      for k := 0 to High(teams) do begin
        if (i <> j) and (j <> k) and (i <> k) then
          writeln((i+1) + '    ' + (j+1) + '     ' + (k+1));
      end;
  
  writeln('Итого: ', factor(8) div factor(5));
end.