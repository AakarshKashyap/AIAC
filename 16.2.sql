-- 1. Display all records
SELECT * FROM employees;

-- 5. Find employees from IT department
SELECT * FROM employees WHERE department = 'IT';

-- 7. Show employees in ascending order of salary
SELECT * FROM employees ORDER BY salary ASC;

-- 11. Find highest and lowest salary
SELECT MAX(salary), MIN(salary) FROM employees;

-- 20. Count employees in each department
SELECT department, COUNT(*) FROM employees GROUP BY department;
