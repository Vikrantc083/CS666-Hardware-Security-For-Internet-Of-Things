`include "subbytes.v"
`include "shiftrows.v"
`include "mixcolumn.v"
`include "xor1.v"

module round(clk,data_in,key_in,data_out,taar);
input clk;
input [3:0]taar;
input [127:0]data_in,key_in;
output [127:0] data_out;

wire mux[3:0];
wire orr,orr1,orr2; // final or value in orr2
wire q1,q2,q3,q4;

wire [127:0]sub_data_out,shift_data_out,mix_data_out; 

    subbytes a1(clk,data_in,sub_data_out);
    shiftrows a2(clk,sub_data_out,shift_data_out);
    mixcolumn a3(clk,shift_data_out,mix_data_out);
    
    //1010 to be 0000
    not n1 (mux[1],taar[1]);
    not n2 (mux[3],taar[3]);
    assign mux[0] = taar[0];
    assign mux[2] =taar[2];

    or o1 (orr,mux[0],mux[1]);
    or o2 (orr1,orr,mux[2]);
    or o3 (orr2,orr1,mux[3]);
    
    wire ans[127:0];
    wire ans1[127:0];
    wire ans2[127:0];
    wire x;
    not nn1 (x,orr2);

    genvar i;
    for (i = 0;i <128;i=i+1) 
    begin 
        assign ans[i]=orr2;
        assign ans1[i]=x;
    end
 
    //ans[127:0] has our 0000 for 1010; now we apply mux;

    wire [127:0]newans;
    wire [127:0]newans1;
    wire [127:0]finalans;

     //128 bit and or operations.

    for (i = 0;i <128;i=i+1) 
    begin 
    and aa5 (newans[i],mix_data_out[i],ans[i]);
    end 

    for (i = 0;i <128;i=i+1) 
    begin 
    and aa6 (newans1[i],shift_data_out[i],ans1[i]);
    end 

    for (i = 0;i <128;i=i+1) 
    begin 
    or  oo3(finalans[i],newans[i],newans1[i]);
    end

    
    xor1 gw1 (data_out,finalans,key_in);

endmodule