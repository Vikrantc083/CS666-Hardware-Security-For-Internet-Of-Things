`include "aes.v"

module aes_test;

reg clk,rst;
reg [127:0]pt,key;
wire [127:0]ct;
aes a1(clk,pt,key,ct);  // aes_main(clk,data_in,key,data_out);

initial
        clk = 0;
    always
      #5 clk = ~clk;   

initial 
begin
    
    //#0 pt =272591435686934902924926950097051405367;
    //#0 key=240053983285614976113571109108609834581;

    //#0 pt= 128'hcd13336b62440faf9d2ca82225f34c37;
    //#0 key=128'hb498b728e7d54351380cf0af2dd1de55;

    //#0 pt= 128'h01234567890123456789012345678901;
    //#0 key=128'h00000000009876543210987654321098;

    #0 pt= 128'h54776F204F6E65204E696E652054776F;
    #0 key=128'h5468617473206D79204B756E67204675;
    
    #4 rst=1;
    #15 rst=0;
    #800 $finish;

    // Answer in hex (ciphertext): E92862385C8BF11EA8702D252003FA9A
    

end
initial 
begin
    $dumpfile("aestest.vcd");
    $dumpvars(0,aes_test);
    $monitor("time=%d,%d,cipher_text in hexadecimal =%h",$time,clk,ct);
end
endmodule