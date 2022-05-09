type Element = (Int,Int)
type BinaryRelation = Element -> Bool
bound = 99

emptyBinaryRelation :: BinaryRelation
emptyBinaryRelation = \nin -> False

universalBinaryRelation :: BinaryRelation
universalBinaryRelation = \nin -> True

contains :: Element -> BinaryRelation -> Bool
contains elem rel = rel elem

add :: Element -> BinaryRelation -> BinaryRelation
add elx rel = \elem -> if elx == elem then True else rel elem

addMultiple :: [Element] -> BinaryRelation -> BinaryRelation
addMultiple es rel = foldr add rel es

subRelation :: BinaryRelation -> BinaryRelation -> Bool
subRelation r1 r2 = subRelationHelper1 r1 r2 0

subRelationHelper1 :: BinaryRelation -> BinaryRelation -> Int -> Bool
subRelationHelper1 r1 r2 n
  | n > bound = True
  | otherwise = subRelationHelper2 r1 r2 n 0 && subRelationHelper1 r1 r2 (n+1)

subRelationHelper2 :: BinaryRelation -> BinaryRelation -> Int -> Int-> Bool
subRelationHelper2 r1 r2 n m
  | m > bound                                    = True
  | contains (n,m) r1 && not (contains (n,m) r2) = False
  | otherwise                                    = subRelationHelper2 r1 r2 n (m+1)

equal :: BinaryRelation -> BinaryRelation -> Bool
equal rel1 rel2 = (subRelation rel1 rel2) && (subRelation rel2 rel1)

reflexive :: BinaryRelation -> Bool
reflexive rel = foldr (\elx acc -> rel (elx,elx) && acc) True [0..bound]

union :: BinaryRelation -> BinaryRelation -> BinaryRelation
union rel1 rel2 = (\elem -> rel1 elem || rel2 elem)

inverse :: BinaryRelation -> BinaryRelation
inverse rel = (\elem -> if rel (snd elem, fst elem) then True else False)

symmetric :: BinaryRelation -> Bool
symmetric rel = and [rel (sec, fir) | fir<-[0..bound], sec<-[0..bound], rel (fir,sec)]

antiSymmetric :: BinaryRelation -> Bool
antiSymmetric rel = and[not (rel (sec, fir)) | fir<-[0..bound], sec<-[0..bound], (rel (fir, sec)) && fir /= sec]

transitive :: BinaryRelation -> Bool
transitive rel = and [rel(fir,thd) | fir<-[0..bound], sec<-[0..bound], thd<-[0..bound], (rel (fir,sec)) && (rel (sec,thd))]

equivalence :: BinaryRelation -> Bool
equivalence r = reflexive r && symmetric r && transitive r

reflexiveClosure :: BinaryRelation -> BinaryRelation
reflexiveClosure rel = (\elx -> if (fst elx == snd elx) then True else rel elx)

symmetricClosure :: BinaryRelation -> BinaryRelation
symmetricClosure rel = foldr (\elx acc -> if rel elx then add (snd elx, fst elx) acc else acc) rel [(fir, sec) | fir <- [0..bound], sec <- [0..bound]]

selfJoin :: BinaryRelation -> BinaryRelation
selfJoin rel = addMultiple [ (fir,thd) | fir<- [0..bound], sec<- [0..bound], thd<- [0..bound], rel (fir,sec) && rel (sec,thd)] emptyBinaryRelation

transitiveClosure :: BinaryRelation -> BinaryRelation
transitiveClosure rat = if equal rat (union (selfJoin rat) rat) then rat else  transitiveClosure (union (selfJoin rat) rat)

toString :: BinaryRelation -> String
toString r = show [(a,b) | a <- [0..bound], b <- [0..bound], r (a,b)]