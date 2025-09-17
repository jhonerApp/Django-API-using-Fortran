import csv
import numpy as np


def extract_array(file_name, comma_to_dot=True):
    results = []
    with open(file_name) as csvfile:

        reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC)  # change contents to floats
        for row in reader:
            results.append(row)

    if comma_to_dot:
        for i in range(len(results)):
            for j in range(len(results[0])):
                if isinstance(results[i][j], str):
                    results[i][j] = results[i][j].replace(",", ".", 1)

    results = np.array(results).astype(np.double)
    return results
