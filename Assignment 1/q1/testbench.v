`include "ebfa.v"  

module testbench;

    reg [7:0]A,B;
    reg Ci;          // i/p's in reg

    wire [7:0]S,C;
    wire Co;         // o/p's in wire

    ebfa obj (S,Co,A,B,Ci);

    initial 
    begin
    A=128;
    B=12;
    Ci=0;

    $monitor("A=%d, B=%d, S=%d, Co=%b",A,B,S,Co);
    end

endmodule    
