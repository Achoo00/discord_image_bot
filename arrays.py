x=[1,2,3]

for num in x:
    try:
        y=x[num]
    except Exception as e:
        print(e)
