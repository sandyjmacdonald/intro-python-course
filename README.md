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

## Sheep GWAs Data

sheepdata.txt contains (again, after the header line) lines with 37 columns. The first column is 
the identifier of a particular mutation in the sheep genome (more correctly, a Single 
Nucleotide Polymorphism) and it is followed by 36 p-values which indicate the degree of
association with each of 36 different climatic parameters.
