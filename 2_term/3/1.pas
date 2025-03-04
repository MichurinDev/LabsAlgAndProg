function GetRandomArr(l: integer): Array of integer;
var
  i: integer;
  output:Array of integer;

begin
  Randomize;
  SetLength(output, l);
  
  for i := 0 to High(output) do begin
    output[i] := Random(100);
  end;
  
  Result := output;
end;


function BubleSort(arr: Array of integer): Array of integer;
var
  i, j, k: integer;

begin
  for i := 0 to High(arr)-1 do
    for j := i+1 to High(arr) do begin
      if (arr[i] > arr[j]) then begin
        k := arr[j];
        arr[j] := arr[i];
        arr[i] := k;
      end;
    end;
  
  Result := arr;
end;

function QuickSort(arr: Array of integer; left, right: integer): array of integer;
var i, j, pivot, temp: integer;
begin
  if left >= right then Result := arr;

  i := left;
  j := right;
  pivot := arr[(left + right) div 2];

  repeat
    while arr[i] < pivot do i += 1;
    while arr[j] > pivot do j -= 1;

    if i <= j then begin
      temp := arr[i];
      arr[i] := arr[j];
      arr[j] := temp;
      i += 1;
      j -= 1;
    end;
  until i > j;

  if left < j then QuickSort(arr, left, j);
  if i < right then QuickSort(arr, i, right);

  Result := arr;
end;

function SelectionSort(arr: array of integer): array of integer;
var
  i, j, temp, min_idx: integer;
begin
  for i := 0 to High(arr) do begin
    min_idx := i;
    for j := i + 1 to High(arr) do
        if arr[j] < arr[min_idx] then min_idx := j;

    temp := arr[i];
    arr[i] := arr[min_idx];
    arr[min_idx] := temp;
  end;

  Result := arr;
end;

begin
  var origin: Array of integer;
  origin := GetRandomArr(10);
  writeln('Исходный массив:        ', origin);
  writeln('Пузырьковая сортировка: ', BubleSort(origin));
  writeln('Быстрая сортировка:     ', QuickSort(origin, 1, High(origin)));
  writeln('Сортировка выбором:     ', SelectionSort(origin));
end.