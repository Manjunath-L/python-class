USE AMAZON;

-- 1. 
select *
from emp e inner join dept d
on e.dno = d.dno;
 
-- 2.
select E.FNAME,E.LNAME,E.JOB,D.DNAME
from emp E inner join dept D
on e.dno = d.dno
WHERE E.JOB IN ('SALESMAN','MANAGER');

-- 3.
select E.*, D.DNAME , D.LID 
from emp E inner join dept D
on e.dno = d.dno
WHERE E.JOB IN ('SALESMAN','MANAGER','DEVELOPER') AND D.DNO IN (110,111,112) AND E.FNAME LIKE '__H%' ;


-- 4.
select E.FNAME,D.DNAME,concat(substr(E.FNAME,1,2),D.LID,YEAR(E.DOB)) AS 'PASSWORD'
from emp E inner join dept D
on e.dno = d.dno;

-- 5.
select E.FNAME,D.DNAME,L.LOCATION
FROM EMP E INNER JOIN DEPT D INNER JOIN location L
ON E.DNO = D.DNO AND D.LID = L.LID;
