import itertools
def putinmatrixcm(a):                            #placing into matrix in column major form
    def transpose_matrix(matrix):                #converting from row major to column major
        transposed_matrix = [[matrix[j][i] for j in range(4)] for i in range(4)]
        return transposed_matrix
    r=0    
    c=[]
    ans1=[]
    for i in range(0,len(a)-7,8):
        for j in range(8):
            c.append(int(a[i+j]))
        ans1.append(c)
        c=[]
        
    ans=[] 
    x=[]
    for i in range(0,len(ans1)-3,4):
        for j in range(4):
            x.append(ans1[i+j])
        ans.append(x)
        x=[]
        
    return(transpose_matrix(ans)) 

ct="10110010000111101110101101110011100101010011111001111010001001110111000111011011001000100010111011001011111011101010011110001000"
fct="00110011110011110110000000010100000111111101001011110001001000011111111110011010011000010010011011111110111111010000001111100110"

ct1="00001100101010111110001111101001100110001000110101100110011001101010100101101010001110011110011110110110010110011100101010010001"
fct1="10010010001100010111101110001010100111100010010011110001100101100000111100110111001110000101101001000000100001011011000011010101"

ct=putinmatrixcm(ct)
fct=putinmatrixcm(fct)

ct1=putinmatrixcm(ct1)
fct1=putinmatrixcm(fct1)

def batoi(by):  
    byt=[]
    for i in range(len(by[0])):
        byt.append(int(by[0][i]))                                     #Binary array to int 
    byt=byt[::-1]
    intt=0
    for i in range(len(byt)):
        intt=intt+(int(byt[i])*(2**i))
    return(intt) 
    
def inter(arr1, arr2, arr3, arr4):                      #intersection
    set1 = set(arr1)
    set2 = set(arr2)
    set3 = set(arr3)
    set4 = set(arr4)
    intersection = set1.intersection(set2, set3, set4)
    return list(intersection)

def bxa(arr1, arr2):                                   #bxa:bitwise_xor_array
    result = [a ^ b for a, b in zip(arr1, arr2)]
    return result

def i_sbox(byt):                                       #i_sbox: inverse_Sbox
    byt=byt[::-1]
    intt=0
    for i in range(len(byt)):
        intt=intt+(byt[i]*(2**i))
    byte=intt    
    
    sbox = [
        0x52, 0x09, 0x6a, 0xd5, 0x30, 0x36, 0xa5, 0x38, 0xbf, 0x40, 0xa3, 0x9e, 0x81, 0xf3, 0xd7, 0xfb,
        0x7c, 0xe3, 0x39, 0x82, 0x9b, 0x2f, 0xff, 0x87, 0x34, 0x8e, 0x43, 0x44, 0xc4, 0xde, 0xe9, 0xcb,
        0x54, 0x7b, 0x94, 0x32, 0xa6, 0xc2, 0x23, 0x3d, 0xee, 0x4c, 0x95, 0x0b, 0x42, 0xfa, 0xc3, 0x4e,
        0x08, 0x2e, 0xa1, 0x66, 0x28, 0xd9, 0x24, 0xb2, 0x76, 0x5b, 0xa2, 0x49, 0x6d, 0x8b, 0xd1, 0x25,
        0x72, 0xf8, 0xf6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xd4, 0xa4, 0x5c, 0xcc, 0x5d, 0x65, 0xb6, 0x92,
        0x6c, 0x70, 0x48, 0x50, 0xfd, 0xed, 0xb9, 0xda, 0x5e, 0x15, 0x46, 0x57, 0xa7, 0x8d, 0x9d, 0x84,
        0x90, 0xd8, 0xab, 0x00, 0x8c, 0xbc, 0xd3, 0x0a, 0xf7, 0xe4, 0x58, 0x05, 0xb8, 0xb3, 0x45, 0x06,
        0xd0, 0x2c, 0x1e, 0x8f, 0xca, 0x3f, 0x0f, 0x02, 0xc1, 0xaf, 0xbd, 0x03, 0x01, 0x13, 0x8a, 0x6b,
        0x3a, 0x91, 0x11, 0x41, 0x4f, 0x67, 0xdc, 0xea, 0x97, 0xf2, 0xcf, 0xce, 0xf0, 0xb4, 0xe6, 0x73,
        0x96, 0xac, 0x74, 0x22, 0xe7, 0xad, 0x35, 0x85, 0xe2, 0xf9, 0x37, 0xe8, 0x1c, 0x75, 0xdf, 0x6e,
        0x47, 0xf1, 0x1a, 0x71, 0x1d, 0x29, 0xc5, 0x89, 0x6f, 0xb7, 0x62, 0x0e, 0xaa, 0x18, 0xbe, 0x1b,
        0xfc, 0x56, 0x3e, 0x4b, 0xc6, 0xd2, 0x79, 0x20, 0x9a, 0xdb, 0xc0, 0xfe, 0x78, 0xcd, 0x5a, 0xf4,
        0x1f, 0xdd, 0xa8, 0x33, 0x88, 0x07, 0xc7, 0x31, 0xb1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xec, 0x5f,
        0x60, 0x51, 0x7f, 0xa9, 0x19, 0xb5, 0x4a, 0x0d, 0x2d, 0xe5, 0x7a, 0x9f, 0x93, 0xc9, 0x9c, 0xef,
        0xa0, 0xe0, 0x3b, 0x4d, 0xae, 0x2a, 0xf5, 0xb0, 0xc8, 0xeb, 0xbb, 0x3c, 0x83, 0x53, 0x99, 0x61,
        0x17, 0x2b, 0x04, 0x7e, 0xba, 0x77, 0xd6, 0x26, 0xe1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0c, 0x7d
    ]

    x=list(bin(sbox[byte]))
    x.pop(0)
    x.pop(0)
    if(len(x)<8):
        for i in range(8-len(x)):
            x=x[::-1]
            x.append(0)
            x=x[::-1]
    for i in range(len(x)):
        x[i]=int(x[i])
    return(x)

