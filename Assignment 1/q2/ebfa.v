// ebfa: eight bit full adder (design file)

`include "obfa.v"  

module ebfa(S,Co,A,B,Ci);

    input [7:0]A,B;
    input Ci;

    output [7:0]S;
    output Co;
     
    wire [6:0]C;

    obfa fa0 (S[0],C[0],A[0],B[0],Ci);
    obfa fa1 (S[1],C[1],A[1],B[1],C[0]);
    obfa fa2 (S[2],C[2],A[2],B[2],C[1]);
    obfa fa3 (S[3],C[3],A[3],B[3],C[2]);
    obfa fa4 (S[4],C[4],A[4],B[4],C[3]);
    obfa fa5 (S[5],C[5],A[5],B[5],C[4]);
    obfa fa6 (S[6],C[6],A[6],B[6],C[5]);
    obfa fa7 (S[7],Co,A[7],B[7],C[6]);

endmodule    


