print(
    map(lambda a: a if a.find("z")==-1 else a[:a.rfind("z")+1], 
    map(lambda x:("Fizz" if x%3==0 else "") + ("Buzz" if x%5==0 else "") + str(x),
    range(1,101)
    )
    )
    )
