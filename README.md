# LangTrainer
LangTrainer is a flashcard app made with Flask. It is especially suited for learning words in a new language. You just upload the words you want to learn to start practicing. You can run the app locally on your machine to practice with the flashcards.

## Getting Started
### Prerequisites
The app requires that you have the Python interpreter and mysql installed on your computer. The reason I have used MySQL and not SQLite for the database is because I might deploy the app under a domain later and run the server using MySQL.

### Installing
**1.** Change directory to the directory you want the files to be stored inside, and clone the git repository with this command:
```
git clone https://github.com/JaranMellerud/LangTrainer.git
```
**2.** Change directory to the project directory and install the required packages (preferably in a virtual environment you have created):
```
pip install -r requirements.txt
```
**3.** If you do not have it already, install MySQL on your computer. Log in and create a new database for the app. Then store the database URI in your environment variables with the key name "LANGTRAINER_DB_URI".

**4.** Create a secret key for the application and store it in your environment variables with the key name "LANGTRAINER_SECRET_KEY". This key can be whatever you want.

**5.** Run the run.py file to start the application!

## Built With
* [Flask](https://flask.palletsprojects.com/en/1.1.x/) - The web framework used
* [SQLAlchemy](https://www.sqlalchemy.org/) - Database Toolkit

## Why I Made It
I am learning Russian, and I wanted a very minimalistic and simple flash card app to practice vocabulary. I have been very curious about web development, and since I knew Python from before, I thought making a web application with the Flask framework would be a simple way to take a step into web development world. For my next web development project I will definetely not use Flask, but one of the JavaScript frameworks.

## What I have learned
* Flask fundamentals
* Creating and querying databases in MySQL
* Using SQLAlchemy in combination with flask-forms to database via html forms in Flask
* HTML fundamentals (structure, forms, tables)
* CSS fundamentals

## Images
**Fixed box sizes. Might look small since I have a very big screen.**
![Register page](https://user-images.githubusercontent.com/56685171/79042391-ccb87280-7bf7-11ea-94a5-46be4098c156.png)
![Login page](https://user-images.githubusercontent.com/56685171/79042367-8400b980-7bf7-11ea-822f-3a498b1bb4cf.png)
![Practice page](https://user-images.githubusercontent.com/56685171/79042427-1608c200-7bf8-11ea-8108-c028c0ff8922.png)
![Practice page](https://user-images.githubusercontent.com/56685171/79042455-4cded800-7bf8-11ea-8173-7d026224a650.png)
![Vocabulary page](https://user-images.githubusercontent.com/56685171/79042481-831c5780-7bf8-11ea-89cb-9881158eb53f.png)
