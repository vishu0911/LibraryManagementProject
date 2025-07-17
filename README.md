# 📚 Library Management System using Python & MySQL

This project is a simple **Library Management System** developed using **Python (Tkinter)** and **MySQL**. It helps manage student/staff book records including issuing, returning, and fine tracking through a user-friendly graphical interface.

---

## 🚀 Features

- Add, update, and delete library member details
- Issue books with borrow and return dates
- Auto-calculate fine for late returns
- Built-in GUI using Tkinter
- MySQL backend to store records securely

---

## 🛠️ Tech Stack

- **Python 3**
- **Tkinter** (GUI)
- **MySQL** (Database)
- **MySQL Connector for Python**

---

## 📂 How to Run the Project

### 1. Clone the Repository


git clone https://github.com/your-username/LibraryManagementProject.git

/*Install Required Packages*/

pip install mysql-connector-python

/*Setup MySQL Database*/

Open MySQL Workbench

Create a database named: library_db

Use the below SQL command to create a table:

/*SQL Code of Project Library Management System.*/<img width="1347" height="715" alt="FrontEnd" src="https://github.com/user-attachments/assets/304c3ad6-faa4-483a-8839-0a70f512022e" />



CREATE TABLE IF NOT EXISTS library (
    Member VARCHAR(50) NOT NULL,
    PRN_NO VARCHAR(20) PRIMARY KEY,
    ID INT NOT NULL PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Address1 VARCHAR(100),
    Address2 VARCHAR(100),
    PosdId VARCHAR(20),
    Mobile VARCHAR(20),
    BookId VARCHAR(20),
    BookTitle VARCHAR(100),
    Author VARCHAR(100),
    DateBorrow VARCHAR(100),
    DateDue VARCHAR(100),
    DaysOnBook VARCHAR(100),
    LateReturn VARCHAR(100),
    DateOverdue VARCHAR(100),
    FinalPrice VARCHAR(100)
);




