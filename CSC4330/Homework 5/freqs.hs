import Data.List
import Data.Char

frequencies :: String -> [(Char,Int)]
frequencies inp
  | (inp == []) = []
  | otherwise = map (\letter -> (head letter, length letter)) . group . sort $ lower inp

lower :: String -> String
lower inp = map toLower inp
