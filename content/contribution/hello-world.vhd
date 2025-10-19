library ieee;
use ieee.std_logic_1164.all;
use std.textio.all;
entity hello_world is end;
architecture tb of hello_world is
begin
  process
    variable l : line;
  begin
    write(l, string'("Hello, World!"));
    writeline(output, l);
    wait;
  end process;
end tb;
