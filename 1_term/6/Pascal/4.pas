uses Lenght;

function LengthOfList(arr: array of Integer): Integer;
var
  count, i: Integer;
begin
  count := 0;
  for i := 0 to len_arr(arr) do
    count += 1;
  Result := count;
end;

function FindMax(arr: array of Integer): Integer;
var
  maxNum, i: Integer;
begin
  maxNum := arr[0];
  for i := 1 to len_arr(arr) - 1 do
  begin
    if arr[i] > maxNum then
      maxNum := arr[i];
  end;
  Result := maxNum;
end;

function FindMaxRec(arr: array of Integer): Integer;
begin
  if len_arr(arr) = 1 then
    Result := arr[0]
  else begin
    if arr[0] > FindMaxRec(arr[2:]) then
      Result := arr[0]
    else 
      Result := FindMaxRec(arr[2:]);
  end;
end;

var
  arr: array of Integer;
  maxVal, maxValRec: Integer;
begin
  SetLength(arr, 7);
  arr[0] := 5;
  arr[1] := 2;
  arr[2] := 3;
  arr[3] := 7;
  arr[4] := 1;
  arr[5] := 6;
  arr[6] := 8;

  maxVal := FindMax(arr);
  maxValRec := FindMaxRec(arr);

  WriteLn(maxVal);
  WriteLn('---');
  WriteLn(maxValRec);
end.