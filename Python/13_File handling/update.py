    
flag = True
while(flag):
    ans = input("\nDo you want to update (Y,N) : ")

    if ans.lower() == 'y':
        with open('sample.txt','a+') as f:
            f.seek(len(f.read())+5)
            line = input("Enter data or line : ")
            f.write("\n")
            f.write(line)
            print("Data Append Successfully")
            f.close()
        
        with open('sample.txt','r') as f1:    
            for i in f1.readlines():
                print(i,end='')

            

    else:
        flag = False
