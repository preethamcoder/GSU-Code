#GRANT all privileges on windowsext.* to root@localhost IDENTIFIED BY 'Passw0rd$' WITH GRANT OPTION;
	create database hackGSU;
	
  use hackGSU;
	
  DROP table if exists Information;
	
  DROP table if exists Attendees;
	
  drop table if exists EnrolledCourses; 
	
  create table Information(id BIGINT, firstName varchar(200), lastName varchar(200));
	
  insert into Information values (2000121193, "Preetham", "Thelluri");
	
  insert into Information values (2000121194, "Nachiket", "Hinge");
	
  insert into Information values (2000121195, "John", "Gunerli");
	
  insert into Information values (2000121176, "Joe", "India");
	
  insert into Information values (2000121196, "Sam", "Gunerli");
	
  insert into Information values (2000121125, "Jo", "Gu");
	
  insert into Information values (2000121188, "Jill", "American");
	
  insert into Information values (2000121215, "Donald", "Trump");
	
  insert into Information values (1111111111, "Joe", "Biden");
	
  insert into Information values (1234554321, "Shah Rukh", "Khan");
	
  insert into Information values (1234567891, "Sanjivika", "Pani");
	
  insert into Information values (1234567892, "Virat", "Kohli");
	
  insert into Information values (1234567893, "John", "Sharma");
	
  insert into Information values (1234567890, "Gyandeep", "Reddy");
	
  select * from Information ORDER BY ID;
	
  create table Attendees(id BIGINT, fname varchar(20), lname varchar(20), crn varchar(20));
	
  insert into Attendees values (2000121193, "Preetham", "Thelluri", "ECON2105");
	
  select * from Attendees;
	
  insert into Attendees values (1234567891, "Sanjivika", "Pani", "ECON2105");
	
  create table EnrolledCourses(id BIGINT, crn varchar(10));
	
  insert into EnrolledCourses values(1234567891, "CSC1302");
	
  insert into EnrolledCourses values(1234567890, "CSC1301");
	
  insert into EnrolledCourses values(1234567891, "HON1000");
	
  insert into EnrolledCourses values(1234567890, "HON1000");
	
  insert into EnrolledCourses values(2000121193, "HON1000");
	
  insert into EnrolledCourses values(2000121194, "HON1000");
	
  insert into EnrolledCourses values(2000121193, "CSC3320");
	
  insert into EnrolledCourses values(2000121193, "CSC2510");
	
  insert into EnrolledCourses values(2000121194, "MATH2215");
	
  insert into EnrolledCourses values(2000121195, "MATH2212");
	
  insert into EnrolledCourses values(2000121195, "MATH2652");
	
  insert into EnrolledCourses values(1234567892, "HON1000");
	
  insert into EnrolledCourses values(1234567892, "MATH2215");
	
  insert into EnrolledCourses values (2000121196, "ECON2105");
	
  insert into EnrolledCourses values (2000121196, "ECON2106");
	
  insert into EnrolledCourses values (1234554321, "ECON2105");
	
  insert into EnrolledCourses values (1234554321, "ECON2106");
	
  insert into EnrolledCourses values (2000121193, "ECON2105");
	
  select * from EnrolledCourses;
	
  create table Courses(crn varchar(20), stime varchar(20), etime varchar(20), day1 varchar(12), day2 varchar(12));
	
  insert into Courses values("CSC1301", "09:00:00", "10:50:00", "Tuesday", "Thursday");
	
  insert into Courses values("CSC1302", "09:00:00", "10:50:00", "Tuesday", "Thursday");
	
  insert into Courses values("CSC2510", "09:00:00", "10:50:00", "Tuesday", "Thursday");
	
  insert into Courses values("CSC3320", "09:00:00", "10:50:00", "Tuesday", "Thursday");
	
  insert into Courses values("HON1000", "09:30:00", "10:20:00", "Monday", "Monday");
	
  insert into Courses values("MATH2211", "10:30:00", "12:20:00", "Monday", "Wednesday");
	
  insert into Courses values("MATH2212", "10:30:00", "12:20:00", "Monday", "Wednesday");
	
  insert into Courses values("MATH2215", "10:30:00", "12:20:00", "Monday", "Wednesday");
	
  insert into Courses values("MATH2652", "10:30:00", "12:20:00", "Monday", "Wednesday");
	
  insert into Courses values("ECON2105", "12:45:00", "14:05:00", "Monday", "Friday");
	
  insert into Courses values("ECON2106", "14:20:00", "15:40:00", "Monday", "Friday");
	
  update Courses SET stime = "12:45:00", day1 = "Monday" where crn = "ECON2105" or CRN = "ECON2106";
	
  select * from Courses;
	
  commit;
  
