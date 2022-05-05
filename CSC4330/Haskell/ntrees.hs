data NTree a = Nil | Tree a [NTree a] deriving Show

sumElements :: NTree Int -> Int
sumElements Nil = 0
sumElements (Tree n1 n2) = foldr (+) n1 (map sumElements n2)

heightNTree :: NTree Int -> Int
heightNTree Nil = 0
heightNTree (Tree n1 []) = 0
heightNTree (Tree n1 n1s) = foldr (+) 1 [0, maximum (map heightNTree n1s)]

preOrder :: NTree Int -> [Int]
preOrder Nil = []
preOrder (Tree n1 n2) = [n1] ++ foldr (++) [] (map preOrder n2)
