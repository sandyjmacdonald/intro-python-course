# Introduction to Python Programming course files

### (Bioscience Technology Facility Data Science group)

The list above contains the files that you'll need during the Introduction to Python Programming
course. To download a file, just right-click the filename then select "Download linked file as...",
"Save link as..." or whatever your favourite browser's option is to save the file.

## DNA Sequence Length Data

The file `seq_lengths.txt` contains >12,000 data points, each of which is the length of a DNA
sequence sampled from a particular experiment. The data is simply formatted with a single
integer value per line.

## RNA-Seq Data

The `rna_seq_data.txt` file contains data from an experiment that was measuring the amounts of
RNA for different genes in cells under different conditions. The format is that each line
(after the first line which contains the names of the different columns) contains four values:
an identifier (ID) for the sequence, the name of the gene, a "fold change value" and the p-value
of the significance of the difference in expression between the conditions. The fold change is the
ratio of amounts between the conditions, and the p-value is calculated using a standard Student's
_t_-test.

The p-values in that file are just the raw p-values from the _t_-test, and so are likely to be
misleading because there are so many tests that some of them are likely to indicate a significant
difference purely by chance. We normally correct for this using a method to adjust the p-values.
In this case, we used the Benjamini-Hochberg method to re-calculate the p-value to ensure that
the false discovery rate (FDR - the proportion of comparisons which appear significant purely
by chance) is a reliable value that we can use instead. For this reason, the
`corrected_rna_seq_data.txt` file contains a column with the q-values as well.

## Met Office Weather Data

`met-office-weather` contains the Python code which generates the page at
[https://met-office-weather.vercel.app/](https://met-office-weather.vercel.app/) by scraping data
from the Met Office API.
