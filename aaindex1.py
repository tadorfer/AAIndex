import pandas as pd

def conversion_aa1(data):
    "Converts raw AAIndex1 into useable Pandas DataFrame"
    
    # define column names and initialize dataframe
    col1 = ['Description']
    aa = ['A', 'R', 'N', 'D', 'C', 'Q', 'E', 'G', 'H', 'I',
          'L', 'K', 'M', 'F', 'P', 'S', 'T', 'W', 'Y', 'V']
    columns = col1+aa
    df = pd.DataFrame(data=[], columns=columns)
    
    # conversion by parsing text file line by line
    with open(data) as f: 
        for i, line in enumerate(f):
            if line[0] == 'H':
                description = line.split()[1]
            if line[0] == 'I':
                tmp = i
            if 'tmp' in locals():
                if i == tmp+1:
                    tmp1 = [description]+line.split()
                if i == tmp+2:
                    tmp2 = line.split()
                    tmp_all = tmp1+tmp2
                    tmp_all = pd.DataFrame([tmp_all], columns=columns)
                    df = df.append([tmp_all]).reset_index(drop=True)    
    
    return df