import argparse

import utils.scrapper as s

def get_arguments():
    """Gets arguments from the command line.

    Returns:
        A parser with the input arguments.

    """

    parser = argparse.ArgumentParser(usage='Scraps the strains URLs from Leafly.')

    parser.add_argument('output_file', help='Output .txt file', type=str)

    parser.add_argument('-start_page', help='Starting page identifier', type=int, default=1)

    parser.add_argument('-end_page', help='Ending page identifier', type=int, default=1)

    return parser.parse_args()

if __name__ == '__main__':
    # Gathers the input arguments and its variables
    args = get_arguments()
    output_file = args.output_file
    start_page = args.start_page
    end_page = args.end_page

    # Opens an output file
    with open(output_file, 'w') as f:
        # Iterates through the page range
        for i in range(start_page, end_page + 1):
            # Gets the list of strains that pertains to the iterated page
            strains_list = s.get_strains_list(i)

            # Writes the list to the file
            f.write('\n'.join(strains_list))
            f.write('\n')
    
    # Closes the file
    f.close()
