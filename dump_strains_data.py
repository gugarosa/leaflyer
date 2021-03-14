import argparse
import json

import utils.scrapper as s

def get_arguments():
    """Gets arguments from the command line.

    Returns:
        A parser with the input arguments.

    """

    parser = argparse.ArgumentParser(usage='Scraps strains meta-data from Leafly.')

    parser.add_argument('input_file', help='Input .txt file holding the list of URLs', type=str)

    parser.add_argument('output_file', help='Output .json file', type=str)

    return parser.parse_args()

if __name__ == '__main__':
    # Gathers the input arguments and its variables
    args = get_arguments()
    input_file = args.input_file
    output_file = args.output_file

    # Opens an input file
    with open(input_file, 'r') as f:
        urls = f.readlines()
    
    # Closes the file
    f.close()

    # Creates a dictionary holding the data
    data = {}
    data['strains'] = []

    # Iterates through every possible URL
    for url in urls:
        # Scraps the meta-data
        url_data = s.get_strain_data(url)

        # Appends the url-based data to the dictionary itself
        data['strains'].append(url_data)

    # Outputs the data to a .json file
    with open(output_file, 'w') as f:
        json.dump(data, f)
