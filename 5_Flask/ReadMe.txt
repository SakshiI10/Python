1. Create a virtual environment in VS Code.
pip install virtualenv
virtualenv env 

2. Open Administrator Windows Powershell.
Set-ExecutionPolicy Unrestricted

3. Come back to VS Code.
.\env\Scripts\activate.ps1

4. Run python Code.
python 1_hello_world.py 

5. Create static and templates folder
Do not add confidential files in static folder as it's data would be directly visible on the weebpage.

6. Create a HTML file and store it in templates folder.

7. Import SQLAlchemy.

8. In new terminal activate the environment and paste following codes for creating a todo.db file (it was created in instance):
>>> from app import app, db
>>> with app.app_context():
...     db.create_all()
... 
>>> exit()

9. Open sqlite viewer.

10. build app.py and index.html as you need.