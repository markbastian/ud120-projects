#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []

    for p, a, n in zip(predictions, ages, net_worths):
        cleaned_data += [(a[0], n[0], p[0] - n[0])]

    cleaned_data.sort(key=lambda (p, a, e): e * e)
    return cleaned_data[:len(predictions) * 9 / 10]

