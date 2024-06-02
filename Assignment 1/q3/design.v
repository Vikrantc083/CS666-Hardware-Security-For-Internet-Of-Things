module jc(clk,rst,q);
  input clk,rst;
  output [3:0]q;

  // initiate 4 D-FF
  dff df1(q[0],~q[3],clk,rst);
  dff df2(q[1],q[0],clk,rst);
  dff df3(q[2],q[1],clk,rst);
  dff df4(q[3],q[2],clk,rst);
endmodule

module dff(q,d,clk,rst);
  input d,clk,rst;
  output q;
  
  reg q; // need memory, as sequential needs memory

  always @(posedge clk)
   begin
    if(rst) q=1'b0;
    else q=d;
   end
endmodule   