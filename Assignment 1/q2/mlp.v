// 8 bit multiplier

`include "ebfa.v"  

module mlp(M,A,B);

    input [3:0]A,B;
    output [7:0]M; //final output **
    
    wire ci1=1'b0; //initial carry in 0 

    
    wire [0:0] E[3:0][7:0];  //4*8 matrix

    genvar i; 

    generate
    for(i=0;i<8;i=i+1)
        begin
            if(i<4)
            begin
                assign E[0][i]=A[i]&&B[0];
            end
            else
            begin
                assign E[0][i]=0;
            end
        
            if(i>0 && i<5)
            begin
                assign E[1][i]=A[i-1]&&B[1];
            end
            else
            begin
                assign E[1][i]=0;
            end

            if(i>1 && i<6)
            begin 
                 assign E[2][i]=A[i-2]&&B[2];
            end
            else 
            begin
                assign E[2][i]=0;
            end

            if(i>2 && i<7)
            begin
                assign E[3][i]=A[i-3]&&B[3];
            end
            else
            begin 
                assign E[3][i]=0;
            end

        end
    endgenerate


    wire [7:0]S4,S5; //intermediate results
    wire [7:0]C4,C5; //intermediate carry

     generate
        for (i=0;i<8;i=i+1)
        begin
            if(i!=0)
            begin
                obfa a1(S4[i],C4[i],E[0][i],E[1][i],C4[i-1]);  //obfa(S,Co,A,B,Ci);
            end
            else
            begin
                obfa a2(S4[i],C4[i],E[0][i],E[1][i],ci1); 
            end 
        end
    endgenerate

    generate
        for (i=0;i<8;i=i+1)
        begin
            if(i!=0)
            begin
                obfa a1(S5[i],C5[i],E[2][i],E[3][i],C5[i-1]);  //obfa(S,Co,A,B,Ci);
            end
            else
            begin
                obfa a2(S5[i],C5[i],E[2][i],E[3][i],ci1); 
            end 
        end
    endgenerate

    ebfa fa0 (M,co1,S4,S5,C5[7]); // ebfa(S,Co,A,B,Ci)

endmodule