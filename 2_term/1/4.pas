//Счётчик различных подстрок. Напишите программу, которая принимает строку и 
//подсчитывает количество различных подстрок в этой строке.

function el_in_arr(arr: Array of string; el: string): boolean;
begin
  var i: integer;
  for i := 0 to Length(arr) - 1 do begin
    if arr[i] = el then
      el_in_arr := true;
  end;
end;

begin
  var line, substr: string;
  var i, j, counter: integer;
  var output: real;
  var used_substr: Array of string;
  
  write('Введите строку: ');
  readln(line);
  
  for i := 1 to Length(line) do
    for j := i to Length(line) do begin
      substr := Copy(line, i, j - i + 1);

      if not el_in_arr(used_substr, substr) then begin
        counter += 1;

        SetLength(used_substr, Length(used_substr) + 1);
        used_substr[High(used_substr)] := substr;
      end;
    end;
    writeln('Количество подстрок: ' + counter)
end.