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

function BubbleSort(arr: Array of integer): Array of integer;
var i, j, temp: integer;
begin
  for i := 0 to High(arr)-1 do begin
    for j := i+1 to High(arr) do begin
      if (arr[i] > arr[j]) and (arr[i] mod 2 = 0) and (arr[j] mod 2 = 0)  then begin
        temp := arr[j];
        arr[j] := arr[i];
        arr[i] := temp;
      end;
    end;
  end;
  Result := arr;
end;

begin
  var origin: Array of integer;
  origin := GetRandomArr(10);
  writeln(origin);
  writeln(BubbleSort(origin));  
end.