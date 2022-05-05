import Data.Char
import Data.List

factorial :: Int -> Int
factorial 0 = 1
factorial 1 = 1
factorial n
  | n < 0 = 0
  | otherwise = foldr (*) 1 [1..n]

wordValue :: String -> Int
wordValue inp
  | otherwise = foldr (+) 0 (converter inp)

converter :: String -> [Int]
converter [] = [0] 
converter (x:xs) = [(ord (toLower x) - 96)] ++ converter xs

longest :: [String] -> String
longest inp = foldl (\each word -> if length each > length word then each else word) "" inp

rmdups :: [Int] -> [Int]
rmdups [] = []
rmdups ys = foldl join [] ys

join :: [Int] -> Int -> [Int]
join [] x  = [x]
join xs x
  | (last xs == x) = xs
  | otherwise = xs ++ [x]

minmax :: [Int] -> (Int,Int)
minmax [] = (minBound :: Int, maxBound :: Int)
minmax lst = (minn lst, maxn lst)

maxn :: [Int] -> Int
maxn [] = minBound :: Int
maxn lst = foldl (max) (minBound :: Int) lst

minn :: [Int] -> Int
minn [] = maxBound :: Int
minn lst = foldl (min) (maxBound :: Int) lst
