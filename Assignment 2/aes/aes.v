`include "aes_key_expand.v"
//`include "xor1.v"
`include "fbfa.v"

module aes(clk,pt,key,ct);

input clk,rst;
input [127:0] pt,key;
output  [127:0] ct;

wire [127:0] key0,key1,key2,key3,key4,key5,key6,key7,key8,key9,key10;
wire [127:0] keyi [0:9]; // 128 bit ka 11 keys

wire [127:0] s [0:10]; //state matrix
wire [3:0] t [0:10];  //intermediate taar
assign t[0]=4'b0001;

wire Co,Ci;
wire [3:0]D;
assign Ci = 1'b0;
assign D= 4'b0001;

aes_key_expand_128 a0(clk,key,key0,key1,key2,key3,key4,key5,key6,key7,key8,key9,key10);
xor1 x1 (s[0],pt,key0); //round 0 (ans in state0 wire)

assign keyi[0]=key1, keyi[1]=key2, keyi[2]=key3, keyi[3]=key4, keyi[4]=key5, keyi[5]=key6, keyi[6]=key7, keyi[7]=key8, keyi[8]=key9, keyi[9]=key10;

genvar i;
generate
for (i = 0;i <10;i=i+1) 
    begin 
        fbfa w1(t[i+1],Co,t[i],D,Ci); //fbfa(S,Co,A,B,Ci);
        round r1(clk,s[i],keyi[i],s[i+1],t[i]);  //round(clk,data_in,key_in,data_out,taar);
    end
endgenerate

assign ct=s[10];
endmodule