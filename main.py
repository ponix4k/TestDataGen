#! /usr/bin/python3
def main():
    opt = input("Select database type to export data to \n#1 - SQLite3\n#2 - CSV(in development)")
    if opt() == 1:
        SQL3.main()
    else:
       print("Whoops this is still under construction")

if __name__ == "__main__":
    main()