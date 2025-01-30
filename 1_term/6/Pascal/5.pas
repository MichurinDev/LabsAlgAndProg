//Разработайте функцию, которая принимает список чисел в качестве аргумента. 
//Она должна вычислить количество этих чисел, сумму всех чисел в списке и 
//вернуть это значение.

uses Lenght;

var arr: array of Integer;

function f(l: array of integer): (integer, integer);
begin
    var count: integer;
    var sum_nums: integer;
    var i: integer;

    count := 0;
    sum_nums := 0;

    for i := 0 to len_arr(l)-1 do begin
        count += 1;
        sum_nums += l[i];
    end;
    
    Result := (count, sum_nums);
end;

function f_rec(l: array of integer): (integer, integer);
begin
  var count: integer;
  var sum_nums: integer;

  if len_arr(l) = 1 then
    Result := (1, l[0])
  else begin
    count := f_rec(l[1:])[0];
    sum_nums := f_rec(l[1:])[1];
  
    count += 1;
    sum_nums += l[0];
    
    Result := (count, sum_nums)
  end;
end;

begin
  SetLength(arr, 7);
  arr[0] := 5;
  arr[1] := 2;
  arr[2] := 3;
  arr[3] := 7;
  arr[4] := 1;
  arr[5] := 6;
  arr[6] := 8;

  writeln(f(arr));
  writeln('---');
  writeln(f_rec(arr));

end.