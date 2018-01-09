# career-map
Visual interface for establishing a career map and training plan in the IT industry.

https://it-map.herokuapp.com/


Documentation:

Data.csv: 

It’s the data file which contains the all the data for the job positions and their promotions, gathered from the managers. 

Dropdown.csv:

It’s a data file which contains all the jobs in a list. It was created to read it and add dropdown functionality to the website.

Flask app:

The project was based on the Dijkstra’s algorithm which can easily be done in python with the library networkx. So, the foundation of the project had to be python. We used Flask framework to build the website. The backend project work is done here.

Mapapp.py

It is the base of the flask app, it contains the methods to run the website. It imports all the other python files in the project. 

Compute.py

The Dijkstra’s algorithm is computed in this python file and exported to the mapapp.py file.

Models.py

This file is used to create the dropdowns or the text fields required in the project.

HTML

The front-end work is done here.

About.html:

This page shows the user what they will get out of the website and what the project is about

Index.html

This is the homepage

View.html

This page displays the map and the shortest distance between two positions.

Layout.html

This is the master page containing header and footer for all other pages.

Heroku:

The project had to be deployed onto the web. So we used Heroku, it has a free version with limited usability which is fine for the project.

.gitignore:

This file contains the python environment which the project needs to run on. It will ignore everything else.

Procfile:

This file is used to run the Heroku with gunicorn.

Requirements.txt:

This file contains all the dependencies of the flask app and other dependencies needed to run the project. This is used to create a virtual environment in Heroku to deploy the flask app. 

GIT:

This project also has a version control. All the changes have been committed to the master branch. 
