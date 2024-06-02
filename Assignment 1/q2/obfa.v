// obfa: one bit full adder (design file)

module obfa(S,Co,A,B,Ci);   
    input A,B,Ci;
    output S,Co;
    
    wire x1,x2;
    xor xo1(x1,A,B);
    xor xo2(x2,x1,Ci);  // Sum = A ^ B ^ C; 

    wire a1,a2,a3,o1;

    and a_1(a1,A,B);
    and a_2(a2,B,Ci);
    and a_3(a3,Ci,A);  
    or o_1 (o1,a1,a2,a3);    //Co=(A&B) | (B&Ci) | (Ci&A);

    assign S= x2;
    assign Co=o1;
    
endmodule