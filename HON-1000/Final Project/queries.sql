create database db100;
use db100;
drop table if exists SENATOR;
create table SENATOR (
  id       int not null auto_increment,
  lname    varchar(25),
  fname    varchar(25),
  birthday date,
  gender   char(1),
  state    char(2),
  party    varchar(20),
  url      varchar(50),
  twitter  varchar(50),
  facebook varchar(50),
  youtube  varchar(50),
  primary key (id)
);
create table HREP (
  id       int not null auto_increment,
  lname    varchar(25),
  fname    varchar(25),
  birthday date,
  gender   char(1),
  state    char(2),
  district int,
  party    varchar(20),
  url      varchar(50),
  twitter  varchar(50),
  facebook varchar(50),
  youtube  varchar(50),
  primary key (id)
);
#Query 1
select 'HREP' as ltype, state, lname, fname, gender, birthday from HREP where MONTH(birthday) = 10 union select 'SENATOR', state, lname, fname, gender, birthday from SENATOR where MONTH(birthday) = 10 order by ltype, state ASC, lname ASC;
#Query 2: One of the senators turned 50 a few days ago, so there is a small discrepency between values in the database!
select state, lname, fname, TIMESTAMPDIFF(YEAR, birthday, CURDATE()) as age
from SENATOR
where TIMESTAMPDIFF(YEAR, birthday, CURDATE()) < 50
order by TIMESTAMPDIFF(YEAR, birthday, CURDATE()) asc;
#Query 3
select state, count(lname) as NumHreps
from hrep
group by state
order by count(lname) desc; 
#Query 4
SELECT 'SENATOR' as 'TYPE', gender, COUNT(id) 
FROM SENATOR
GROUP BY gender
UNION 
SELECT 'HREP', gender, COUNT(id)
FROM HREP
GROUP BY gender;
#Query 5
select lname, fname, state from SENATOR where twitter = "" ORDER by state ASC, lname ASC;               
commit;
