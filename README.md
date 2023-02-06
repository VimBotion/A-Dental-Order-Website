# Final-ProjectFr
HTML:

All inside the templates folder

The index.html shows a table with the order history that each user submit in the order.html (order route "/order"), each user has their own table

The layout.html is the base template that containts all the elements inside the head tag. It containts the footer and some jinja blocks:
    {% block title %}{% endblock %} for the title
    {% if session["id"] %}{% endif %} contains the navbar that is show only if the user has log in
    {% block main %}{% endblock %} for all the content inside the main tag
    {% block javascript %}{% endblock %} for the script tag 


The location.html shows the location of the dental lab using google maps

The login.html shows a form with name, email, password inputs that the user has to fill, it uses javascript and error checks in python flask to ensure the user enter all the data correctly, it also has a link to the register.html

The register.html shows a form with name, email, password and confirm password inputs that the user has to fill and if everything is correct, this data is passed to the user table in the database

The order.html shows a form with data of the patient that the user (doctor) has to fill and when submit it it redirects to the homepage showing a table with the history of the orders. If everything is correctm the data is passed to the order table in the database

CSS:

We use the tailwind css framework to build our website it was installed with the Tailwind CLI tool. It created a tailwind.config.js file that we used to made our own class called "text-letters" for the color of the text used in the navbar
