singleDigit :: Int -> Int
singleDigit 0 = 0
singleDigit num
    | (num < 10) = num
    | otherwise = singleDigit((num `rem` 10) + (num `div` 10))
