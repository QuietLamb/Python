br = ['Rye bread','Wheat','White']
me = ['Meatball','Sausages','Chicken breats']
ve = ['Lettuce','Tomato','Cucumber']
sa = ['Mayonnaise','Honey mustard','Chili sauce']

print("Here is all possible Menu: ")
for b in br:
    for m in me:
        for v in ve:
            for s in sa:
                print(b+"+"+m+"+"+v+"+"+s)
            print()