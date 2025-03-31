case_3times = set()

for i in range(1,6):
    for j in range(i,7):
        for k in range(j,7):
            case_3times.add((i,j,k))

total_cases = len(case_3times)

for i in range(3,19):
    n_cases = 0
    for c in case_3times:
        if sum(c)>=i:
            n_cases+=1
    probability = n_cases * 100 / total_cases
    print("Probability of obtaining more than {:2d} is {:6.2f}%".format(i,probability))