def m_h_GF2p8(hex1, hex2):                             #GF(2^8) multiplication
    def m_GF2p8(poly1, poly2, modulus):
        product = 0
        while poly2 > 0:
            if poly2 & 1:
                product ^= poly1 
            poly1 <<= 1
            if poly1 & (1 << 8):
                poly1 ^= modulus
            poly2 >>= 1
        return product

    def hex_to_int(hex_string):
        return int(hex_string, 16)
    
    def int_to_hex(num):
        return hex(num)[2:]
        
    hex1=hex1[::-1]
    intt=0
    for i in range(len(hex1)):
        intt=intt+(hex1[i]*(2**i))
    poly1=intt 
    
    
    hex2=hex2[::-1]
    intt1=0
    for i in range(len(hex2)):
        intt1=intt1+(hex2[i]*(2**i))
    poly2=intt1 
    
    # Define the irreducible polynomial x^8 + x^4 + x^3 + x + 1
    modulus = hex_to_int("11B")
    # Perform multiplication in GF(2^8)
    product = m_GF2p8(poly1, poly2, modulus)
    # Convert the result back to hexadecimal
    result_hex = int_to_hex(product)

    return result_hex

keylist = list(itertools.product([0, 1], repeat=8))
#print(len(keylist))

k00=[] #
k00_1=[] #
k00_2=[] #

k13=[]  #
k13_1=[] #
k13_2=[] #

k22=[] #
k22_1=[] #
k22_2=[]

k31=[] #
k31_1=[] #
k31_2=[] #

print()
print("***********************************************************************************")
print(" *****  Evaluation of step wise key-space reduction of target Bytes  *****  ")
print(" *****  No. of potential keys in respective positions  ***** ")
print("***********************************************************************************")
print()
print("Initially 2^8 keys possible for every Byte: k00: 256 |*|  k13: 256 |*| k22: 256 |*| k31: 256")
print()
print("***********************************************************************************")
print()

for i in range(len(keylist)):                                             #EQN_1 (k00)
    for j in range(len(keylist)):
        f1= m_h_GF2p8(bxa(i_sbox(bxa(ct[0][0],keylist[i])),i_sbox(bxa(fct[0][0],keylist[i]))),[0,0,0,0,0,0,0,1])
        f2= m_h_GF2p8(bxa(i_sbox(bxa(ct[1][3],keylist[j])),i_sbox(bxa(fct[1][3],keylist[j]))),[0,0,0,0,0,0,1,0])
        if(f1==f2):
            k00.append(keylist[i])
            k13.append(keylist[j])

