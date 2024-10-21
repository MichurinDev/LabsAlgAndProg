program f3;

var
  s, new_s, word, sentence, s1, s2: string;
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
  WriteLn('Задача 4');
  Write('Введите предложение: ');
  ReadLn(sentence);
  Write('Введите первый символ: ');
  ReadLn(s1);
  Write('Введите второй символ: ');
  ReadLn(s2);

  WriteLn('Вхождения символа ', s1);
  for word in sentence.Split([' ']) do
    if Pos(s1, word) > 0 then
      WriteLn(word);

  WriteLn;
  WriteLn('Вхождения символа ', s2);
  for word in sentence.Split([' ']) do
    if Pos(s2, word) > 0 then
      WriteLn(word);

  // Задача 5
  WriteLn;
  WriteLn('Задача 5');
  Write('Введите предложение: ');
  ReadLn(sentence);
  WriteLn(Length(sentence) - Length(StringReplace(sentence, ' ', '', [rfReplaceAll])));

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

