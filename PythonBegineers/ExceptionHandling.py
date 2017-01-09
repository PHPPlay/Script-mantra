#!/usr/bin/python3


# the below code will check if the file blah is exist or not. If not it will except and print the file not found
#def Main():
 #   try:
  #      f = open("Blah.txt", "r")
   #     for line in f:
    #        print(line.strip("\n\r"))

#        f.close()

#    except:
 #       print("The file was either not found or unable to be read or locate")

#if __name__ == "__main__":
 #   Main()

def Main():
    try:
        d = open("Fuckme.txt", "r")
        for line in d:
            print(line.strip("\n\r"))
        d.close()

    except:
        print("The file does not exist")

    finally:
        print("Exiting")


if __name__ == "__main__":
    Main()
