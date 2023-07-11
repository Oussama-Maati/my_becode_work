def slices(series, length):
    if length <= 0 or length > len(series):
        raise ValueError("Length argument doesn't fit the series.")
    return [list(map(int, series[i:i+length])) for i in range(len(series)-length+1)]
