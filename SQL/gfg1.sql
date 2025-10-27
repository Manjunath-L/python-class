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

SELECT * FROM student;

ALTER TABLE student
add Department VARCHAR(50);

UPDATE student
SET Department = 'Computer Science'
where StudentID = 1;

select age from student;

DROP TABLE student;

TRUNCATE TABLE  student;

alter table student modify age bigint;