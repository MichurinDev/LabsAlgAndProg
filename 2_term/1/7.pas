//Генерация паролей. Напишите программу для генерации всех возможных паролей 
//фиксированной длины из заданного набора символов. Учитывайте возможность 
//использования заглавных и строчных букв, цифр и специальных символов.
  
var
  alph: string;
  password: array of char;
  n: integer;

procedure GeneratePasswords(currentLength: integer);
var
  i: integer;
begin
  if currentLength = n then
    writeln(String.Join('', password))
  else begin
    for i := 1 to Length(alph) do begin
      password[currentLength] := alph[i];
      GeneratePasswords(currentLength + 1);
    end;
  end;
end;

begin
  write('Введите длину пароля: ');
  readln(n);
  write('Введите набор символов: ');
  readln(alph);

  SetLength(password, n);
  GeneratePasswords(0);
end.
