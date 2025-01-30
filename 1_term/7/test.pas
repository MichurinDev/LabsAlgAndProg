//Читает числа из файла, выводит кол-во уникальных и дубликатов
uses Lenght;

function str_count_in_str_arr(line: string; arr: array of String): integer;
begin
  var i, count: integer;
  for i := 1 to len_arr(arr) do begin
    if arr[i-1] = line then
      count += 1;
  end;
  
  Result := count;
end;

var
  f: TextFile;
  repeat_counter, uniq_counter, i, j, n, count: integer;
  line: String;
  lines, repeat_arr: array of String;
  in_repeat_arr: boolean;

begin  
  AssignFile(f, 'test_data.txt');
  
  rewrite(f);

  randomize;
  for i := 0 to 9 do begin
    n := random(10);
    Writeln(f, n);
  end;
  CloseFile(f);
 
  AssignFile(f, 'test_data.txt');
  Reset(f);

  count := 0;

  while not Eof(f) do
  begin
    ReadLn(f, line);
    SetLength(lines, len_arr(lines) + 1);
    lines[len_arr(lines)-1] := line;
  end;
  
  writeln(lines);
  
  for i := 1 to len_arr(lines) do begin
      line := lines[i-1];
      count := str_count_in_str_arr(line, lines);
  
      if count = 1 then
        uniq_counter += 1
      else begin
          if len_arr(repeat_arr) > 0 then begin
                in_repeat_arr := False;
                for j := 1 to len_arr(repeat_arr) do begin
                  if line = repeat_arr[j-1] then
                    in_repeat_arr := True;
                end;
                
                if in_repeat_arr = False then begin
                  repeat_counter += 1;
                  SetLength(repeat_arr, len_arr(repeat_arr) + 1);
                  repeat_arr[len_arr(repeat_arr)-1] := line;
                end;
          end
          else begin
            repeat_counter += 1;
            SetLength(repeat_arr, len_arr(repeat_arr) + 1);
            repeat_arr[len_arr(repeat_arr)-1] := line;  
          end;
    end;
  end;

  writeln('Уникальных: ', uniq_counter);
  writeln('Повторяющихся: ', repeat_counter);
end.