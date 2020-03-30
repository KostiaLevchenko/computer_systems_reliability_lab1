import math
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import uniform, gamma, norm, expon


from src.frequency import frequency
from src.chi_square import chi_squre
from src.ask_file_path import ask_file_path
from src.open_file import open_file

if __name__ == "__main__":
    array = open_file(path=ask_file_path())

    m = np.mean(array)
    d = np.std(array) ** 2
    alpha = m ** 2 / d
    beta = m / d
    n_cells = 10

    chi_exp, chi_normal, chi_uniform, chi_gamma = 0, 0, 0, 0

    while not (chi_exp and chi_normal and chi_uniform and chi_gamma):
        try:
            array_normal = list(np.random.normal(m, math.sqrt(d), len(array)))
            array_exp = list(np.random.exponential(m, len(array)))
            array_uni = list(np.random.uniform(min(array), max(array), len(array)))
            array_gamma = list(np.random.gamma(alpha, beta, len(array)))
            chi_exp = chi_squre(frequency(array, n_cells), frequency(array_exp, n_cells))
            chi_normal = chi_squre(frequency(array, n_cells), frequency(array_normal, n_cells))
            chi_uniform = chi_squre(frequency(array, n_cells), frequency(array_uni, n_cells))
            chi_gamma = chi_squre(frequency(array, n_cells), frequency(array_gamma, n_cells))
        except ValueError:
            pass

    print("exp:", chi_exp)
    print("normal:", chi_normal)
    print("uniform:", chi_uniform)
    print("gamma:", chi_gamma)

    F, P, Q, lambdat = [], [], [], []

    if min(chi_exp, chi_normal, chi_uniform, chi_gamma) == chi_exp:
        F = expon.pdf(range(int(min(array)), int(max(array))), loc=1 / m, scale=m)
        Q = expon.cdf(range(int(min(array)), int(max(array))), loc=1 / m, scale=m)
        P = [1 - i for i in Q]
        lambdat = [F[i] / P[i] for i in range(len(F))]
        print("exp")

    if min(chi_exp, chi_normal, chi_uniform, chi_gamma) == chi_normal:
        F = norm.pdf(range(int(min(array)), int(max(array))), loc=m, scale=math.sqrt(d))
        Q = norm.cdf(range(int(min(array)), int(max(array))), loc=m, scale=math.sqrt(d))
        P = [1 - i for i in Q]
        lambdat = [F[i] / P[i] for i in range(len(F))]
        print("normal")

    if min(chi_exp, chi_normal, chi_uniform, chi_gamma) == chi_uniform:
        F = uniform.pdf(range(int(min(array)), int(max(array))), min(array), max(array))
        Q = uniform.cdf(range(int(min(array)), int(max(array))), min(array), max(array))
        P = [1 - i for i in Q]
        lambdat = [F[i] / P[i] for i in range(len(F))]
        print("uni")

    if min(chi_exp, chi_normal, chi_uniform, chi_gamma) == chi_gamma:
        F = gamma.pdf(range(int(min(array)), int(max(array))), a=alpha, scale=1 / beta)
        Q = gamma.cdf(range(int(min(array)), int(max(array))), a=alpha, scale=1 / beta)
        P = [1 - i for i in Q]
        lambdat = [F[i] / P[i] for i in range(len(F))]
        print("gamma")

    h = (max(array) - min(array)) / n_cells
    borders = [min(array) + h * i for i in range(n_cells)]
    qt = [0 for i in range(n_cells)]
    for i in range(len(array)):
        for j in range(len(borders)):
            if array[i] <= borders[j] + h:
                qt[j] += 1
    for i in range(len(qt)):
        qt[i] /= len(array)
    pt = [1 - i for i in qt]

    print("Tндв =", m)
    print("D =", d)
    print("σ =", math.sqrt(d))

    fig = plt.figure()
    ax = fig.add_subplot(221)
    rects1 = ax.hist(array, density=True, alpha=.5, label="f(t)")
    rects2 = ax.plot(range(int(min(array)), int(max(array))), F, color='black', label="f*(t)")
    ax.set_xlabel('t')
    ax.set_ylabel('f(t)')
    ax.legend()

    ax2 = fig.add_subplot(222)
    rects4 = ax2.bar(borders, qt, alpha=.5, width=h, align="edge")
    rects5 = ax2.plot(range(int(min(array)), int(max(array))), Q, color='black')
    ax2.set_xlabel('t')
    ax2.set_ylabel('Q(t)')
    ax2.legend((rects4[0], rects5[0]), ('q(t)', 'q*(t)'))

    ax3 = fig.add_subplot(223)
    rects6 = ax3.bar(borders, pt, alpha=.5, width=h, align="edge")
    rects7 = ax3.plot(range(int(min(array)), int(max(array))), P, color='black')
    ax3.set_xlabel('t')
    ax3.set_ylabel('P(t)')
    ax3.legend((rects6[0], rects7[0]), ('p(t)', 'p*(t)'))

    ax4 = fig.add_subplot(224)
    ax4.set_xlabel('t')
    ax4.set_ylabel('λ')
    ax4.plot(range(int(min(array)), int(max(array))), lambdat, color='black')

    plt.show()
