# Student Management System

Hello,
This repository contains Student Management System Project using python.

## General
This repository contains basic Student management System where one can Create, Update, Display and Delete the students from the system.
There are three files related to the project : 
- main.py
- mydb.py
- student_gui.py

I have showed the Graphical User Interface in this project. 

[GUI](https://github.com/ShrutiPatil2223/Student-Management-System/blob/main/GUI_Screenshot%20.png) of the project can be found here.
 
  
## 1. Git
I have never used git before, so being a novice user I am, while working on this project I got to know a lot about git. 
Things I learned from the git are - Clone, push, pull, commit, seamless integration with other tools like in my project, they are sonarcloud and Gitlab-CI.
And most important is how it helps to track the project activities.

 My Stats:

 [![GitHub Streak](https://github-readme-streak-stats.herokuapp.com/?user=ShrutiPatil2223&theme=cobalt)](https://github.com/ShrutiPatil2223)  

## 2. UML Diagrams 
For my project, I have used this 3 UML diagrams :
1. [Activity Diagram](https://github.com/ShrutiPatil2223/Student-Management-System/blob/0aaf8a70706785e4c1420de90f5653a4911635c3/UML%20diagrams_updated/Activity%20Diagram_update.jpg) - This Activity Diagram shows the workflow of the student managemnt system.
2. [Sequence Diagram](https://github.com/ShrutiPatil2223/Student-Management-System/blob/1cc59052e29656270753d4ac11e6e960a4bb97d3/UML%20diagrams_updated/sequence%20diagram_update.jpg) - This Sequence Diagram shows that connection and interaction between 3 objects via carrying out messages over the time.
3. [Use Case Diagram](https://github.com/ShrutiPatil2223/Student-Management-System/blob/main/UML%20diagrams_updated/use%20case%20UML.png) - This Use Case Diagram shows that interaction between user and student management system GUI.

## 3. DDD
I have drawn [Context Mapping Diagram](https://github.com/ShrutiPatil2223/Student-Management-System/blob/main/UML%20diagrams_updated/DDD_update.jpg) and 
[Core Domain Chart](https://github.com/ShrutiPatil2223/Student-Management-System/blob/18ca2a030b9d673bbfe34d9b58020f48a31e1f5f/UML%20diagrams_updated/DDD_updated_1.png) and [Event storming diagram](https://github.com/ShrutiPatil2223/Student-Management-System/blob/main/UML%20diagrams_updated/EVENT%20STORMING.png)


## 4. Metrics
[![SonarCloud](https://sonarcloud.io/images/project_badges/sonarcloud-white.svg)](https://sonarcloud.io/summary/new_code?id=ShrutiPatil2223_Student-Management-System)

I have used sonarcloud to analyze the quality of the code. 

These are the metrics listed below : 

- Quality Gate Status [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=ShrutiPatil2223_Student-Management-System&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=ShrutiPatil2223_Student-Management-System)

- Bugs [![Bugs](https://sonarcloud.io/api/project_badges/measure?project=ShrutiPatil2223_Student-Management-System&metric=bugs)](https://sonarcloud.io/summary/new_code?id=ShrutiPatil2223_Student-Management-System)

- Code Smells [![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=ShrutiPatil2223_Student-Management-System&metric=code_smells)](https://sonarcloud.io/summary/new_code?id=ShrutiPatil2223_Student-Management-System)

- Duplicated Lines [![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=ShrutiPatil2223_Student-Management-System&metric=duplicated_lines_density)](https://sonarcloud.io/summary/new_code?id=ShrutiPatil2223_Student-Management-System)

- Lines of Code [![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=ShrutiPatil2223_Student-Management-System&metric=ncloc)](https://sonarcloud.io/summary/new_code?id=ShrutiPatil2223_Student-Management-System)

- Maintainability Rating [![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=ShrutiPatil2223_Student-Management-System&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=ShrutiPatil2223_Student-Management-System)

- Security Rating [![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=ShrutiPatil2223_Student-Management-System&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=ShrutiPatil2223_Student-Management-System)

## 5. Clean Code Developement

Clean code Developement [Cheatsheet](https://github.com/ShrutiPatil2223/Student-Management-System/blob/8308fe13863e139d7bd8a0baf6685dc310d40d07/cheatsheet.txt) is here and example from the code.

Comments/Doctstrings : 
Use Docstrings or comments to explain the function/methods.
[Docstrings](https://github.com/ShrutiPatil2223/Student-Management-System/blob/main/mydb.py#L41 )

Naming Convention : Here, I have used functions name like create_student,display_students,update_student,delete_student-This follows the snake_case convention.
[Naming convention](https://github.com/ShrutiPatil2223/Student-Management-System/blob/main/student_gui.py#L72)

DRY (Don't Repeat Yourself): Reusable functions, modules, or libraries can help prevent code duplication. In sonarcloud metrics, we can see no duplication
Duplicated Lines [![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=ShrutiPatil2223_Student-Management-System&metric=duplicated_lines_density)](https://sonarcloud.io/summary/new_code?id=ShrutiPatil2223_Student-Management-System)

Multiple lines : Keep lines short and readable so that horizontal scrolling could be avoided. Maximum 79 characters. Break down the lines.
[multline code](https://github.com/ShrutiPatil2223/Student-Management-System/blob/main/student_gui.py#L39 )


## 6.& 7. Build and CI/CD
For me, point 6 and 7 are integrated. I have used Gitlab-CI for the build and Continuous Integration/Continuous Deployment. As I was searching for the build management tool, I got to know that Maven, Ant and Gradle are mainly used for java based project. As my project is in Python, hence I have used Gitlab-CI.

This is build stage screenshot [Build](https://github.com/ShrutiPatil2223/Student-Management-System/blob/81fce9d5673fa662e88b1bb6f299b6bbf75e1814/Gitlab-Build_Stage.png) - As I started exploring the Gitlab-CI tool, it does not support project with GUI. Hence I have just build mydb.py.

This is test stage screenshot [Test](https://github.com/ShrutiPatil2223/Student-Management-System/blob/main/Gitlab-Testing_stage.png) - In this stage I have ran my project's unttest_.py file.

This is screenshot of the whole [CI/CD](https://github.com/ShrutiPatil2223/Student-Management-System/blob/81fce9d5673fa662e88b1bb6f299b6bbf75e1814/Gitlab-CICD_pipeline.png) pipeline.


gitlab-ci file - Its a configuration file which contains build,test and deployment stages. It includes dependencies which triggers/automate the CI/CD pipeline. [yaml file](https://github.com/ShrutiPatil2223/Student-Management-System/blob/81fce9d5673fa662e88b1bb6f299b6bbf75e1814/gitlab-ci.yml)



CI/CD - [![pipeline status](https://gitlab.com/ShrutiPatil2223/Project-CICD/badges/main/pipeline.svg)](https://gitlab.com/ShrutiPatil2223/Project-CICD/-/commits/main)

## 8. Unit tests

I have imported unittest module for unit testing. Asserting method is used to check whether actual value from database and the expected values are equal or not.
I have written 2 small unit tests. They are both based on CRUD Operation. 

1. Creating a new student.

2. Update an existing student.

This is my [unittest_.py](https://github.com/ShrutiPatil2223/Student-Management-System/blob/d8dbb4f95e3443e5fc81d0a0dfa807f1a05219fd/unittest_.py) file.


## 9. IDE(Spyder)

I have used Spyder as an IDE for this project. Some of the features are Syntax highlighting, Auto indentation, one line execution, code folding and many more which makes Spyder a good IDE to use.

Shortcuts that I liked :

F5 - To run file

F9 - To run a selected line/lines

Ctrl + Tab - To move between editor files which are already open

Ctrl + L - Clears the console

Ctrl + ! - Comment/uncomment the lines


## 10. Domain Specific Language (DSL)

In my project, DSL file is related to the the project only.
I have written small dsl program which does the CRUD operation. To call the DSL dile, I have written a python program as an interpereter to call the DSL file. Everything is gettign stored in students.db database file. So, I have used SQLite Viewer Web App(Online website) to see my database file.

Here, is the attached [DSL file](https://github.com/ShrutiPatil2223/Student-Management-System/blob/84ab4e762cdc8137e1178a9c6e741711a08f25da/student.dsl) and [Interepreter file](https://github.com/ShrutiPatil2223/Student-Management-System/blob/84ab4e762cdc8137e1178a9c6e741711a08f25da/dsl_interpreter.py) and screenshot of the [students.db](https://github.com/ShrutiPatil2223/Student-Management-System/blob/84ab4e762cdc8137e1178a9c6e741711a08f25da/dsl_interpreter_db.png) after running interpreter file.

## 11. Functional Programming

To cover all the functional apsects, I have written a python program which calculates the age of the particular student.

- Side-Effect-Free Functions : get_student_age function is side effect free function which calculates age of the student.
[Fuctional Programming](https://github.com/ShrutiPatil2223/Student-Management-System/blob/main/functional_programming.py#L9 )

- Closure : make_course_filter function is an example of closure. It defines a nested function called course_filter, which takes the course argument from its enclosing scope and returns it. 
[Fuctional Programming](https://github.com/ShrutiPatil2223/Student-Management-System/blob/main/functional_programming.py#L13 )

- Higher-order function : The process_data function is a higher-order function because it takes another function (func) as an argument and applies it to each element of the students list using map from functools.
[Fuctional Programming](https://github.com/ShrutiPatil2223/Student-Management-System/blob/main/functional_programming.py#L5 )
  
- Final Data Structure : List named "students" is defined which containa instances of the "Student" class with various arguments.
[Fuctional Programming](https://github.com/ShrutiPatil2223/Student-Management-System/blob/main/functional_programming.py#L19 )
  
- Functions as Parameters and Return Values : The filter_math_students variable is assigned the result of calling make_course_filter('Math'), which returns a closure (course_filter function) that filters students based on their course. This demonstrates the use of functions as return values.
[Fuctional Programming](https://github.com/ShrutiPatil2223/Student-Management-System/blob/main/functional_programming.py#L26 )









