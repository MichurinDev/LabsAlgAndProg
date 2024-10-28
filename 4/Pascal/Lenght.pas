unit Lenght;
interface

function len(str: string): integer;

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

end.