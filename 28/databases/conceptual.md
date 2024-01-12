### Conceptual Exercise

Answer the following questions below:

- What is PostgreSQL?
    It is a language used to communicate with and structure databases

- What is the difference between SQL and PostgreSQL?
    SQL supports Java, JS whereas PostgreSQL supports a much wider range of languages

- In `psql`, how do you connect to a database?
    \c databaseName

- What is the difference between `HAVING` and `WHERE`?
    Having refers to groups and Where looks for a specific Rows 

- What is the difference between an `INNER` and `OUTER` join?
    An Inner join includes all the fields that have a parameter from both databases that are linked. Outer does the opposite

- What is the difference between a `LEFT OUTER` and `RIGHT OUTER` join?
    Left or Right refers to the database being joined on or being joined into

- What is an ORM? What do they do?
    An ORM would be like SQLAlchemy. It allows you to use code in python to make queries to a database by translating the queries back and forth.

- What are some differences between making HTTP requests using AJAX 
  and from the server side using a library like `requests`?
    Client side requests through AJAX could potentially be faster given it can talk directly to the API server. However, it is possibly easier to to use server side requests because they are all being sent and recieved through the same channel.
    
- What is CSRF? What is the purpose of the CSRF token?
    The token helps to ensure that the person making the request to the server is the intended party. It sends a generated token in the body of the HTML that is checked and verified otherwise it throws an error.
- What is the purpose of `form.hidden_tag()`?
    This tag hides the CSRF Token when iterating through the fields in the form when using WTForms.
