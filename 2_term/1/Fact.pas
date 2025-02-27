unit Fact;
interface

function factor(n: integer): longint;

implementation

function factor(n: integer): longint;
begin
    if n = 0 then factor := 1
    else
      factor := n * factor(n-1)
end;

end.