#!/usr/bin/python3

# File IO
# The below lines will open a file and read the content and list the file using for loop
#def Main():
    #f = open("myfile.txt", "r")
    #for line in f:
     #   print(line.strip("\n\r"))
    #f.close()
# The below code will write the strings to the file myfile
#def Main():
#    f = open("myfile.txt", "w")
 #   for i in range(4):
  #      f.write(input("Please enter the string: ") + '\n')

   # f.close()

# The below the set of code will create a words and write the content of word in the file
def Main():
    words = ["cat", "sat", "bat", "map"]
    with open("words.txt", 'w') as f:
        for word in words:
            f.write(word + "\n")



if __name__ == "__main__":
    Main()
