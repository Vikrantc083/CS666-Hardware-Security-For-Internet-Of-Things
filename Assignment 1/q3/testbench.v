`include "design.v"  

module testbench;

    reg clk,rst;

    wire [3:0]q;

    jc obj(clk,rst,q);

    initial
        clk = 0;
    always
      #5 clk = ~clk;
      

    initial
       begin
         #0 rst =1;
         #10 rst =0;
         #220 $finish;
       end

       initial
        begin 
        $dumpfile("example.vcd");
        $dumpvars(0,testbench);
        $monitor("time=%t,rst=%b,clk=%b,q=%b",$time,rst,clk,q);
        end
endmodule