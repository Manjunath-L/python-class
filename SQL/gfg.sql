USE school;
CREATE TABLE Student (
    StudentID INT PRIMARY KEY,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50),
    Age INT CHECK (Age >= 16),
    Email VARCHAR(100) UNIQUE
);

INSERT INTO Student (StudentID, FirstName, LastName, Age, Email)
VALUES 
(1, 'Aarav', 'Sharma', 20, 'aarav.sharma@example.com'),
(2, 'Meera', 'Verma', 19, 'meera.verma@example.com'),
(3, 'Ravi', 'Patel', 18, 'ravi.patel@example.com');


create database amazon;
use amazon;