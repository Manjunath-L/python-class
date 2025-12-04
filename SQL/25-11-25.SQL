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


-- 27-11-25
select *
from emp e left outer join dept d 
on e.dno = d.dno;

select *
FROM EMP E right outer join dept D
ON E.DNO = D.DNO;

select L.LOCATION
FROM  location L left outer join customer C
ON C.LID = L.LID
where C.CID IS  null;

select P.*
FROM  product P left outer join customer C
ON P.PRODUCT_ID = C.PRODUCT_ID
where C.ORDER_ID IS null;

select P.*
from customer C right outer join product P 
ON C.PRODUCT_ID = P.PRODUCT_ID
where C.ORDER_ID IS NULL;

select L.LOCATION
from dept D right outer join location L
ON D.LID = L.LID
where D.LID IS NULL;

-- 28-11-25
select e1.fname,e1.sal,e2.fname,e2.sal
from emp e1 join emp e2
on e1.mgr = e2.eid
where e1.sal > 35000 and e2.sal < 500000;


select e1.fname,e1.job,e2.FNAME,e2.job,d1.DNAME,d2.dname
from emp e1 join emp e2 inner join dept d1 inner join dept d2
on e1.mgr = e2.eid and e1.dno = d1.dno and e2.DNO = d2.DNO
where e1.job in ('manager','salesman') and d1.DNAME in ('MARKETING','DELIVERY') and e2.JOB in ('manager');

select e1.*
from emp e1 join emp e2
on e1.sal  > e2.sal
where e2.fname = "karan";

select *
from emp e natural join location l;

-- emp=left 
(select *
from emp e left outer join dept d
on e.dno = d.dno)
union
(select *
from emp e  right outer join dept d
on e.dno = d.dno);

(select fname
from emp)
union
(select fname
from emp);

(select fname
from emp)
union all
(select fname
from emp);

(select fname , job
from emp)
union 
(select fname , JOB
from emp);

(select fname 
from emp)
union 
(select JOB
from emp);

set autocommit = 0;

create table emp
(
id int,
name varchar(20));

insert into emp values (1,"yeash"),(2,"dboos");

select fname,sal,dno ,row_number() over(partition by dno order by sal desc) AS 'Rank'
from emp;
select fname,sal,dno ,row_number() over(order by sal desc) AS 'Rank'
from emp;
select fname,sal,dno ,rank() over(order by sal desc) AS 'Rank'
from emp;
select fname,sal,dno ,rank() over(partition by dno order by sal desc) AS 'Rank'
from emp;

select fname,sal,dno ,dense_rank() over(order by sal desc) AS 'Rank'
from emp;

select e1.*
from emp e1
where e1.sal > (select avg(e2.SAL) from emp e2 where e1.dno = e2.dno);
SELECT E.FNAME
FROM EMP E 
WHERE E.DOB < (SELECT M.DOB FROM EMP M WHERE M.EID = E.MGR); 
