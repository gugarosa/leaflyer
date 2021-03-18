"""Module used to merge and export data, and detect duplicates."""

import json


def merge_json_files(file_name, n_files=1):
    """Merges a set of indexed JSON files (1, 2, ..., n) into a new one.

    Args:
        file_name (str): Name of the file to be merged without their indexes and extension.
        n_files (int): Amount of files to be merged.

    Returns:
        The merged file.

    """

    # Creates the data object and its `strains` array
    data = {}
    data['strains'] = []

    # Iterates through every possible file
    for i in range(n_files):
        # Opens the input file
        with open(f'{file_name}_{i+1}.json', 'r') as f:
            # Loads the temporary data
            tmp_data = json.load(f)

            # Merges the data
            data['strains'] += tmp_data['strains']

        # Closes the file
        f.close()

    # Removes any possible duplicates
    unique_data = list({row['name']: row for row in data['strains']}.values())

    # Opens the output file
    with open(f'{file_name}.json', 'w') as f:
        # Dumps the merged data
        json.dump(unique_data, f)
