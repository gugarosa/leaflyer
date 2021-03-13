import argparse

import utils.scrapper as s

def get_arguments():
    """Gets arguments from the command line.

    Returns:
        A parser with the input arguments.

    """

    parser = argparse.ArgumentParser(usage='Scraps strains meta-data from Leafly.')

    parser.add_argument('input_file', help='Input .txt file holding the list of URLs', type=str)

    parser.add_argument('output_file', help='Output .csv file', type=str)

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

    # Iterates through every possible URL
    for url in urls:
        # Scraps the meta-data
        url_data = s.get_strain_data(url)

        print(url_data)