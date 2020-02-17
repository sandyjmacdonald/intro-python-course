# York Python Course Files

The list above contains the data files that you can use during the York Python courses.  To download a
file, just right-click the name then select "Download linked file as...", "Save link as..." or 
whatever your favourite browser's option is to save the file.

## DNA Sequence Length Data

The file seqLengths.txt contains >12,000 data points, each of which is the length of a DNA 
sequence sampled from a particular experiment.  The data is simply formatted with a single 
integer value per line.

## RNA-Seq Data

The RNAseq\_data.txt file contains data from an experiment that was measuring the amounts of 
RNA for different genes in cells under different conditions.  The format is that each line 
(after the first line which contains the names of the different columns) contains four values: 
an identified for the sequence, the name of the gene, a "fold change value" and the p-value 
of the significance of the different between the conditions.  The fold change is the ratio
of amounts between the conditions, and the p-value is calculated using a standard Student's *t*-test.

The p-values in that file are just the raw p-values from the *t*-text, and so are likely to be 
misleading bacaise there are so many tests, that some of them are likely to indicate significance
purely by chance.  We normally correct for this using a method to adjust the p-values.  In this 
case, we used the Benjamini-Hochberg method to re-calculate the p-value to ensure that the 
false discovery rate (FDR - the proportion of comparisons which appear significant purely
by chance), to give a q-value we can use instead. For this data, corrected\_RNAseq\_data.txt 
contains a column with the q-values as well.

## Sheep GWAs Data

sheepdata.txt contains (again, after the header line) lines with 37 columns. The first column is 
the identifier of a particular mutation in the sheep genome (more correctly, a Single 
Nucleotide Polymorphism) and it is followed by 36 p-values which indicate the degree of
association with each of 36 different climatic parameters.

## The weather Script

"weather" contains the python code which generates the page at http://bioltfws1.york.ac.uk/cgi-bin/weather 
by scraping data from the Met Office web service.
