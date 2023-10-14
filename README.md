# A Dental Order Website
#### Video Demo:  https://www.youtube.com/watch?v=HUSYjzgsS8o&t=1s
#### Description: A website to make dental orders with ease
#### Made by: MrRobotAE10 and Vn0m
#### To run this project: First install tailwind and all the libraries used. Run npx tailwindcss -i ./src/input.css -o ./static/output.css --watch, then run python3 app.py in the terminal


When my partner Vn0m and I finished all the psets we agreed to collaborate for our final project, at the beggining it seemed imposibble to think of building something from scratch. At first we put into the table some ideas like a videogame, a weather app, chrome extension, etc. But then looking back into week 9 we realized that a great option could be making a website with flask. We started to discuss some ideas such as an online clothing store, a product landing page, a quiz and finally the winner idea that was a dental order website because MrRobotAE10 grandparents had a dental lab which we wanted to help out by adding this online feature to it. After that we designed the logo for the website, gave it a name and chose the color palette that fits the best with the theme.

Firstly, we decided to choose the languages, tools and frameworks that we were going to use for this project which ended up being python, javascript, html, css, SQL for the languages, github, git, poetry for our tools and finally tailwindCSS and flask for our frameworks. We started by setting up flask and tailwindCSS with poetry, then we created folders called templates and static.


###### **APP.PY**:

We created app.py where we imported the following libraries: 

-from flask import Flask, render_template, request, redirect, session, url_for (for the backend)

-from flask_sqlalchemy import SQLAlchemy (for the database)

-from flask_login import UserMixin (for login)

-from functools import wraps (for the login_required that prevents the user from going to the pages without previous login)

-from werkzeug.security import check_password_hash, generate_password_hash (generate hash for password and compare password input with the database password)

-from datetime import date (shows when the order was made in the table)


We made the user table which contains id(int), username(string), email(string), hash(string) and patient(relationship linked with the orders table). 
Then we made the order table that contains id(int), patient_name(string), patient_age(int), color_chart(string), dates(string), patient_sex(string), indications and doctor_id(int and relationship with user table).

After the tables we can see the register route ("/register") that that has two methods (POST, GET), if the request method is via GET it renders the register.html and if its POST it takes the users inputs and it registers to the database only if the data is correct and username doesnt exist. After everything is correct it redirects you to the homepage ("/").

    We used the generate_password_hash() function  to hash the password.

The login route ("/login") has two methods (POST, GET), if the request method is via GET it renders the login.html and if its POST it takes the users inputs and if the user didnt fill the inputs it renders login.html. Then it query the database to ensure username, email, password are correct and if that is the case it redirects to the homepage ("/").

The logout ("logout")route clears the session and redirects you to the login page.

The index route ("/") checks if the user is logged in and query the database for the order info of each user (this means each user can see its own orders). It also renders the template index.html with the order info that was recolected.

The location route ("/location") renders the template for location.html.

The last route is order ("/order") which takes two methos (GET, POST), if its GET renders order.html and if its POST it takes the user input: patient_name, patient_age, patient_color_chart, indications, patient_sex and date. Then it ensures all the data is correct and sends it to the database where the doctor_id is equal to the id of the user that is logged in. Redirects to the homepage and displays in the table all the info that was entered.


###### **REGISTRATION.JS AND LOGIN.JS**

We created registration.js and login.js which works this way:

We have an array of different validation options (items in our array which also have three properties: attribute, isValid, and errormessage) that are: minlength, custommaxlength, match, required and pattern (This options are attributes in our html which makes the code very reusable).

    -Minlength: The isValid property takes the input value and its length and makes it so its length cannot be less than 3 charactes which we specify in the html element, then the errormessage property takes the input and the label and pops a message of error with the specific label if the input is not typed as we intended.
    -custommaxlength: The isValid property takes the input value and its length and makes it so its length cannot be more than 10 charactes which we specify in the html element, then the errormessage property takes the input and the label and pops a message of error with the specific label and the specific max length that we specified if the input is not typed as we intended.
    -match: The isValid property gets the attribute match from the confirm password element and it compares the input that the user types with the matched password, then the errormessage compares if the password is the same as the match attribute and if not it pops an error message using the specific label and match of the element.
    -pattern: The isValid property compares the text that is typed with a pattern that we put in the html element which is an specific email pattern so that we can test if it is a valid one or else errormessage property is going to pop a message with the specific label telling us that it is not valid.
    -required: the required is a general property where isValed checks for every element that it should not be blank or else errormessage will pop a message with the specific label that tells the input is required.

After, the validateSingleFormGroup function checks the form group and see if it meets the validation criteria that we just explained by getting all the elements that we need for the form group like label, input, textarea, .error, .error-icon and .success-icon. We loop trough all the validation options (array) and check if the input that we have in formgroup has the particular attribute, if not and if the isValid function does not work then is should send an error message and if its correct a success message. We also have for example formElement.setAttribute('novalidate', ''); which ignores the html restrictions so we can use our own, we also have an event for each input elements which we select them trough the formElement with an array that make the validation trigger with each input at a time using 'blur' for immediate feedback.

Finally, we use the formGroup function to check weather if all the form is valid for it to be submited or if it has errors and it cant be submited(if every call to validateSingleFormGroup returns true then it will return true). Therefore, in our eventListener for submit we can say that the form is valid if the result of validateAllFormGroups returns true or false. When the form is not valid we trigger the event.preventDefault(); , and when its valid the sendToAPI function makes that it checks all the form elements (inputs) and make it an object so that it submits to the API when validated. 

###### **HTML**:

All inside the templates folder

The index.html shows a table with the order history that each user submit in the order.html (order route "/order"), each user has their own table

The layout.html is the base template that containts all the elements inside the head tag. It containts the footer and some jinja blocks:

   - "{% blockk title %}{% endblock %}" for the title
    
   - "{% if session["id"] %}{% endif %}" contains the navbar that is show only if the user has log in
    
   -{% block main %}{% endblock %} for all the content inside the main tag
    
   -{% block javascript %}{% endblock %} for the script tag 


The location.html shows the location of the dental lab using google maps

The login.html shows a form with name, email, password inputs that the user has to fill, it uses javascript and error checks in python flask to ensure the user enter all the data correctly, it also has a link to the register.html

The register.html shows a form with name, email, password and confirm password inputs that the user has to fill and if everything is correct, this data is passed to the user table in the database

The order.html shows a form with data of the patient that the user (doctor) has to fill and when submit it it redirects to the homepage showing a table with the history of the orders. If everything is correctm the data is passed to the order table in the database

###### **CSS**:

We use the tailwind css framework to build our website it was installed with the Tailwind CLI tool. It created a tailwind.config.js file that we used to made our own class called "text-letters" for the color of the text used in the navbar
