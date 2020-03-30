from scipy.stats import chi2_contingency


def chi_squre(arr1, arr2):
    table = [arr1, arr2]
    chi_square_statistic, prob, dof, expected = chi2_contingency(table)
    return chi_square_statistic
