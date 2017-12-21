# Library-Website

It is a un-finished Library-Website

Basically, I built it up with Python, HTML5, Python  3.0,, Django, Pycharm, and some CSS template.

It includes the function for users to search books, to borrow, and to chech it's status. Also, it has the functions for clerks to check the borrow history and the INSERT/UPDATE/CREATE in SQL query with sqlite.

I would like to explain the structure and how it operate briefly 


Step 1.
We need to create the Date with its' attributes firstly. So, go to th models.py and code in some data you want to insert into it.


Step 2.
Go to the python file: 'Apps.py'. Code with one name, which you can eventually go to the admin side(superuser) to manage the whole system. It is critial and will be very helpyful if you do so.


Step 3.
Go to the python file; "admin.py". This step is for importing the models that you had bullt before. You need to import them into the administration mode for manage those data easily. 


Step 4.
Build the Html file for the page for every browser. Further more, yoy need to build some click bottom in this step or some searching bar and the type of input for the searching bar(the the Exception catch stuff, after all you do want the Web shot up suddenly for the typo in unexpected form, right?)
 
 
Step 5.
Go to the 'urls.py' for setting the path(url) for every commanded-input from the HTML.

Step 6.
Now, we go back to 'view.py' to make so def function. The function import the models, HTML, and also the urls.  def function should able to notify whcih html(page) and the url(next page), the most importantly, the operating in the models. Then, all of the results will be presented in the screen for the uesrs or clerks. Good luck and wish all the best. 
