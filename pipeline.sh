# Defines the constants
URL_LIST_FILE="strains_url.txt"
STRAINS_DATA_FILE="strains_data.json"
START_PAGE=1
END_PAGE=2

# Performs the URL extraction
python scrap_strains_list.py $URL_LIST_FILE -start_page $START_PAGE -end_page $END_PAGE

# Extracts meta-information about the strains
python scrap_strains_data.py $URL_LIST_FILE $STRAINS_DATA_FILE