def main():
    version = "0.0.1"
    print("Simple Text File Management System", version)
    command = input(">> ")
    try:
        with open(command,"r") as file:
            pass
    except:



        print(command)


main()