import numpy as np


def compute_mean(x):
    result = np.array(x)
    result = np.sum(result)/len(result)

    return result


def compute_median(x):
    size = len(x)
    x = np.sort(x)
    result = -1
    # print(x)
    if (size % 2 == 0):
        result = (x[int((size-1)/2)] + x[(int((size-1)/2))+1])/2
        return result
    else:
        result = x[int(((size-1)+1)/2)]
        return result


def compute_std(x):
    mean = compute_mean(x)
    variance = np.sum((x - mean)**2)/len(x)

    return np.sqrt(variance)


def compute_correlation_cofficient(x, y):
    N = len(x)
    numerator = N*(x.dot(y))-(np.sum(x)*np.sum(y))
    denominator = np.sqrt(N*np.sum(x**2)-(np.sum(x))**2) * \
        np.sqrt(N*np.sum(y**2)-(np.sum(y))**2)
    return np.round(numerator/denominator, 2)


if __name__ == "__main__":
    # Question 1:
    # X = [2, 0, 2, 2, 7, 4, -2, 5, -1, -1]
    # print("Mean: ", compute_mean(X))

    # Question 2:
    # X = [1, 5, 4, 4, 9, 13]
    # print("Median: ", compute_median(X))

    # Question 3:
    # X = [171, 176, 155, 167, 169, 182]
    # print(compute_std(X))

    # Question 4:
    X = np.asarray([-2, -5, -11, 6, 4, 15, 9])
    Y = np.asarray([4, 25, 121, 36, 16, 225, 81])
    print("Correlation: ", compute_correlation_cofficient(X, Y))
