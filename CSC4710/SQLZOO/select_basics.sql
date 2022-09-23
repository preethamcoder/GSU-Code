/* ALL QUESTIONS ARE IN ORDER. QUIZ Answers in here too*/
SELECT population FROM world
  WHERE name = 'Germany'
  
SELECT name, population FROM world
  WHERE name IN ('Sweden', 'Norway', 'Denmark');
  
 SELECT name, area FROM world WHERE area BETWEEN 200000 AND 250000
 
 -- Quiz
 SELECT name, population FROM world WHERE population BETWEEN 1000000 AND 1250000
 
 -- Table-E for question 2
 
 SELECT name FROM world WHERE name LIKE '%a' OR name LIKE '%l'
 
 -- The table with Italy, Malta, and Spain for question 4
 
 -- Andorra 936 for question 5
 
 SELECT name, area, population FROM world WHERE area > 50000 AND population < 10000000
 
 SELECT name, population/area FROM world WHERE name IN ('China', 'Nigeria', 'France', 'Australia')
