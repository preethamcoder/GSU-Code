type Matrix = [[Int]]
type Column = [Int]
type Row = [Int]

removeColumn :: Matrix -> Int -> Matrix
removeColumn m n = map (\row -> take (n) row ++ drop (n+1) row) m

determinant :: Matrix -> Int
determinant []         = 0
determinant [[x]]      = x
determinant [[x, y], [a, b]] = x*b - a*y
determinant mat = foldr (+) 0 [((-1) ^ counter) * (head mat !! counter) * determinant(removeColumn (drop 1 mat) counter) | counter <- [0 .. tar]]
  where
    tar = length (head mat) - 1
