`include "aes_key_expand.v"
`include "xor1.v"

module aes(clk,pt,key,ct);

input clk,rst;
input [127:0] pt,key;
output  [127:0] ct;

wire [3:0]t1,t2,t3,t4,t5,t6,t7,t8,t9,t10;

wire [127:0] key0,key1,key2,key3,key4,key5,key6,key7,key8,key9,key10;
wire [127:0] s0,s1,s2,s3,s4,s5,s6,s7,s8,s9,s10;

xor1 x1 (s0,pt,key0); //round 0 (ans in state0 wire)

aes_key_expand_128 a0(clk,key,key0,key1,key2,key3,key4,key5,key6,key7,key8,key9,key10);
           
assign t1=4'b0001;
round r1(clk,s0,key1,s1,t1); 

assign t2=4'b0010;  
round r2(clk,s1,key2,s2,t2);

assign t3=4'b0011;  
round r3(clk,s2,key3,s3,t3);

assign t4=4'b0100;    
round r4(clk,s3,key4,s4,t4);

assign t5=4'b0101;  
round r5(clk,s4,key5,s5,t5); 

assign t6=4'b0110;  
round r6(clk,s5,key6,s6,t6);

assign t7=4'b0111;  
round r7(clk,s6,key7,s7,t7);  

assign t8=4'b1000;  
round r8(clk,s7,key8,s8,t8);

assign t9=4'b1001;  
round r9(clk,s8,key9,s9,t9);  

assign t10=4'b1010;  
round r10(clk,s9,key10,s10,t10); 

assign ct=s10;
endmodule