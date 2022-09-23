/* All questions are in order, as always */

select name, continent, population FROM world

select name FROM world WHERE population >= 200000000

selectT name, GDP/population from world where population >= 200000000

select name, population/1000000 from world where continent = 'South America'

select name, population from world where name in ('France', 'Germany', 'Italy')

select name from world where name like '%United%'

select name, population, area from world where population > 250000000 or area > 3000000

SELECT name, population, area FROM world WHERE (area > 3000000) XOR (population > 250000000)

SELECT name, ROUND(population/1000000, 2), ROUND(GDP/1000000000, 2) FROM world WHERE continent = 'South America'

SELECT name, ROUND(GDP/population, -3) FROM world WHERE GDP > 1000000000000

SELECT name, capital from world where LEN(name) = LEN(capital)

select name, capital from world where name <> capital and LEFT(name, 1) = LEFT(capital, 1)

SELECT name FROM world WHERE name NOT LIKE '% %' and name like '%a%' and name like '%e%' and name like '%o%' and name like '%i%' and name like '%u%'
