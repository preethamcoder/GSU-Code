import Data.Char

convertNum2Binary :: Int -> String
convertNum2Binary 0 = ""
convertNum2Binary num = convertNum2Binary(num `div` 2) ++ show (num `mod` 2)

convertFraction2Binary :: Float -> String
convertFraction2Binary 0 = ""
convertFraction2Binary num = convertNum2Binary(truncate num) ++ "." ++ lim (snd(properFraction num)) ""

lim :: Float -> (String -> String)
lim nm res
    | length res == 23 = res
    | nm == 0 = res
    | otherwise = lim (snd(properFraction(nm * 2))) (res ++ show (fst(properFraction(nm * 2))))