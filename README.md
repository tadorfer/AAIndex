# AAIndex: raw --> dataframe

This repository is for converting raw AAIndex data, as provided by [GenomeNet](https://www.genome.jp/aaindex/), into a more useable, Python-friendly dataframe.
The current version of the AAIndex database is v9.2, which was last updated in 2017. I have provided the converted .csv files for now, but should there be any updates in the future, the code can be used to incorporate any changes.
<br><br>

- <b>AAIndex1</b>: contains 566 amino acid indices
- <b>AAIndex2</b>: contains 94 amino acid mutation matrices
- <b>AAIndex3</b>: contains 47 matrices denoting statistical protein contact potentials
<br>

While AAIndices 1 & 3 contain exactly 20 rows and 20 columns (each corresponding to one of the 20 amino acids), AAIndex2 contains matrices with varying row (20-22) and column (20-21) size. Thus, rows and columns are labelled numerically (0, 1, 2,...) instead of categorically (A, R, N,...). All rows and columns have been scaled up to the largest number of rows (22) and columns (21), which for some matrices results in the final one or two rows (or final column) to be all zeros. Therefore, it is important to work with the matrix description at hand to know the dimensions of the matrix of interest.

## Requirements

- Numpy
- Pandas


## Execution

The functions in the script <i>raw_to_df.py</i> can be executed as follows (given the same directory tree as in this repository is used):

'''
from raw_to_df import conversion_aa1, conversion_aa2, conversion_aa3

# execute functions
df_aa1 = conversion_aa1('data/aaindex1.txt')
df_aa2 = conversion_aa2('data/aaindex2.txt')
df_aa3 = conversion_aa3('data/aaindex3.txt')

# save as .csv
df_aa1.to_csv('aaindex1.csv', index=False)
df_aa2.to_csv('aaindex2.csv', index=False)
df_aa3.to_csv('aaindex3.csv', index=False)

#### Before (Raw)

<p align="center">
  <img src="/imgs/before.png" height="650" width="650">
</p>

#### After (DataFrame)

<p align="center">
  <img src="/imgs/after.png" height="300" width="700">
</p>