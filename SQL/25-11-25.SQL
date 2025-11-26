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

-- 26 - 11 - 25 
-- 6.
select C.FIRST_NAME,C.ORDER_ID,O.ORDER_DATE,P.PRICE AS 'TOTAL_PRICE' ,L.LOCATION,L.CITY,L.STATE 
from customer C inner join orders O inner join product P inner join location L 
ON C.LID = L.LID AND C.PRODUCT_ID = P.PRODUCT_ID AND C.ORDER_ID = O.ORDER_ID
where C.ORDER_ID IS NOT NULL;

-- 7.
select L.STATE,SUM(P.PRICE) AS "REVENUE"
FROM customer C inner join product P inner join location L
ON C.PRODUCT_ID = P.PRODUCT_ID AND C.LID = L.LID
group by L.STATE;

-- 8.
select C.FIRST_NAME,SUM(P.PRICE) AS 'SPENT_MONEY'
FROM customer C inner join product P 
ON C.PRODUCT_ID = P.PRODUCT_ID
group by C.FIRST_NAME 
order by SPENT_MONEY DESC
limit 2;

-- 9.
SELECT E.FNAME , D.DNAME ,L.LOCATION
FROM EMP E inner join DEPT D INNER join location L 
ON E.DNO = D.DNO AND D.LID = L.LID
where D.LID IN (1,2,4) AND D.DNAME LIKE '%D%'AND E.DOJ between '2019-01-01' AND '2021-12-31'; 


-- 10. 
SELECT C.FIRST_NAME, C.ORDER_ID,P.PNAME,P.PRICE,O.DELIVERY_DATE,L.CITY
FROM customer C INNER join product P INNER join orders O INNER join location L 
ON C.PRODUCT_ID = P.PRODUCT_ID AND C.ORDER_ID = O.ORDER_ID AND C.LID = L.LID
where L.CITY = "MUMBAI" AND C.ORDER_ID IS not null;