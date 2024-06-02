`include "mlp.v"  

module testbench;

    reg [3:0]A,B; // i/p's in reg

    wire [7:0]M;  // o/p's in wire

    mlp obj (M,A,B);

    initial 
    begin
    A=11;
    B=15;
    $monitor("A=%d, B=%d, AxB =%d",A,B,M);
    end

endmodule    
