unit Lenght;
interface

function len(str: string): integer;
function len_arr(arr: array of string): integer;

implementation

function len(str: string): integer;
  var 
    i: integer;
    s: string;
  
  begin    
    i := 1;
    while s <> str do
      begin
      s += str[i];
      i += 1
    end;
  Result := i - 1;
end;

function len_arr(arr: array of string): integer;
var 
  i: integer;
begin    
  Result := 0;
  for i := 0 to High(arr) do begin
    Result += 1;
  end;
end;

end.