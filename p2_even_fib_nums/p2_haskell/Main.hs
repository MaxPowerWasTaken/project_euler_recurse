{- PROBLEM STATEMENT:
Each new term in the Fibonacci sequence is generated by adding the previous two terms. 
By starting with 1 and 2, the first 10 terms will be:
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
By considering the terms in the Fibonacci sequence whose values do not exceed four million, 
find the sum of the even-valued terms.
-}

module Main where
main :: IO ()
main = print sum_

{- CONSTANTS-}
limit = 4000000

{-LOGIC-}
sum_ = sum even_fibs_lt_4mil
even_fibs_lt_4mil = takeWhile (<limit) even_fibs
even_fibs = filter(\x -> x `mod` 2 == 0) fibs
fibs = 1:1: zipWith(+) fibs (tail fibs)

{- NOTES ON STUFF THAT DIDNT WORK
this line below will crash computer by trying to calculate an infinite list (check every fib ever for <4million or not)
even_fibs_lt_4mil = filter(\x -> x `mod` 2 == 0 && x < limit) fibs

fibs = [1,1, zipWith(+) fibs (tail fibs)] <- but this does not work
fibs = [1,1] <> zipWith(+) fibs (tail fibs) <-  but this does 
-}