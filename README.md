# Alice_for_Jagriti

This is an interactive textbook for students preparing for navodaya entrance exams. It contains static notes in Hindi as well and mentors can upload notes too for student's healthy preparation. It has a quiz and result portal which could be used by students to analyze student's performance. Quiz can be uploaded by mentors only. Students can upload queries too, which would be answered by students. The website contains an admin portal where notes uploaded would be approved to maintain decorum in the community. The admin also has the right to remove the registered user. Thus, this website can become a platform for the students to test themselves under the best guidance. 

************************************************************

# How to Clone this repo

Open gitbash and type the following command:

git clone "https://github.com/somya51p/Alice_for_Jagriti/"

*************************************************************
Open Visual Studio code and type the following command in terminal:

python reqirements.txt

*************************************************************
Followed by these commands in terminal itself:

python manage.py migrate
python manage.py makemigrations notes,quiz,Book
python manage.py migrate

*************************************************************

To run the Alice app then type:

python manage.py runserver

This would make the app run in the browser..
**************************************************************

In order to access the django-admin, One must create a superuser so type the following command for the same:

python manage.py createsuperuser

Fill the required details and it would be created..

**************************************************************

# Enjoy using the Alice Web App..

**************************************************************
**************************************************************
