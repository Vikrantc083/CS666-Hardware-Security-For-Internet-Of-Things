// fbfa: four bit full adder (design file)

`include "obfa.v"  

module fbfa(S,Co,A,B,Ci);

    input [3:0]A,B;
    input Ci;

    output [3:0]S;
    output Co;
     
    wire [2:0]C;

    obfa fa0 (S[0],C[0],A[0],B[0],Ci);
    obfa fa1 (S[1],C[1],A[1],B[1],C[0]);
    obfa fa2 (S[2],C[2],A[2],B[2],C[1]);
    obfa fa3 (S[3],Co,A[3],B[3],C[2]);
   

endmodule    


