unit Lenght;
interface

function len(str: string): integer;
function len_arr(arr: array of integer): integer;

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

function len_arr(arr: array of integer): integer;
var 
  i: integer;
begin    
  Result := 0;
  for i := 0 to High(arr) do
    Result += 1;
end;

end.