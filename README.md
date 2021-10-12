# TestDataGen
This is a Python app to create test data using the faker module and store it into an SQLite3 Database.


---
## Installation
---
N.B If running the files gives an error message saying the files is dos mode error ('/r)' then open the offending file in vim and use the :set binary then save this will correct this problem

run the install.sh file to get required libs and create the directories that are needed.



---
## Usage
---

Use `python3 SQL3.py` to run the main program this will give you a READ, WRITE eXit options and export them to the SQLite3 Database.

---
## Misc
---
If you want to properly view the database you can use `sqllitebrowser` you can get it [here](https://sqlitebrowser.org/dl/)

## Linux (debian)
---
```bash
sudo apt-get update && sudo apt-get install sqlitebrowser -y
```
