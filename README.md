# UW-La Crosse Alumni
This is an alumni system written by Gong Chen. He reserves all rights of this project.
I pushed this project in github only for maintaining convenience.

Han Chen
3/20/2015

====================
 Deployment Guide
====================

IMPORTANT

To ensure that everything works together compatibly, please use 32-bit version for all software, tools, libraries, and so on, no matter which version of Operating system you are using.

#Before Running

1. Download or pull this project from github https://github.com/alvinvinvinvin/Alumni/
2. Download and install MySql http://dev.mysql.com/downloads/
3. Create new scheme in MySql named “mse_alumn”
4. Download and install Python 2.7 (not 3.0+) https://www.python.org/downloads/
5. After installed Python, in your command prompt or terminal, run “pip install Django==1.6.5”.
6. After Django installation progress done, run “python”. In your python environment, run “import django”, and then run “print(django.get_version())”. If your Django was installed correctly, you would see the version of Django which should be “1.6.5” in our case. If you encountered any problem, please check Django official website. https://www.djangoproject.com/
7. Install Pagination tool. It is in the package called “django-pagination-1.0.7.tar.gz”. Unzip it, in its root directory (where the “setup.py” file belongs to), run “python setup.py”. It will automatically install this tool to python library.

#To Run

Modify “settings.py” in “Alumni\Alumni” directory to make this project compatible with your Operating System environment. It has rich comment to introduce you how to set up your own setting file in detail.

#Windows

1. Install “MySQL-python-1.2.5.win32-py2.7” and “PIL-1.1.7.win32-py2.7”.
2. In root directory of “Alumn” project (where “manage.py” belongs to), run “python manage.py syncdb” to synchronize your database scheme with project models. It only works when the “mse_alumn” scheme we created earlier is empty, so if you had any historical data in that, backup, clear it, and run this command again.
3. In same directory, run “python manage.py runservcr 8000”. The server will run and using 8000 port to be accessed. You can change it to whatever port number you want to, just be sure it is not occupied by other processes.
4. Open browser. Input “localhost:8000” in address bar. Hit enter. You should see the main page of the website.
5. Remember it is just a virtual server running locally for debugging only. Other machine with different IP address cannot access your running virtual server.

#MAC OSX

First of all, be prepared to face dozens of tricky problems. They might take your days to figure out how to successfully running your Django project on MAC OSX environment. I didn’t write down all of them here because I forgot 80% of what problems you would face and what the solutions are. Just use google and you will find a lot of answers. However, trying out which answer is correct for your case will take the most time you spend on that. Just be prepared, be confident and be patient, you can finally make it running!

1. In terminal, run “pip install Pillow” to install “PIL” similar in Windows.
2. Run “pip install MySQL-python”. If you encountered problems relating to MySQL here, try to uninstall your MySQL first, and run “brew install mysql”.
3. In root directory of “Alumn” project (where “manage.py” belongs to), run “python manage.py syncdb” to synchronize your database scheme with project models. It only works when the “mse_alumn” scheme we created earlier is empty, so if you had any historical data in that, backup, clear it, and run this command again.
4. In same directory, run “python manage.py runservcr 8000”. The server will run and using 8000 port to be accessed. You can change it to whatever port number you want to, just be sure it is not occupied by other processes.
5. Open browser. Input “localhost:8000” in address bar. Hit enter. You should see the main page of the website.


#Deployment using Apache

This guide is only for Windows.

1. Install Apache. Pick correct version for compatible with Python 2.7. http://httpd.apache.org/ . You can also find downloaded versions in package.
2. Set up middleware “mod_wsgi”. https://code.google.com/p/modwsgi/ . You can also find downloaded versions in package. If you don’t know how to set up a middleware in Apache configuration, google it.
