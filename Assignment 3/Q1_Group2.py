import csv
def rank_simple(vector):
    return sorted(range(len(vector)), key=vector.__getitem__)

def rankdata(a):
    n = len(a)
    ivec=rank_simple(a)
    svec=[a[rank] for rank in ivec]
    sumranks = 0
    dupcount = 0
    newarray = [0]*n
    for i in range(n):
        sumranks += i
        dupcount += 1
        if i==n-1 or svec[i] != svec[i+1]:
            averank = sumranks / float(dupcount) + 1
            for j in range(i-dupcount+1,i+1):
                newarray[ivec[j]] = averank
            sumranks = 0
            dupcount = 0
    return newarray

def inverse_sbox(upper_nibble,lower_nibble):
      
      sbox = [
        [0x52, 0x09, 0x6a, 0xd5, 0x30, 0x36, 0xa5, 0x38, 0xbf, 0x40, 0xa3, 0x9e, 0x81, 0xf3, 0xd7, 0xfb],
        [0x7c, 0xe3, 0x39, 0x82, 0x9b, 0x2f, 0xff, 0x87, 0x34, 0x8e, 0x43, 0x44, 0xc4, 0xde, 0xe9, 0xcb],
        [0x54, 0x7b, 0x94, 0x32, 0xa6, 0xc2, 0x23, 0x3d, 0xee, 0x4c, 0x95, 0x0b, 0x42, 0xfa, 0xc3, 0x4e],
        [0x08, 0x2e, 0xa1, 0x66, 0x28, 0xd9, 0x24, 0xb2, 0x76, 0x5b, 0xa2, 0x49, 0x6d, 0x8b, 0xd1, 0x25],
        [0x72, 0xf8, 0xf6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xd4, 0xa4, 0x5c, 0xcc, 0x5d, 0x65, 0xb6, 0x92],
        [0x6c, 0x70, 0x48, 0x50, 0xfd, 0xed, 0xb9, 0xda, 0x5e, 0x15, 0x46, 0x57, 0xa7, 0x8d, 0x9d, 0x84],
        [0x90, 0xd8, 0xab, 0x00, 0x8c, 0xbc, 0xd3, 0x0a, 0xf7, 0xe4, 0x58, 0x05, 0xb8, 0xb3, 0x45, 0x06],
        [0xd0, 0x2c, 0x1e, 0x8f, 0xca, 0x3f, 0x0f, 0x02, 0xc1, 0xaf, 0xbd, 0x03, 0x01, 0x13, 0x8a, 0x6b],
        [0x3a, 0x91, 0x11, 0x41, 0x4f, 0x67, 0xdc, 0xea, 0x97, 0xf2, 0xcf, 0xce, 0xf0, 0xb4, 0xe6, 0x73],
        [0x96, 0xac, 0x74, 0x22, 0xe7, 0xad, 0x35, 0x85, 0xe2, 0xf9, 0x37, 0xe8, 0x1c, 0x75, 0xdf, 0x6e],
        [0x47, 0xf1, 0x1a, 0x71, 0x1d, 0x29, 0xc5, 0x89, 0x6f, 0xb7, 0x62, 0x0e, 0xaa, 0x18, 0xbe, 0x1b],
        [0xfc, 0x56, 0x3e, 0x4b, 0xc6, 0xd2, 0x79, 0x20, 0x9a, 0xdb, 0xc0, 0xfe, 0x78, 0xcd, 0x5a, 0xf4],
        [0x1f, 0xdd, 0xa8, 0x33, 0x88, 0x07, 0xc7, 0x31, 0xb1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xec, 0x5f],
        [0x60, 0x51, 0x7f, 0xa9, 0x19, 0xb5, 0x4a, 0x0d, 0x2d, 0xe5, 0x7a, 0x9f, 0x93, 0xc9, 0x9c, 0xef],
        [0xa0, 0xe0, 0x3b, 0x4d, 0xae, 0x2a, 0xf5, 0xb0, 0xc8, 0xeb, 0xbb, 0x3c, 0x83, 0x53, 0x99, 0x61],
        [0x17, 0x2b, 0x04, 0x7e, 0xba, 0x77, 0xd6, 0x26, 0xe1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0c, 0x7d]
    ]
      
      sbox_value_func=sbox[upper_nibble][lower_nibble]
      return sbox_value_func




