import csv


def read_csv(filename, delimiter="\t"):
    """
    Read test data from CSV file, store in list of dictionaries, return this 
    list.
    
    Skips blank rows
    Skips rows starting with # character (to allow comments in file)
    Assumes first non-skipped row contains headings and uses these as 
    dictionary keys.
    Subsequent non-skipped rows are assumed to contain data and are used
    to supply dictionary values
    
    Args:
        filename: filename of csv file
        delimiter: csv delimiter character. Defaults to tab (\t)
    
    Returns:
        List of dictionaries
        e.g.
        [{"name":"Fred", "dob":"01/01/70"}, {"name":"Ginger", "dob":"02/02/71"}]
    
    """
    with open(filename, 'rb') as csvfile:
        csv_rows = csv.reader(csvfile, delimiter=delimiter)

        # Holds keys (heading) values from csv file
        keys = []
        # Holds data from file as list of dictionaries in same sequence
        # as original file
        extracted_data = []
        
        #Examine each row in turn
        for row in csv_rows:
            #Skip rows with no content
            if not row:
                continue
            #Skip row that contains only blank spaces
            if "".join(row).isspace():
                continue
            #Skip comment rows
            if row[0].startswith('#'):
                continue
            #Set dictionary keys using contents of first valid row encountered
            if not keys:
                # Don't construct keys if the row only contains blank spaces
                # Safety measure as hard to distinguish from blank line by eye
                # (Same filtering not applied to data as test data might  
                # deliberately be just spaces).
                if not "".join(row).isspace():
                    keys = row
            # Once keys set, construct dictionary from them and the contents
            # of subsequent rows, then  append to extracted_data list
            else:
                temp = {key:value for key, value in zip(keys, row)}
                extracted_data.append(temp)
        
        # Return the extracted values (list of dictionaries)        
        return extracted_data

zzz = read_csv("rep_order_date_and_mags_court.tsv")