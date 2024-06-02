Board1_Responses=[]
Board2_Responses=[]
Board3_Responses=[]


def Make_Challenge_Response_list(Board_Responses,file_name):
    with open(file_name,"r") as file:
        File_data=file.readlines()
        count=1
        for line in File_data:
            colon_index=line.index(":")
            newline_index=line.index("\n")
            if(count%2==0):
                sliced_string_responses=line[colon_index+1:newline_index]
                Board_Responses.append(sliced_string_responses)
            count+=1


def calculate_uniformity(Board):
    sum=0
    count_responses=0
    for row in Board:
        for res in row:
            sum+=int(res)
            count_responses+=1
    uniformity_tmp=(sum/count_responses)*100
    uniformity_main=round(uniformity_tmp,2)
    return uniformity_main


Make_Challenge_Response_list(Board1_Responses,"Assignment 4/CRPS/G2/Board1_10K_2.txt")
Make_Challenge_Response_list(Board2_Responses,"Assignment 4/CRPS/G2/Board2_10K_2.txt")


def calculate_uniqueness(Board_x,Board_y):
    Hamming_Distance=0
    for i in range(len(Board_x)):
          hd=Board_x[i]^Board_y[i]
          Hamming_Distance=Hamming_Distance+hd
    tmp=Hamming_Distance/(len(Board_x)/100)
    uniqueness=tmp
    return uniqueness



def reliabilityOfPUF(g):
    a=[]
    b=[]
    for i in range(1,16):
        s=g+str(i)+".txt"
        Make_Challenge_Response_list(b,s)
        a.append(b)
        b=[]

    realibility=0
    for i in range(10000): #10000
        f=[]
        for j in range(15): 
            f.append(int(a[j][i]))
        if(f.count(1)>f.count(0)): 
            Board3_Responses.append([1])
            rel=(1-(f.count(0)/15))*100
        else:
            Board3_Responses.append([0])   
            rel=(1-(f.count(1)/15))*100
        realibility=realibility+rel         
    return(realibility/10000)    

print("")
print("")
print("********************  Algorithm Starts  ********************")
print("")
rel_add="Assignment 4/CRPS/G2/Board3_G2/Board3_10K_2_S"

#Reliability
board3_reliabiliy=reliabilityOfPUF(rel_add)

#uniformity
#Calculating uniformity of Board 1
temp=[]
for i in Board1_Responses:
    temp.append(i)
board1_uniformity=calculate_uniformity(temp)

#Calculating uniformity of Board 2
temp=[]
for i in Board2_Responses:
    temp.append(i)
board2_uniformity=calculate_uniformity(temp)

temp=[]
for i in Board3_Responses:
    temp.append(i)
board3_uniformity=calculate_uniformity(temp)


#Calculating uniqueness

Board1_array=[]
Board2_array=[]
Board3_array=[]

for row in Board1_Responses:
    Board1_array.append(int(row[0]))
for row in Board2_Responses:
    Board2_array.append(int(row[0]))
for row in Board3_Responses:
    Board3_array.append(int(row[0]))

#Uniqueness Between Board 1 and Board 2
uniqueness_Board1_Board2=calculate_uniqueness(Board1_array,Board2_array)

#Uniqueness Between Board 2 and Board 3
uniqueness_Board2_Board3=calculate_uniqueness(Board2_array,Board3_array)

#Uniqueness Between Board 1 and Board 3
uniqueness_Board1_Board3=calculate_uniqueness(Board1_array,Board3_array)

#Board Responses
print("********************  Board Responses  ********************")
print("")
print("Board 1 Responses: ",Board1_array)
print("")
print("Board 2 Responses: ",Board2_array)
print("")
print("Board 3 Responses: ",Board3_array)

#Outputs
print("")
print("")
print("********************  Output  ********************")
print("")
print("The Realibility For Board 3 is: ",board3_reliabiliy,"%")
print("The Uniformity For Board 1 is: ",board1_uniformity,"%")
print("The Uniformity For Board 2 is: ",board2_uniformity,"%")
print("The Uniformity For Board 3 is: ",board3_uniformity,"%")
print("The Uniqueness For Board 1 and Board 2 is: ",uniqueness_Board1_Board2,"%")
print("The Uniqueness For Board 2 and Board 3 is ",uniqueness_Board2_Board3,"%")
print("The Uniqueness For Board 1 and Board 3 is: ",uniqueness_Board1_Board3,"%")
print("")
print("")
print("********************  Algorithm End  ********************")
print("")
print("")