ciphertext=[]
complete_power_array=[]
with open('Question 1 traces/HW_power_trace_2.csv', mode ='r')as file: 
  csvFile = csv.reader(file)
  count=0
  for lines in csvFile:
        count=count+1
        ciphertext.append((int)(lines[1]))
        single_power_array=[]
        for i in range(2,13):
            single_power_array.append((int)(lines[i]))
        complete_power_array.append(single_power_array)

print("**********************************************************************")
print("Q1 Group 2 Solution")
print("**********************************************************************")

ranking=[]
Key=[]
for i in range(0,256):
    Key.append(i)

print("List Of Guessed Keys")
print(Key)
print("**********************************************************************")


for k in range(0,11):
    print("Starting iteration for",k+1,"th Power Trace ")

    rows, cols = (10000, 256)
    one_bin_4thbyte = [[0 for i in range(cols)] for j in range(rows)]
    zero_bin_4thbyte = [[0 for i in range(cols)] for j in range(rows)]

    for i in range(0,10000):
     for j in range(0,256):
        fourth_byte_cipher_bin=format(ciphertext[i],'b')
        fourth_byte=fourth_byte_cipher_bin[32:40:1]
        x=format(((int)(fourth_byte,2)^(int)(Key[j])),'b') #implement the inverse sbox function
        if len(x) < 8:
            x = '0' * (8 - len(x)) + x
        upper_nibble=int(x[0:4:1],2)
        lower_nibble=int(x[4:8:1],2)

        sbox_value=inverse_sbox(upper_nibble,lower_nibble)
        
        if(sbox_value&1):
            one_bin_4thbyte[i][j]=complete_power_array[i][k]
            
        else:
            zero_bin_4thbyte[i][j]=complete_power_array[i][k]

    print("Zero Bin Value ",zero_bin_4thbyte)
    print("One Bin Value",one_bin_4thbyte)


    one_bin_4thbyte_frequency=[]
    one_bin_4thbyte_value=[]
    zero_bin_4thbyte_frequency=[]
    zero_bin_4thbyte_value=[]
    for i in range(0,256):
        temp_one_fr=0
        temp_zero_fr=0
        temp_one_value=0
        temp_zero_value=0
        for j in range(0,10000):
            if(one_bin_4thbyte[j][i]==0):
                temp_zero_fr+=1
            else:
                temp_one_fr+=1
            temp_zero_value+=zero_bin_4thbyte[j][i]
            temp_one_value+=one_bin_4thbyte[j][i]
        one_bin_4thbyte_frequency.append(temp_one_fr)
        zero_bin_4thbyte_frequency.append(temp_zero_fr)   
        one_bin_4thbyte_value.append(temp_one_value)
        zero_bin_4thbyte_value.append(temp_zero_value)

    #Difference of mean
    difference_of_mean_4thbyte=[]
    for i in range(0,256):
        zero_f=zero_bin_4thbyte_frequency[i]
        one_f=one_bin_4thbyte_frequency[i]
        zero_v=zero_bin_4thbyte_value[i]
        one_v=one_bin_4thbyte_value[i]
        if(zero_f and one_f):
            dom_value=abs((one_v/one_f)-(zero_v/zero_f))
        else:
            if(zero_f==0):
                dom_value=one_v/one_f
            else:
                dom_value=zero_v/zero_f

        difference_of_mean_4thbyte.append(dom_value)
    print("Difference Of Mean Array ")
    print(difference_of_mean_4thbyte)
    rank_temp=rankdata(difference_of_mean_4thbyte)
    ranking.append(rank_temp)
    print("Ranking of Difference Of Mean Values")
    print(rank_temp)
    print("**********************************************************************")

print("Complete Ranking Matrix")
print(ranking)
total_rank=[]
for i in range(0,256):
    t_rank=0
    for j in range(0,11):
        t_rank+=ranking[j][i]
    total_rank.append(t_rank)

print("Total Ranking Matrix")
print(total_rank)
final_key_index_4thbyte=0
temp_val=0
for i in range(0,256):
    if(total_rank[i]>temp_val):
        temp_val=total_rank[i]
        final_key_index_4thbyte=i
