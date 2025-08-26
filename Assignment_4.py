try:
    what=input("what you want to perform: \n 1.Read a File and Handle Errors: \n 2.Write and Append Data to a File: ")
    what=int(what)
    if what==1:
        # Task 1: Read a File and Handle Errors
        try:
            file1 = open('sample.txt', 'r+')
            print("Reading file contains: ")
            read1 = file1.readlines()
            n=1
            for i in read1:
                print("Line",n,": ", i)
                n+=1
            file1.close()
        except FileNotFoundError:
            print("The file 'sample.txt' was not found")
    elif what==2:
        # Task 2: Write and Append Data to a File
        try:
            file2 = open('output.txt', 'w')
            x=input("What you want to write: ")
            file2.write(x)
            print("Data is successfully written in output.txt")
            file2.close()
            file3 = open('output.txt', 'a')
            y = input("What you want to append: ")
            file3.write("\n")
            file3.write(y)
            print("Data is successfully append in output.txt")
            file3.close()
            file1 = open('output.txt', 'r')
            print("Reading file final contains: ")
            read2 = file1.read()
            print(read2)
            file1.close()
        except FileNotFoundError:
            print("The file 'output.txt' was not found")
    else:
        print("Enter valid choice")
except ValueError:
    print("Enter a number")