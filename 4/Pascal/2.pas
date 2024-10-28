program f2;

uses lenght;

var
  word: string;
  index, m, n: Integer;

begin
  // Задача 1
  WriteLn('Задача 1');
  Write('Введите слово: ');
  ReadLn(word);
  WriteLn(word[3]);

  // Задача 2
  WriteLn('Задача 2');
  Write('Введите слово: ');
  ReadLn(word);
  Write('Введите номер символа: ');
  ReadLn(index);
  WriteLn(word[index]);

  // Задача 3
  WriteLn('Задача 3');
  Write('Введите слово: ');
  ReadLn(word);
  word := LowerCase(word);
  WriteLn(word[1] = word[Length(word)]);

  // Задача 4
  WriteLn('Задача 4');
  Write('Введите слово: ');
  ReadLn(word);
  WriteLn(word[2] + word[4]);

  // Задача 5
  WriteLn('Задача 5');
  Write('Введите слово: ');
  ReadLn(word);
  WriteLn(Copy(word, 2, 3));

  // Задача 6
  WriteLn('Задача 6');
  Write('Введите слово: ');
  ReadLn(word);
  WriteLn(Copy(word, 1, len(word) div 2));

  // Задача 7
  WriteLn('Задача 7');
  Write('Введите слово: ');
  ReadLn(word);
  Write('Начало: ');
  ReadLn(m);
  Write('Конец: ');
  ReadLn(n);
  WriteLn(Copy(word, m, n));
end.

