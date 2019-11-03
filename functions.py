import numpy as np


def winsorize(x, tr=0.2, verbose=False):
    x = np.array(x)
    y = list(np.empty(len(x)))
    threshold_index = int(round(len(x) * tr, 0))
    winsorized_value_lower = int(np.max(np.sort(x)[:threshold_index:]))
    winsorized_value_upper = int(np.min(np.sort(x)[::-1][:threshold_index:]))
    for i in range(len(x)):
        if x[i] > winsorized_value_upper:
            y[i] = winsorized_value_upper
        elif x[i] < winsorized_value_lower:
            y[i] = winsorized_value_lower
        else:
            y[i] = x[i]
        p = round((i / len(x)) * 100, 1)
        sys.stdout.write('\r'+str(p) + '\r')
        sys.stdout.flush()
    return y


x = np.random.randint(1, 100, size=29000)
winsorize(x)
%timeit winsorize(x)
