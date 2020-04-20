
# Instructions to access Database

## Installation:

- 	Install MySQL, Python, Node Package Manager with all the environment variables set up.

-	Download mysql module for JS
	npm install mysql
	(Install in same folder as the JS code)

-	Download mysql-connector module using pip for python

## Usage:

-	Run the following code on MySQL

	`ALTER USER 'root'@'localhost' IDENTIFIED WITH 	mysql_native_password BY 'password'`

	Where root as your user localhost as your URL and password 	as your password

	Then run this query to refresh privileges:

	`flush privileges;`

	Try connecting using node after you do so.

	If that doesn't work, try it without @'localhost' part.
	
-	MySQL :
	
	`create database project;`
	
	`use project;`
	
	`create table project(word varchar(100), count integer(10));` // 'word' can be added as primary key depending on our usage
	`desc project;` // to check the table definition 
	
	`select * from project;` //to view the records

-	For Python dictionary to SQL, check examples uploaded.

-	For Visualization, it is convenient to use dataframes, hence convert the SQL data to dataframes (JS)
	
	npm install dataframe-js	//install library
	(Check uploaded example for usage)

-	For SQL to JS to CSV (Optional), download the dependencies first : 

	1. fast-csv 
	
	2. fs 
	
	3. csv-writer
