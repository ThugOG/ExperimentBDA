
### Commands to run Mapper and Reducers 
(Use only in case if you dont know how to run them on hadoop)

MM = Matrix multiplication
WC = Word Count

1) ```cat input.txt | python3 mapper_WC.py | sort -k1,1 | python3 reducer_WC.py```
(python3 subjective to the python version, also clone input.txt in same folder)


2) ```cat input_MM.txt | python3 mapper_MM.py | sort | python3 reducer_MM.py```


3) I case of R programs use R studio to run them.
