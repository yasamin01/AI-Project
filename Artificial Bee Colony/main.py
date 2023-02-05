# Artificial Bee Colony (ABC)

import random


def Fitness(x):  # sphere
    ans = 0
    for i in range(len(x)):
        ans += x[i] ** 2

    return ans


# Employee Bee

def Employee_Bee(X, f, trials):
    for i in range(len(X)):
        V = []
        R = X.copy()
        R.remove(X[i])
        r = random.choice(R)
        for j in range(len(X[0])):
            V.append((X[i][j] + random.uniform(-1, 1) * (X[i][j] - r[j])))
        if f(X[i]) < f(V):
            trials[i] += 1
        else:
            X[i] = V
            trials[i] = 0

    return X, trials


def P(X, f):
    P = []
    s = sum([1 / abs(1 + f(i)) for i in X])
    for i in range(len(X)):
        P.append((1 / (1 + f(X[i]))) / s)

    return P


# Onlooker Bee

def Onlooker_Bee(X, f, trials):
    Pi = P(X, f)
    for i in range(len(X)):
        if random.random() < Pi[i]:
            V = []
            R = X.copy()
            R.remove(X[i])
            r = random.choice(R)
            for j in range(len(X[0])):
                V.append((X[i][j] + random.uniform(-1, 1) * (X[i][j] - r[j])))
            if f(X[i]) < f(V):
                trials[i] += 1
            else:
                X[i] = V
                trials[i] = 0
    return X, trials


# Scout Bee

def Scout_Bee(X, trials, bounds, limit=3):
    for i in range(len(X)):
        if trials[i] > limit:
            trials[i] = 0
            X[i] = [bounds[i][0] + (random.uniform(0, 1) * (bounds[i][1] - bounds[i][0])) for i in range(len(X[0]))]
    return X


def ABC(dimensions, bound, f, limit=4, population=20, runs=20):
    bound = [(-10, 10) for i in range(dimensions)]

    X = [[bound[i][0] + (random.uniform(0, 1) * (bound[i][1] - bound[i][0])) for i in range(dimensions)] for i in range(population)]

    trials = [0 for i in range(population)]

    while runs > 0:
        X, trials = Employee_Bee(X, f, trials)
        X, trials = Onlooker_Bee(X, f, trials)
        X = Scout_Bee(X, trials, bound, limit)
        runs -= 1

    fx = [f(i) for i in X]
    print(fx)
    I = fx.index(min(fx))
    print(X[I])


dimensions = 1
bound = [(-10, 10)]

ABC(dimensions, bound, Fitness, limit=50, population=20, runs=100)


