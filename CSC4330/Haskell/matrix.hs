type Matrix = [[Int]]
type Column = [Int]
type Row = [Int]

removeColumn :: Matrix -> Int -> Matrix
removeColumn m n = map (\row -> take (n-1) row ++ drop (n) row) m

determinant :: Matrix -> Int
determinant []         = 0
determinant [[x]]      = x
determinant [[x, y], [a, b]] = x*b - a*y
determinant mat = foldr (+) 0 [((-1) ^ counter) * (head mat !! counter) * determinant(removeColumn (drop 1 mat) (1+counter)) | counter <- [0 .. tar]]
  where
    tar = length (head mat) - 1
