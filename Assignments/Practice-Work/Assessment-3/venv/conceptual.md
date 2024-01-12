### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?
  - Javascript is front end and backend  Python is Back end
  - code blocs are defined differently

- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.
  
  - you can use a try-catch statement that will attempt to retrieve the value
  at key "c"

- What is a unit test?
  - they take results from only one thing such as a function

- What is an integration test?
  - they test the interaction between multiple elements of your application

- What is the role of web application framework, like Flask?
  - They are meant to simplify and make the task of communicating with servers
  easier for humans to process

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?
  - the parameter in the route url is hard coded and would be good as a foundation page
  however if you want a dynamic url that takes user input into consideration the query
  param would be better

- How do you collect data from a URL placeholder parameter using Flask?
  - if you take the desired vairable name and encase it in "<>". You can
  then pass the variable of the same name into the function

- How do you collect data from the query string using Flask?
  - you would use the request.args.get() method

- How do you collect data from the body of the request using Flask?
  - request.args.get()

- What is a cookie and what kinds of things are they commonly used for?
  - A cookie is tiny bytes of data save on the browser at the request of the server.
  It is then sent back to the server with future request to the server

- What is the session object in Flask?
  - session uses cookies to store larger amounts of data in a safer manner.

- What does Flask's `jsonify()` do?
  - it attempts to convert strings to json readable text