print("The 4th Key Byte is ",hex(Key[final_key_index_4thbyte]))     
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
fourth_byte_answer=hex(Key[final_key_index_4thbyte])
#4th byte done
#fifth byte start
print("Lets Find Out The 5th Byte Of The Key ")
ranking=[]

for k in range(0,11):
    print("Starting iteration for",k+1,"th Power Trace ")

    rows, cols = (10000, 256)
    one_bin_5thbyte = [[0 for i in range(cols)] for j in range(rows)]
    zero_bin_5thbyte = [[0 for i in range(cols)] for j in range(rows)]

    for i in range(0,10000):
     for j in range(0,256):
        fifth_byte_cipher_bin=format(ciphertext[i],'b')
        fifth_byte=fifth_byte_cipher_bin[40:48:1]
        x=format(((int)(fifth_byte,2)^(int)(Key[j])),'b') #implement the inverse sbox function
        if len(x) < 8:
            x = '0' * (8 - len(x)) + x
        upper_nibble=int(x[0:4:1],2)
        lower_nibble=int(x[4:8:1],2)

        sbox_value=inverse_sbox(upper_nibble,lower_nibble)
        
        if(sbox_value&1):
            one_bin_5thbyte[i][j]=complete_power_array[i][k]
            
        else:
            zero_bin_5thbyte[i][j]=complete_power_array[i][k]


    print("Zero Bin Value ",zero_bin_5thbyte)
    print("One Bin Value",one_bin_5thbyte)

    one_bin_5thbyte_frequency=[]
    one_bin_5thbyte_value=[]
    zero_bin_5thbyte_frequency=[]
    zero_bin_5thbyte_value=[]
    for i in range(0,256):
        temp_one_fr=0
        temp_zero_fr=0
        temp_one_value=0
        temp_zero_value=0
        for j in range(0,10000):
            if(one_bin_5thbyte[j][i]==0):
                temp_zero_fr+=1
            else:
                temp_one_fr+=1
            temp_zero_value+=zero_bin_5thbyte[j][i]
            temp_one_value+=one_bin_5thbyte[j][i]
        one_bin_5thbyte_frequency.append(temp_one_fr)
        zero_bin_5thbyte_frequency.append(temp_zero_fr)   
        one_bin_5thbyte_value.append(temp_one_value)
        zero_bin_5thbyte_value.append(temp_zero_value)


    difference_of_mean_5thbyte=[]
    for i in range(0,256):
        zero_f=zero_bin_5thbyte_frequency[i]
        one_f=one_bin_5thbyte_frequency[i]
        zero_v=zero_bin_5thbyte_value[i]
        one_v=one_bin_5thbyte_value[i]
        if(zero_f and one_f):
            dom_value=abs((one_v/one_f)-(zero_v/zero_f))
        else:
            if(zero_f==0):
                dom_value=one_v/one_f
            else:
                dom_value=zero_v/zero_f

        difference_of_mean_5thbyte.append(dom_value)
    print("Difference Of Mean Array ")
    print(difference_of_mean_5thbyte)
    rank_temp=rankdata(difference_of_mean_5thbyte)
    ranking.append(rank_temp)
    print("Ranking of Difference Of Mean Values")
    print(rank_temp)
    print("**********************************************************************")

print("Complete Ranking Matrix")
print(ranking)
total_rank=[]
for i in range(0,256):
    t_rank=0
    for j in range(0,11):
        t_rank+=ranking[j][i]
    total_rank.append(t_rank)

print("Total Ranking Matrix")
print(total_rank)
final_key_index_5thbyte=0
temp_val=0
for i in range(0,256):
    if(total_rank[i]>temp_val):
        temp_val=total_rank[i]
        final_key_index_5thbyte=i
print("The 5th Key Byte is ",hex(Key[final_key_index_5thbyte]))     
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
fifth_byte_answer=hex(Key[final_key_index_5thbyte])

print("FINAL RESULT")
print("The 4th Key Byte is ",fourth_byte_answer)          
print("The 5th Key Byte is ",fifth_byte_answer)  