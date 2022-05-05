type Matrix = [[Int]]
type Column = [Int]
type Row = [Int]

transpose :: Matrix -> Matrix
transpose [] = []
transpose mat = [extractColumn mat n | n <- [0 .. l]] where l = length (head mat) - 1

matrixMultiply :: Matrix -> Matrix -> Matrix
matrixMultiply mtrixa mtrixb = [rowMul row mtrixb | row <- mtrixa]

determinant :: Matrix -> Int
determinant [] = 0
determinant [[k]] = k
determinant mat = sum [((-1) ^ cc) * (head mat !! cc) * determinant (removeColumn (drop 1 mat) cc) | cc <- [0 .. l]]
  where
    l = length (head mat) - 1

extractColumn :: Matrix -> Int -> Column
extractColumn mat n = [row !! n | row <- mat]

removeColumn :: Matrix -> Int -> Matrix
removeColumn mat ind = transpose (take ind t ++ drop (1+ind) t) where t = transpose mat

scalarProduct :: Row -> Row -> Int
scalarProduct xs ys = sum [x * y | (x, y) <- zip xs ys]

rowMul :: Row -> Matrix -> Row
rowMul row matrix = [scalarProduct row col | col <- transpose matrix]
