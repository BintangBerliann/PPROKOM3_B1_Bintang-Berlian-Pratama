z = [1, 3, 2, 4, 'Alice', 'Bob'] 
z.sort(key=str)
print(z) 
print("Hello there!\nHow are you?\nI\'m doing fine.") 

multi_line = """Hello there! 
How are you? 
I'm fine.""" 
print(multi_line) 

spam = ' Hello World ' 
spam.strip() 
spam.lstrip() 
spam.rstrip()
print(spam)

join_cats = ', '.join(['cats', 'rats', 'bats'])
join_name = ' '.join(['My', 'name', 'is', 'Simon'])
join_ABC = 'ABC'.join(['My', 'name', 'is', 'Simon'])
split_name = 'My name is Simon'.split()
split_ABC = 'MyABCnameABCisABCSimon'.split('ABC')
print(join_cats)
print(join_name)
print(join_ABC)
print(split_name)
print(split_ABC)