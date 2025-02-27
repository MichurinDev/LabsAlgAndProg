program f3;

uses Lenght;

var
  s, new_s, word, sentence, s1, s2, temp_str: string;
  i, counter: Integer;

begin
  // Задача 1
  WriteLn('Задача 1');
  Write('Введите слово: ');
  ReadLn(s);
  new_s := '';

  for i := Length(s) downto 1 do
    new_s := new_s + s[i];

  WriteLn(new_s);

  // Задача 2
  WriteLn('Задача 2');
  Write('Введите слово: ');
  ReadLn(word);
  WriteLn(StringOfChar('*', Length(word)) + word + StringOfChar('*', Length(word)));

  // Задача 3
  WriteLn;
  WriteLn('Задача 3');
  Write('Введите слово: ');
  ReadLn(word);

  for i := 2 to Length(word) do
    if (i mod 3 = 2) then
      WriteLn(word[i]);

  // Задача 4
  WriteLn;
  writeln('Задача 4');
  write('Введите предложение: ');
  readln(sentence);
  
  write('Введите первый символ: ');
  readln(s1);
  
  write('Введите второй символ: ');
  readln(s2);
  
  writeln('Вхождения символа ', s1);
  temp_str := '';
  
  for i := 1 to len(sentence) do
  begin
    if sentence[i] = ' ' then
    begin
      if Pos(s1, temp_str) > 0 then
        writeln(temp_str);
      temp_str := '';
    end
    else
      temp_str := temp_str + sentence[i];
  end;
  
  // Проверка последнего слова
  if Pos(s1, temp_str) > 0 then
    writeln(temp_str);

  writeln;
  writeln('Вхождения символа ', s2);
  
  temp_str := '';
  
  for i := 1 to length(sentence) do
  begin
    if sentence[i] = ' ' then
    begin
      if Pos(s2, temp_str) > 0 then
        writeln(temp_str);
      temp_str := '';
    end
    else
      temp_str := temp_str + sentence[i];
  end;

  // Проверка последнего слова
  if Pos(s2, temp_str) > 0 then
    writeln(temp_str);

  // Задача 5
  WriteLn;
  WriteLn('Задача 5');
  WriteLn('Введите предложение: ');
  ReadLn(sentence);
  
  counter := 0;

  for i := 1 to len(sentence) do
  begin
    if sentence[i] = ' ' then
      counter := counter + 1;
  end;

  WriteLn('Количество пробелов: ', counter);

  // Задача 6
  WriteLn;
  WriteLn('Задача 6');
  Write('Введите предложение: ');
  ReadLn(sentence);
  counter := 0;

  for i := 1 to Length(sentence) - 1 do
    if sentence[i] = sentence[i + 1] then
      counter := counter + 1;

  WriteLn(counter);
end.

