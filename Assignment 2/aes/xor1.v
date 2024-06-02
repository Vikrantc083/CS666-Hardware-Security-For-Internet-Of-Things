module xor1(op,a,b);

    input [127:0] a,b;
    output [127:0] op;

    assign op = a^b;

endmodule