-- Consultas 
SELECT * FROM employee
SELECT Ssn, COUNT (Essn) FROM employee e, dependent d where (e.Ssn = d.Essn);
SELECT * FROM dependent;
-----------------------------------------------------------------------------
SELECT Bdate, Address FROM employee
WHERE Fname = 'John' AND Minit = 'B' AND Lname = 'Smith';
-----------------------------------------------------------------------------
SELECT * FROM departament WHERE Dname = 'Research';
-----------------------------------------------------------------------------
SELECT Fname, Lname, Address
FROM employee, departament
WHERE Dname = 'Research' AND Dnumber = Dno;
-----------------------------------------------------------------------------
SELECT * FROM project;




-- Recuperando informações dos departamentos presentes em Stafford
SELECT Dname AS Department, Mgr_ssn AS Manager FROM departament d, dept_locations l
WHERE d.Dnumber = l.Dnumber;

-- padrão sql -> || no MySQL usa a função concat()
SELECT Dname AS Department, concat(Fname, ' ', Lname) FROM departament d, dept_locations l, employee e
WHERE d.Dnumber = l.Dnumber AND Mgr_ssn = e.Ssn;

-- Recuperando informações dos projetos em Stafford
SELECT * FROM project, departament WHERE Dnum = Dnumber AND Plocation = 'Stafford';

-- Recuperando informações sobre os departamentos e projetos localizados em Stafford
SELECT Pnumber, Dnum, Lname, Address, Bdate
FROM project, departament, employee
WHERE Dnum = Dnumber AND Mgr_ssn = Ssn AND
Plocation = 'Stafford';

-- Operadores Lógicos
SELECT * FROM employee WHERE Dno IN (3,6,9);

-- Expressões e alias
SELECT Bdate, Address
FROM EMPLOYEE
WHERE Fname = ‘John’ AND Minit = ‘B’ AND Lname = ‘Smith’;
---------------------------------------------------------
SELECT Fname, Lname, Address
FROM EMPLOYEE, DEPARTMENT
WHERE Dname = ‘Research’ AND Dnumber = Dno;

-- Recolhendo o valor do INSS-*
SELECT Fname, Lname, Salary, Salary*0.011 FROM employee;
SELECT Fname, Lname, Salary, Salary*0.011 AS INSS FROM employee;
SELECT Fname, Lname, Salary, round(Salary*0.011,2) AS INSS FROM employee;

-- definir um aumento de salário para os gerentes que trabalham no projeto associado ao ProdutoX
SELECT e.Fname, e.Lname, 1.1*e.Salary AS increased_sal FROM employee AS e,
works_on AS w, project AS p WHERE e.Ssn = w.Essn AND w.Pno = p.Pnumber AND p.Pname='ProductX';

-- Concatenando e fornecendo alias
SELECT Dname AS Department, concat(Fname, ' ', Lname) AS Manager FROM departament d, dept_locations l, employee e
WHERE d.Dnumber = l.Dnumber AND Mgr_ssn = e.Ssn;

-- Recuperando dados dos empregados que trabalham para o departamento de pesquisa
SELECT Fname, Lname, Address FROM employee, departament
WHERE Dname = 'Research' AND Dnumber = Dno;

-- Definindo alias para legibilidade da consulta
SELECT e.Fname, e.Lname, e.Address FROM employee e, departament d
WHERE d.Dname = 'Research' AND d.Dnumber = e.Dno;

