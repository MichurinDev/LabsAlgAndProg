unit StringForSymbs;
interface
  function generate_string(symbol: Char; count: Integer): string;
  
  implementation
  
  function generate_string(symbol: Char; count: Integer): string;
  var
    str: string;
    i: integer;
  begin
   while i <> count do begin
     str += symbol;
     i += 1;
   end;
   Result := str;
  end;
end.