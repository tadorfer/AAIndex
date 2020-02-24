# AAIndex: raw --> dataframe

This repository is for converting raw AAIndex data, as provided by [GenomeNet](genome.jp/aaindex/), into a more useable, Python-friendly dataframe.
The current version of the AAIndex database is v9.2, which was last updated in 2017. <br>

- <b>AAIndex1</b>: contains 566 amino acid indices
- <b>AAIndex2</b>: contains 94 amino acid mutation matrices
- <b>AAIndex3</b>: contains 47 matrices denoting statistical protein contact potentials
<br>

While AAIndices 1 & 3 contain exactly 20 rows and 20 columns (each corresponding to one of the 20 amino acids), AAIndex2 contains matrices with varying row (20-22) and column (20-21) size. Thus, rows and columns are labelled numerically (0, 1, 2,...) instead of categorically (A, R, N,...). All rows and columns have been scaled up to the largest number of rows (22) and columns (21), which for some matrices results in the final one or two rows (or final column) to be all zeros. Therefore, it is important to work with the matrix description at hand to know the dimensions of the matrix of interest.


### Demonstration

#### Before (Raw)

<p align="center">
  <img src="/imgs/before.png" height="700" width="650">
</p>

#### After (DataFrame)

<p align="center">
  <img src="/imgs/after.png" height="700" width="650">
</p>