k00=list(set(k00)) 
k13=list(set(k13))      
print("After Eqn 1: k00:",len(k00)," |*|  k13:",len(k13)," |*| k22: 256 |*| k31: 256")
print()
print("***********************************************************************************")
print()
#print("k00=",len(k00),"k13=",len(k13))            

for i in range(len(k00)):                                                  #EQN_2 (k00)
    for j in range(len(keylist)):
        f1= m_h_GF2p8(bxa(i_sbox(bxa(ct[0][0],k00[i])),i_sbox(bxa(fct[0][0],k00[i]))),[0,0,0,0,0,0,0,1])
        f2= m_h_GF2p8(bxa(i_sbox(bxa(ct[2][2],keylist[j])),i_sbox(bxa(fct[2][2],keylist[j]))),[0,0,0,0,0,0,1,0])
        #print(f1,f2)
        if(f1==f2):
            k00_1.append(k00[i])
            k22.append(keylist[j])

k00_1=list(set(k00_1)) 
k22=list(set(k22))             
print("After Eqn 2: k00:",len(k00_1)," |*|  k13:",len(k13)," |*| k22:",len(k22)," |*| k31: 256")
print()
print("***********************************************************************************")
print()
#print("k00_1=",len(k00_1),"k22=",len(k22))    

for i in range(len(k00_1)):                                                #EQN_3 (k00)
    for j in range(len(keylist)):
        f1= m_h_GF2p8(bxa(i_sbox(bxa(ct[0][0],k00_1[i])),i_sbox(bxa(fct[0][0],k00_1[i]))),[0,0,0,0,0,0,1,1])
        f2= m_h_GF2p8(bxa(i_sbox(bxa(ct[3][1],keylist[j])),i_sbox(bxa(fct[3][1],keylist[j]))),[0,0,0,0,0,0,1,0])
        #print(f1,f2)
        if(f1==f2):
            k00_2.append(k00_1[i])
            k31.append(keylist[j])

k00_2=list(set(k00_2)) 
k31=list(set(k31))              
print("After Eqn 3: k00:",len(k00_2)," |*|  k13:",len(k13)," |*| k22:",len(k22)," |*| k31:",len(k31))
print()
print("***********************************************************************************")
print()   
#print("k00_2=",len(k00_2),"k31=",len(k31)) 

for i in range(len(k13)):                                                  #EQN_4 (k13)
    for j in range(len(k22)):
        f1= m_h_GF2p8(bxa(i_sbox(bxa(ct[1][3],k13[i])),i_sbox(bxa(fct[1][3],k13[i]))),[0,0,0,0,0,0,0,1])
        f2= m_h_GF2p8(bxa(i_sbox(bxa(ct[2][2],k22[j])),i_sbox(bxa(fct[2][2],k22[j]))),[0,0,0,0,0,0,0,1])
        #print(f1,f2)
        if(f1==f2):
            k13_1.append(k13[i])
            k22_1.append(k22[j])

k13_1=list(set(k13_1)) 
k22_1=list(set(k22_1))       
print("After Eqn 4: k00:",len(k00_2)," |*|  k13:",len(k13_1)," |*| k22:",len(k22_1)," |*| k31:",len(k31))
print()
print("***********************************************************************************")
print()             
#print("k13_1=",len(k13_1),"k22_1=",len(k22_1)) 

for i in range(len(k13_1)):                                                  #EQN_5 (k13)
    for j in range(len(k31)):
        f1= m_h_GF2p8(bxa(i_sbox(bxa(ct[1][3],k13_1[i])),i_sbox(bxa(fct[1][3],k13_1[i]))),[0,0,0,0,0,0,1,1])
        f2= m_h_GF2p8(bxa(i_sbox(bxa(ct[3][1],k31[j])),i_sbox(bxa(fct[3][1],k31[j]))),[0,0,0,0,0,0,0,1])
        #print(f1,f2)
        if(f1==f2):
            k13_2.append(k13_1[i])
            k31_1.append(k31[j])

k13_2=list(set(k13_2)) 
k31_1=list(set(k31_1))                
print("After Eqn 5: k00:",len(k00_2)," |*|  k13:",len(k13_2)," |*| k22:",len(k22_1)," |*| k31:",len(k31_1))
print()
print("***********************************************************************************")
print() 
#print("k13_2=",len(k13_2),"k31_1=",len(k31_1))

