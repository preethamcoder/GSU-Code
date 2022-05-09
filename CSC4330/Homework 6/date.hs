data Date = Date 
  { month :: Int, 
    day   :: Int,
    year  :: Int
  } 
  deriving (Show, Eq)

leapYear :: Date -> Bool
leapYear num
    | ((year(num) `mod` 4 == 0) && ((year(num) `mod` 100 /= 0) || (year(num) `mod` 400 == 0))) = True
    | otherwise = False

daysMonth :: Date -> Int
daysMonth num 
    | month(num) == 1 || month(num) == 3 || month(num) == 5 || month(num) == 7 || month(num) == 8 || month(num) == 10 || month(num) == 12 = 31
    | month(num) == 4 || month(num) == 6 || month(num) == 9 || month(num) == 11 = 30
    | (month(num) == 2 && leapYear num == False) = 28
    | otherwise = 29

tomorrow :: Date -> Date
tomorrow num
    | day(num) < daysMonth num = Date (month(num)) (day(num)+1) (year(num))
    | (day(num) == daysMonth num) && (month(num) < 12) = Date (month(num)+1) (1) (year(num))
    | otherwise = Date 1 1 (year(num)+1)

yesterday :: Date -> Date
yesterday num
    | day(num) > 1 = Date (month(num)) (day(num)-1) (year(num))
    | (day(num) == 1) && (month(num) > 1) = Date (month(num)-1) (daysMonth(firstOfPreviousMonth(num))) (year(num))
    | otherwise = Date 12 31 (year(num)-1)

firstOfNextMonth :: Date -> Date
firstOfNextMonth num
    | month(num) < 12 = Date (month(num)+1) 1 (year(num))
    | otherwise = Date 1 1 (year(num)+1)

firstOfPreviousMonth :: Date -> Date
firstOfPreviousMonth num
    | month(num) > 1 = Date (month(num)-1) 1 (year(num))
    | otherwise = Date 12 1 (year(num)-1)

add :: Int -> Date -> Date
add num da
    | (day(da)+num) <= daysMonth da = Date (month(da)) (day(da)+num) (year(da))
    | otherwise = add (num-(daysMonth da + 1 - day(da))) (firstOfNextMonth(da))

sub :: Int -> Date -> Date
sub num da
    | (day(da)-num) > 1 = Date (month(da)) (day(da)-num) (year(da))
    | otherwise = sub (num - (day(da))) (Date (month(firstOfPreviousMonth(da))) (daysMonth(firstOfPreviousMonth(da))) (year(firstOfPreviousMonth(da))))

(>>>) :: Date -> Date -> Bool
(>>>) d1 d2
    | year(d1) > year(d2) = True
    | (month(d1) > month(d2)) && (year(d1) == year(d2)) = True
    | (day(d1) > day(d2)) && (month(d1) == month(d2)) && (year(d1) == year(d2)) = True
    | otherwise = False

(===) :: Date -> Date -> Bool
(===) d1 d2
    | (day(d1) == day(d2)) && (month(d1) == month(d2)) && (year(d1) == year(d2)) = True
    | otherwise = False

(<<<) :: Date -> Date -> Bool
(<<<) d1 d2
    | year(d1) < year(d2) = True
    | (month(d1) < month(d2)) && (year(d1) == year(d2)) = True
    | (day(d1) < day(d2)) && (month(d1) == month(d2)) && (year(d1) == year(d2)) = True
    | otherwise = False

daysBetween :: Date -> Date -> Int
daysBetween d1 d2
    | ((>>>) d1 d2) = daysBetween d2 d1
    | otherwise = ((numDays d2)-(numDays d1))

numDays :: Date -> Int
numDays da = ((year(da) * 365) +(prevMonths (da) (0) (month(da))) + (day(da))+(numLeap da))

prevMonths :: Date -> Int -> Int -> Int
prevMonths da num mo
  |month(da) == mo = prevMonths (Date (month(da)-1) (day(da)) (year(da))) (num) (mo)
  | month(da) > 1 && month(da) < mo = prevMonths (Date (month(da)-1) (day(da)) (year(da))) (num+daysMonth da) (mo)
  | mo == 1 = 0
  | otherwise = (num + daysMonth da)

numLeap :: Date -> Int
numLeap da 
    | month(da) > 2 = (year(da) `div` 4) - (year(da) `div` 100) + (year(da) `div` 400)
    | otherwise = ((year(da)-1) `div` 4) - ((year(da)-1) `div` 100) + ((year(da)-1) `div` 400)