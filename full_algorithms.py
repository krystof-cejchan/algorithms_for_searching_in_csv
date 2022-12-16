import algorithms
from algorithms import *


def full_linear_search(arr, x, full_match=False):
    results = []
    counter = 0
    length = len(arr)
    for line in arr:

        separated_line = line.split(',')

        res = linear_search(separated_line, len(separated_line), x, full_match)

        if res > -1:
            results.append(line)

        if counter >= length - 1:
            print(results)
            return results

        counter += 1


def full_rabin_karp(searched, arr, q=13):
    results = []
    for line in arr:
        for separated_value in line.split(','):
            res = algorithms.rabin_karp(searched, separated_value, q)

            if res:
                results.append(line)
                break

    return results


def full_boyer_moore(searched, arr):
    results = []
    for line in arr:
        for separated_value in line.split(','):
            res = algorithms.boyer_moore(separated_value, searched)

            if res:
                results.append(line)
                break

    return results
