banks_list=["kotak","HDFC","RBL","SBI","banks of broda"]
file=open("file_bank","w")
i=0
while i<len(banks_list):
    file.write(banks_list[i])
    file.write("\n")
    i=i+1
file.close()



