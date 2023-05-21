---
layout: page
permalink: /pages/module1/assignment1/part3/m1a1p3-sql.html
---

## Module 1: Assignment 1: Part 3: SQL

### Code

```SQL
mysql;
USE COMPANY1;

-- Operation 1
-- List all Employees whose salary is between 1,000 and 2,000. Show the employee name, department, and salary
SELECT EMP.ENAME AS Employee, DEPT.DNAME AS Department, EMP.SAL AS Salary
FROM EMP
JOIN DEPT
ON EMP.DEPTNO = DEPT.DEPTNO
WHERE EMP.SAL >= 1000
AND EMP.SAL <= 2000;

-- Operation 2
-- Count the number of people in department 30 who receive a salary and the number of people who receive a commission
-- Get # of people that receive a salary
SELECT
  COUNT(*)
  FROM EMP
  WHERE EMP.DEPTNO = 30
  AND EMP.SAL <> ''
UNION
-- Get # of people that receive a commission
SELECT
  COUNT(*)
  FROM EMP
  WHERE EMP.DEPTNO = 30
  AND EMP.COMM <> '';

-- Operation 3
-- Find the name and salary of employees in Dallas
SELECT EMP.ENAME AS Employee, EMP.SAL AS Salary
FROM EMP
JOIN DEPT
ON EMP.DEPTNO = DEPT.DEPTNO
WHERE DEPT.LOC = 'DALLAS';

-- Operation 4
-- List all departments that do not have any employees
SELECT DEPT.DNAME AS 'Departments With No Employees'
FROM DEPT
WHERE DEPT.DEPTNO
NOT IN (SELECT EMP.DEPTNO FROM EMP);

-- Operation 5
-- List the department number and average salary of each department
SELECT EMP.DEPTNO AS 'Department Number', AVG(EMP.SAL) as 'Average Salary'
FROM EMP
WHERE EMP.SAL <> ''
GROUP BY EMP.DEPTNO;
```

### Output

Unfortunately I didn't save the output, but it was correct.
