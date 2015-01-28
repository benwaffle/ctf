Zach: Injection 1 (90 pts)

Taking a look at the source code, it’s clear that there is no escaping of the strings before they are put into the SQL query. So, I just left the password field blank and put this in the username field: 
    `' OR username=(SELECT username FROM users LIMIT 1) OR '1'='1`
This creates the following query:
    `SELECT * FROM users WHERE username='' OR username=(SELECT username FROM users LIMIT 1) OR '1'='1' AND password=''`
Since AND is evaluated before OR, the last two logical statements evaluate to true AND false, creating false. The first statement evaluates to false. So the whole statement becomes false OR username=(SELECT username FROM users LIMIT 1) OR false. username will then match the one username returned from the subquery, allowing for a table to be returned with only one row.

flag: `flag_vFtTcLf7w2st5FM74b`
