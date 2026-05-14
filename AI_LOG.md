AI Tools Used: ChatGPT Free Version 

Prompt 1: I copied and pasted the contents of the original README.md file and asked it to explain what all of the files did and where I would put my tables and other logic

AI Output: Explained the models.py file is where you defined the tables, routes is where you create the urls for the pages of your website and the logic for them and so on.

Modifications: No code was generated




Prompt 2: How do I define tables in the models.py file including constraints 

AI Output: Generated code for an example table, and explained what specific things did.

Modifications: None, I created my tables by hand.




Prompt 3: Copied and pasted the tables I made and asked if anything was incorrect, also asked how I would define foriegn key constaints for tables

AI Output: Explained any mistakes I had and showed what a foreign key would look like for my tables.

Modifications: I used the foriegn key code which was maybe 2 lines per table, I created the rest of the keys myself. 



Prompt 4: Copied and pasted the original contents of index.html file and asked about what I now know is the Jinja 2 template language. I saw the example table in the code and asked how I would display the contents of my tables using that 

AI output: Explained specifics of the html and jinja language, also gave code that would display things for one of my tables.

Modifications: I copied and pasted the code that would display items from my table, eventually I would understand the bootstrap and jinja 2 to where I would be making seperate files that extend the base.html file. I liked the way the tables were displayed with the bootstrap classes, the main things I changed were the data that is displayed. I use that html + jinja for all table displays on the main page just altering jinja variables and so on.


Prompt 5: Copied and pasted original routes file and asked what was going on. 

AI Output: Gave surface level information about what was going on.

Modifications: None


Prompt 6: I asked what a route to create a record for one of my tables would look like. 

AI Output: Generated a route and function for the route which only used a "GET" request.

Modification: I used the code at first because I really didn't understand what was going on, I only began to truly understand how to use routes and seperate html files with the render_template and passing jinja variables after watching tutorial videos. I also had a lot more prompts similar to this one trying to get the one page to work. 



Prompt 7: I have a page that has a form that submits information for my table, how do I update the table with this data

AI Output: Explained the request.form to extract the information the form sends as long as the "name" field in the form is the same as what you ask it. Also gave some code

Modification: I took the code which did not validate anything and was simple maybe 10 or so lines. I then proceeded to run into issues because my page methods function argument was only "GET" when submitting the form. Tutorial videos helped me figure out how to use the 1 page for both "GET" and "POST" requests, as well as url_for in the form action. 



Prompt 8: I want to seperate a function from the routes.py file so the file does not get really long, how do I do this in python 

AI Output: Explained how to seperate files and import them into other files

Modifications: None


Prompt 9: I asked about data validation in python, also using exceptions I saw in a video and how I could use it in my create functions

AI Output: Explained functions that would convert datatypes and ways to validate, gave examples using exceptions, generated basic validation for the create functions which was 3 simple checks. 

Modifications: Used all code for the table and added extra conditions myself. 



Prompt 10: I attempted to create a record in a table which should not be possible due to foriegn key constraints, why did the database let me create it

AI Output: Explained that the foreign keys are not activited by default, gave me a function that would activate them in the __init__.py file.

Modifications: Found the exact generated function on stackoverload so I changed nothing


Prompt 11: How to cascade delete records in my tables

AI Output: Showed the parameter to put when defining foreign key constraints

Modification: Took the code it provided and used it where I defined my foreign keys.


Prompt 12: Is there a decimal type because float has too many decimal places

AI Output: Showed how to import decimal datatype and what it looked like in the models.py

Modification: Nothing just imported decimal and changed all my float rows to decimal


Prompt 13: Can you make a template for an account summary page that will display specifics about different accounts I have listed using bootstrap 

AI Output: Gave html + jinja code with bootstrap classes

Modification: Changed variable names, kept the rest as I liked the layout 


Prompt 14: I want to have an account summary page that will display specifics like win rate... how do I use aggregate functions to get the correct results.

AI Output: Generated querys using COUNT and so on.

Modification: No modifications it did exactly what I wanted.


Summary: There was a lot more prompting than what is listed. For example, when I ran into errors that would show up on the website I asked what could be causing it. I also got into some loops where nothing it suggested worked. The main crutch was with the complex queries using aggregate functions, theres still certain details I don't exactly understand to be able to do it all myself. These are just the main prompts that moved the project along. The rest I did myself using the help of "John Elder" on YouTube. 





