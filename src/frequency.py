def frequency(arr, n_cells):
    h = (max(arr) - min(arr)) / n_cells
    borders = [min(arr) + h * i for i in range(n_cells)]
    result = [0 for i in range(n_cells)]
    for i in range(len(arr)):
        for j in range(len(borders)):
            if(arr[i] >= borders[j]) and (arr[i] < borders[j]+h):
                result[j] += 1
    return result
