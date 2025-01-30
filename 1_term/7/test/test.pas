//Скрипт, считывающий числа с файла и выводящий уникальные

var
  f: TextFile;
  line: string;
  uinq_arr: array of string;
  in_uinq_arr: boolean;
  i, len: integer;


begin
AssignFile(f, '1.txt');
Reset(f);

while not Eof(f) do begin
  ReadLn(f, line);

  in_uinq_arr := False;
  if Length(uinq_arr) <> 0 then begin
    for i := 1 to Length(uinq_arr) do begin
      if uinq_arr[i-1] = line then
        in_uinq_arr := True;
    end;
  
    if in_uinq_arr = False then begin
      writeln(line);
      SetLength(uinq_arr, Length(uinq_arr) + 1);
      uinq_arr[Length(uinq_arr) - 1] := line;
    end
   end
   else begin
     writeln(line);
     SetLength(uinq_arr, Length(uinq_arr) + 1);
     uinq_arr[Length(uinq_arr) - 1] := line;
   end;
end;
end.