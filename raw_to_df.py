import pandas as pd
import numpy as np


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


def conversion_aa2(data):
    "Converts raw AAIndex2 into useable Pandas DataFrame"

    # define column names 
    columns = ['A', 'R', 'N', 'D', 'C', 'Q', 'E', 'G', 'H', 'I',
               'L', 'K', 'M', 'F', 'P', 'S', 'T', 'W', 'Y', 'V']

    MAX_ROW = 22
    MAX_COL = 21
    INDICES = 94
    arr = np.zeros((MAX_ROW, MAX_COL, INDICES))
    cnt = -1
    all_desc = []

    with open(data) as f: 
        for i, line in enumerate(f):
            if line[0] == 'H':
                description = line.split()[1]
                all_desc.append(description)
                cnt += 1
            if line[0] == 'M':
                tmp = i
            if 'tmp' in locals():
                for aa in range(MAX_ROW):
                    if i == tmp+(aa+1):
                        tmp_arr = line.split()
                        # replacing dashes with NaN
                        tmp_arr = [e.replace("-", "NaN") if len(e) == 1 else e for e in tmp_arr]
                        try:
                            float(tmp_arr[0])
                            arr[aa,:len(tmp_arr),cnt] = tmp_arr
                        except ValueError:
                            pass

    rows = [str(x) for x in range(22)]
    cols = [str(x) for x in range(21)]

    ext_desc = [[all_desc[i]]*22 for i in range(INDICES)]
    flat_desc = [item for sublist in ext_desc for item in sublist]
    multind = pd.MultiIndex.from_arrays([flat_desc, rows*INDICES], names=['Description', 'Amino Acids'])

    # reshape 3D to 2D
    arr2D = arr.transpose(2,0,1).reshape(-1,arr.shape[1])

    df = pd.DataFrame({cols[i]: arr2D[:,i] for i in range(21)}, multind)

    return df


def conversion_aa3(data):
    "Converts raw AAIndex3 into useable Pandas DataFrame"
    
    # define column names 
    columns = ['A', 'R', 'N', 'D', 'C', 'Q', 'E', 'G', 'H', 'I',
               'L', 'K', 'M', 'F', 'P', 'S', 'T', 'W', 'Y', 'V']

    MAX_ROW = 20
    MAX_COL = 20
    INDICES = 47
    arr = np.zeros((MAX_ROW, MAX_COL, INDICES))
    cnt = -1
    all_desc = []
    
    # conversion by parsing text file line by line
    with open(data) as f: 
        for i, line in enumerate(f):
            if line[0] == 'H':
                description = line.split()[1]
                all_desc.append(description)
                cnt += 1
            if line[0] == 'M':
                tmp = i
            if 'tmp' in locals():
                for aa in range(MAX_ROW):
                    if i == tmp+(aa+1):
                        tmp_arr = line.split()
                        # replacing dashes with NaN
                        tmp_arr = [e.replace("-", "NaN") if len(e) == 1 else e for e in tmp_arr]
                        tmp_arr = [e.replace("NA", "NaN") for e in tmp_arr]
                        arr[aa,:len(tmp_arr),cnt] = tmp_arr

    ext_desc = [[all_desc[i]]*20 for i in range(INDICES)]
    flat_desc = [item for sublist in ext_desc for item in sublist]
    multind = pd.MultiIndex.from_arrays([flat_desc, columns*INDICES], names=['Description', 'Amino Acids'])

    # reshape 3D to 2D
    arr2D = arr.transpose(2,0,1).reshape(-1,arr.shape[1])

    df = pd.DataFrame({columns[i]: arr2D[:,i] for i in range(20)}, multind)

    return df