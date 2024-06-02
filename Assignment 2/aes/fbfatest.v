`include "fbfa.v"  

module testbench;

    reg [3:0]A,B;
    reg Ci;          // i/p's in reg

    wire [3:0]S,C;
    wire Co;         // o/p's in wire

    fbfa obj (S,Co,A,B,Ci);

    initial 
    begin
    A=4'b1001;
    B=4'b0001;
    Ci=0;

    $monitor("A=%d, B=%d, S=%b, Co=%b",A,B,S,Co);
    end

endmodule    
