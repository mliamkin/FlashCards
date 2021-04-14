# FlashCards

1) Start Python Virtual Environment

2) Add this folder to the venv folder

3) Activate Python virtual environment by going to venv folder in command prompt, then "Scripts" folder, then type "activate"

4) Go to posted folder, type "set FLASK_DEBUG=1" and "set FLASK_APP=app.py"

5) Type "flask run"


ISSUES:

+ No way to create set or delete a set
+ As the data is provided via a JSON file, there are no ID's given to items. Data is provided with a dictionary. So, when deleting a flashcard in a set, it will remove a flashcard, but not the one you selected.
