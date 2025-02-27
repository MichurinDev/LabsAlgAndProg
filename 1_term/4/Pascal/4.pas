program f4;

uses Lenght;

var
  sentence, output: string;
  i, comma_counter: Integer;
  found, flag: Boolean;

begin
  // Задача 1
  WriteLn('Задача 1');
  Write('Введите предложение: ');
  ReadLn(sentence);

  output := '';

  for i := 1 to len(sentence) - 1 do
  begin
    if (sentence[i] = sentence[i + 1]) and (output = '') then
    begin
      output := i + ' ' + (i + 1);
    end;
  end;

  if output = '' then
    WriteLn('Предложение не содержит повторяющихся символов')
  else
    writeln(output);

  // Задача 2
  WriteLn;
  WriteLn('Задача 2');
  Write('Введите предложение: ');
  ReadLn(sentence);
  
  output := '';
  i := 0;
  comma_counter := 0;
  
  while (i < len(sentence)) and (comma_counter <> 2) do
  begin
    if sentence[i + 1] = ',' then
      comma_counter += 1;
  
    if (comma_counter = 1) and (sentence[i + 1] <> ',') then
      output += sentence[i + 1];
    
    i += 1;
  end;
  
  WriteLn('Результат: ', output);

  // Задача 3
  WriteLn;
  WriteLn('Задача 3');
  Write('Введите предложение: ');
  ReadLn(sentence);

  sentence := LowerCase(sentence);
  found := False;
  output := '';
  i := 1;

  while (i <= Length(sentence)) and not found do
  begin
    if ((sentence[i] = 'с') or (sentence[i] = 'т')) and (output = '') then
    begin
      output := sentence[i] + ' встретилось раньше';
    end
    else
      i += 1;
  end;
  writeln(output);
end.
