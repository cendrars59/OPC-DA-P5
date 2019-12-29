# 1. Project

## 1.1 Purpose 
This project has been created in a context of Application developer learning path provided by OpenClassRooms. This project is a pratice for evaluation. The practice description is [here](https://openclassrooms.com/fr/projects/157/assignment) (Description in French)

## 1.2 Description

### 1.2.1 Description of the user path
The user is on the terminal. The latter displays the following choices:

* 1 - What food do you want to replace?
* 2 - Find my substituted foods.

The user selects 1. The program asks the user the following questions and the user selects the answers:

Select the category. [Several propositions associated with a number. The user enters the corresponding digit and presses enter]
Select the food. [Several propositions associated with a number. The user enters the number corresponding to the selected food and presses enter]
The program offers a substitute, its description, a store or buy it (if applicable) and a link to the Open Food Facts page for this food.
The user then has the possibility to save the result in the database.
 

### 1.2.2 Description of the user path features

* Food search in the Open Food Facts database.
* The user interacts with the program in the terminal, but if you want to develop a graphical interface you can,
* If the user enters a character that is not a number, the program must repeat the question,
* The research must be carried out on a MySql database.

# 2. Project structure 

## 2.1 DataBase

### 2.1.1 Database installation 

The used database for this project is MySQL community server edition 8.0.18. You can download download directly [here](https://dev.mysql.com/downloads/mysql/).
According your O.S. follow the setup guide provided by the editor. 

### 2.1.2 Physical Schema
You can review the physical schema located into the following directory 

```
project
│   README.md   
│   ...
└───Database
│   └───Schema
│       │   P5-DataModel.mwb

```

The schema can be reviewed with MySQL Workbench. Link to install it [here](https://dev.mysql.com/downloads/workbench/)

### 2.1.3 Database script

The database script has been made for MySQL exclusively. You can find the creation script as described here under. 

```
project
│   README.md   
│   ...
└───Database
│   └───Script
│       │   DAPYP5OpenFood.sql

```

## 2.2 Third part softwares

### 2.2.1 Python version 
The solution has been developped from 3.7.5 Python version -> see [Release note](https://www.python.org/downloads/release/python-375/)

### 2.2.2 MySQL Python connector 
In order to access to database from installation. You have to set up the Python MySQL connector 8.0.18. Please find the link to download [here](https://dev.mysql.com/downloads/connector/python/)

### 2.2.3 OpenFoodFacts API

The setting of the OpenFoodFacts is required for the application usage. You can find the setting procedure for Python [here](https://github.com/openfoodfacts/openfoodfacts-python)


# 3. Using application 