for i in range(len(k22_1)):                                                  #EQN_6 (k22)
    for j in range(len(k31_1)):
        f1= m_h_GF2p8(bxa(i_sbox(bxa(ct[2][2],k22_1[i])),i_sbox(bxa(fct[2][2],k22_1[i]))),[0,0,0,0,0,0,1,1])
        f2= m_h_GF2p8(bxa(i_sbox(bxa(ct[3][1],k31_1[j])),i_sbox(bxa(fct[3][1],k31_1[j]))),[0,0,0,0,0,0,0,1])
        #print(f1,f2)
        if(f1==f2):
            k22_2.append(k22_1[i])
            k31_2.append(k31_1[j])

k22_2=list(set(k22_2)) 
k31_2=list(set(k31_2))                 
print("After Eqn 6: k00:",len(k00_2)," |*|  k13:",len(k13_2)," |*| k22:",len(k22_2)," |*| k31:",len(k31_2))
print()
print("***********************************************************************************")
print() 
#print("k22_2=",len(k22_2),"k31_2=",len(k31_2))


#SECOND CIPHER PAIR **************************************************************************
print(" *****  Second Iteration, with Correct & Faulty Ciphertext number 2 *****  ")
print()
print("***********************************************************************************")
print() 

k00_3=[] #
k00_4=[] #
k00_5=[] #

k13_3=[]  #
k13_4=[]  #
k13_5=[]  #

k22_3=[] #
k22_4=[] #
k22_5=[]

k31_3=[] #
k31_4=[] #
k31_5=[]

for i in range(len(k00_2)):                                             #EQN_1 (k00)
    for j in range(len(k13_2)):
        f1= m_h_GF2p8(bxa(i_sbox(bxa(ct1[0][0],k00_2[i])),i_sbox(bxa(fct1[0][0],k00_2[i]))),[0,0,0,0,0,0,0,1])
        f2= m_h_GF2p8(bxa(i_sbox(bxa(ct1[1][3],k13_2[j])),i_sbox(bxa(fct1[1][3],k13_2[j]))),[0,0,0,0,0,0,1,0])
        if(f1==f2):
            k00_3.append(k00_2[i])
            k13_3.append(k13_2[j])

k00_3=list(set(k00_3)) 
k13_3=list(set(k13_3))    
print("After Eqn 7: k00:",len(k00_3)," |*|  k13:",len(k13_3)," |*| k22:",len(k22_2)," |*| k31:",len(k31_2))
print()
print("***********************************************************************************")
print()        
#print("k00_3=",len(k00_3),"k13_3=",len(k13_3))            


for i in range(len(k00_3)):                                                  #EQN_2 (k00)
    for j in range(len(k22_2)):
        f1= m_h_GF2p8(bxa(i_sbox(bxa(ct1[0][0],k00_3[i])),i_sbox(bxa(fct1[0][0],k00_3[i]))),[0,0,0,0,0,0,0,1])
        f2= m_h_GF2p8(bxa(i_sbox(bxa(ct1[2][2],k22_2[j])),i_sbox(bxa(fct1[2][2],k22_2[j]))),[0,0,0,0,0,0,1,0])
        #print(f1,f2)
        if(f1==f2):
            k00_4.append(k00_3[i])
            k22_3.append(k22_2[j])

k00_4=list(set(k00_4)) 
k22_3=list(set(k22_3))     
print("After Eqn 8: k00:",len(k00_4)," |*|  k13:",len(k13_3)," |*| k22:",len(k22_3)," |*| k31:",len(k31_2))
print()
print("***********************************************************************************")
print()        
#print("k00_4=",len(k00_4),"k22_3=",len(k22_3))    


for i in range(len(k00_4)):                                                #EQN_3 (k00)
    for j in range(len(k31_2)):
        f1= m_h_GF2p8(bxa(i_sbox(bxa(ct1[0][0],k00_4[i])),i_sbox(bxa(fct1[0][0],k00_4[i]))),[0,0,0,0,0,0,1,1])
        f2= m_h_GF2p8(bxa(i_sbox(bxa(ct1[3][1],k31_2[j])),i_sbox(bxa(fct1[3][1],k31_2[j]))),[0,0,0,0,0,0,1,0])
        #print(f1,f2)
        if(f1==f2):
            k00_5.append(k00_4[i])
            k31_3.append(k31_2[j])

