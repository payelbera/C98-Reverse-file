def reverseFile():
    fileName1 = input("Enter File 1")
    fileName2 = input("Enter File 2")

    file1 = open(fileName1,'r')
    file2 = open(fileName2,'r')

    data_a = file1.read();
    

    data_b = file2.read();

    file1_w = open(fileName1,'w')
    file2_w = open(fileName2,'w')

    file1_w.write(data_b)
    file2_w.write(data_a)



reverseFile()