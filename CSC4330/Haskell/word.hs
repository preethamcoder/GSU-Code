import Data.Char

lowercase :: String -> String
lowercase str = map toLower str

strtoInt :: String -> [Int]
strtoInt [] = []
strtoInt (x:xs) = [ord x - 96] ++ strtoInt xs

finalSum :: [Int] -> Int
finalSum [] = 0
finalSum (x:xs) = x + finalSum xs

wordValue :: String -> Int
wordValue inp
    | (inp == []) = 0
    | otherwise = finalSum(strtoInt(lowercase(inp)))