k00_5=list(set(k00_5)) 
k31_3=list(set(k31_3))      
print("After Eqn 9: k00:",len(k00_5)," |*|  k13:",len(k13_3)," |*| k22:",len(k22_3)," |*| k31:",len(k31_3))
print()
print("***********************************************************************************")
print()       
#print("k00_5=",len(k00_5),"k31_3=",len(k31_3)) 


for i in range(len(k13_3)):                                                  #EQN_4 (k13)
    for j in range(len(k22_3)):
        f1= m_h_GF2p8(bxa(i_sbox(bxa(ct1[1][3],k13_3[i])),i_sbox(bxa(fct1[1][3],k13_3[i]))),[0,0,0,0,0,0,0,1])
        f2= m_h_GF2p8(bxa(i_sbox(bxa(ct1[2][2],k22_3[j])),i_sbox(bxa(fct1[2][2],k22_3[j]))),[0,0,0,0,0,0,0,1])
        #print(f1,f2)
        if(f1==f2):
            k13_4.append(k13_3[i])
            k22_4.append(k22_3[j])

k13_4=list(set(k13_4)) 
k22_4=list(set(k22_4))   
print("After Eqn 10: k00:",len(k00_5)," |*|  k13:",len(k13_4)," |*| k22:",len(k22_4)," |*| k31:",len(k31_3),"  Key Succesfully Recovered")
print()
print("***********************************************************************************")
print()         
#print("k13_4=",len(k13_4),"k22_1=",len(k22_4)) 


for i in range(len(k13_4)):                                                  #EQN_5 (k13)
    for j in range(len(k31_3)):
        f1= m_h_GF2p8(bxa(i_sbox(bxa(ct1[1][3],k13_4[i])),i_sbox(bxa(fct1[1][3],k13_4[i]))),[0,0,0,0,0,0,1,1])
        f2= m_h_GF2p8(bxa(i_sbox(bxa(ct1[3][1],k31_3[j])),i_sbox(bxa(fct1[3][1],k31_3[j]))),[0,0,0,0,0,0,0,1])
        #print(f1,f2)
        if(f1==f2):
            k13_5.append(k13_4[i])
            k31_4.append(k31_3[j])

k13_5=list(set(k13_5)) 
k31_4=list(set(k31_4))
print("After Eqn 11: k00:",len(k00_5)," |*|  k13:",len(k13_5)," |*| k22:",len(k22_4)," |*| k31:",len(k31_4))
print()
print("***********************************************************************************")
print()             
#print("k13_5=",len(k13_5),"k31_4=",len(k31_4)) #

for i in range(len(k22_4)):                                                  #EQN_6 (k22)
    for j in range(len(k31_4)):
        f1= m_h_GF2p8(bxa(i_sbox(bxa(ct1[2][2],k22_4[i])),i_sbox(bxa(fct1[2][2],k22_4[i]))),[0,0,0,0,0,0,1,1])
        f2= m_h_GF2p8(bxa(i_sbox(bxa(ct1[3][1],k31_4[j])),i_sbox(bxa(fct1[3][1],k31_4[j]))),[0,0,0,0,0,0,0,1])
        #print(f1,f2)
        if(f1==f2):
            k22_5.append(k22_4[i])
            k31_5.append(k31_4[j])

k22_5=list(set(k22_5)) 
k31_5=list(set(k31_5))     
print("After Eqn 12: k00:",len(k00_5)," |*|  k13:",len(k13_5)," |*| k22:",len(k22_5)," |*| k31:",len(k31_5))
print()
print("***********************************************************************************")
print()        
#print("k22_5=",len(k22_5),"k31_5=",len(k31_5))

print("Final value of Bytes column 1 of key10 (in Hexadecimal)","r0c0:",hex(batoi(k00_5))[2:],"r1c3",hex(batoi(k13_5))[2:],"r2c2",hex(batoi(k22_5))[2:],"r3c1",hex(batoi(k31_5))[2:])
print()
print("***********************************************************************************")
print()
print("Final value of Bytes column 1 of key10 (in Binary)","r0c0:",k00_5,"r1c3",k13_5,"r2c2",k22_5,"r3c1",k31_5)
print()
print("***********************************************************************************")
print() 


