data BST a = Nil | Tree a (BST a) (BST a) deriving Show

sizeBST :: BST Int -> Int
sizeBST Nil = 0
sizeBST (Tree _ left right) = 1 + sizeBST left + sizeBST right

heightBST :: BST Int -> Int
heightBST Nil = -1
heightBST (Tree _ left right) = 1 + max (heightBST left) (heightBST right)

minBST :: BST Int -> Int
minBST Nil = 0
minBST (Tree tree Nil _) = tree
minBST (Tree tree left _) = minBST left

maxBST :: BST Int -> Int
maxBST Nil = 0
maxBST (Tree tree _ Nil) = tree
maxBST (Tree tree _ right) = maxBST right

memberBST :: Int -> BST Int -> Bool
memberBST _ Nil = False
memberBST root (Tree tree left right) 
    | root == tree = True
    | root < tree = memberBST root left
    | root > tree = memberBST root right

insertBST :: Int -> BST Int -> BST Int
insertBST root Nil = Tree root Nil Nil
insertBST root (Tree tree left right)
    | tree == root = Tree tree left right
    | tree < root = Tree tree left (insertBST root right)
    | tree > root = Tree tree (insertBST root left) right

deleteBST :: Int -> BST Int -> BST Int
deleteBST _ Nil = Nil
deleteBST ninja (Tree rt left right)
  | ninja == rt = delete (Tree rt left right)
  | ninja < rt = Tree rt (deleteBST ninja left) right
  | ninja > rt = Tree rt left (deleteBST ninja right)

delete :: BST Int -> BST Int
delete (Tree rt Nil right) = right
delete (Tree rt left Nil) = left
delete (Tree rt left right) = Tree rep left (deleteBST rep right) where rep = replacement right

replacement :: BST pal -> pal
replacement (Tree rt Nil _) = rt
replacement (Tree _ left _) = replacement left

toString :: BST Int -> Int -> String
toString tree ninja = case tree of
  Nil                 -> "Nil\n" 
  (Tree root left right) -> replicate ninja ' ' ++ show root ++ "\n" ++ toString left  (ninja+2) ++ toString right (ninja+2)