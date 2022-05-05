import Data.Char
import Data.List

extractDigits :: Int -> [Int]
extractDigits num
    | num < 10 = [num]
    | otherwise = extractDigits(num `div` 10) ++ [num `rem` 10]

noDupes :: (Ord a) => [a] -> Bool
noDupes xs = (length (nub xs) == length xs)

noRepeatingDigits :: Int -> Bool
noRepeatingDigits nume
    | (nume < 0 && nume >= -10) = True
    | nume < 0 = False
    | (nume >= 0 && nume <= 10) = True
    | otherwise =  noDupes(extractDigits(nume))

numBulls :: Int -> Int -> Int
numBulls n1 n2
    | (noRepeatingDigits n1 && noRepeatingDigits n2 && length (extractDigits n1) == length (extractDigits n2)) = positionMatch (extractDigits n1) (extractDigits n2)
    | otherwise = -1

positionMatch :: [Int] -> [Int] -> Int
positionMatch [] [] = 0
positionMatch (x:xs) (y:ys)
    | x == y    = 1 + (positionMatch xs ys)
    | otherwise = (positionMatch xs ys)

numCows :: Int -> Int -> Int
numCows n1 n2
    | noRepeatingDigits n1 && noRepeatingDigits n2 && length (extractDigits n1) == length (extractDigits n2) = evalLists (extractDigits n1) (extractDigits n2) 0
    | otherwise = -1

checkIfInIt :: [Int] -> Int -> Bool
checkIfInIt [] n = False
checkIfInIt (x:xs) n
    | n == x = True || checkIfInIt xs n
    | otherwise = False || checkIfInIt xs n

checkIfIdenticalPos :: [Int] -> Int -> Int -> Int -> Int
checkIfIdenticalPos [] x yInd xInd = 0
checkIfIdenticalPos (y:ys) x yInd xInd
    | y == x && yInd /= xInd = 1
    | otherwise = 0 + checkIfIdenticalPos ys x (yInd + 1) xInd

evalLists :: [Int] -> [Int] -> Int -> Int
evalLists [] y _ = 0
evalLists (x:xs) ys xInd
    | checkIfInIt ys x == True = evalLists xs ys (xInd+1) + checkIfIdenticalPos ys x 0 xInd
    | otherwise = 0 + evalLists xs ys (xInd+1)
