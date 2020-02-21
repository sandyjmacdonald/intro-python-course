import numpy as np
import matplotlib.pyplot as plt

# Open the data file

f = open("RNASeq_data.txt", 'r')

# Create empty lists that will hold the contents of each column

ids = []
names = []
p_values = []
log_fold_changes = []
sig_p_values = []
sig_fold_changes = []

header = f.readline()
for line in f:

# Remove the newline character, then split the data into fields

    fields = line.strip().split()

# Convert the (non-string) fields into floating-point numbers

    identifier = fields[0]
    name = fields[1]
    p_value = float(fields[2])
    log_fold_change = float(fields[3])

# Add each of the values to the right list

    ids.append(identifier)
    names.append(name)
    if p_value <= 0.05 and abs(log_fold_change) >= 1:
        sig_p_values.append(p_value)
        sig_fold_changes.append(log_fold_change)
    else:
        p_values.append(p_value)
        log_fold_changes.append(log_fold_change)

# Take the log of the p-values. No need to loop over this, because numpy vectorises the operation

log_p_values = list(-np.log10(p_values))
log_sig_p_values = list(-np.log10(sig_p_values))

# Plot all of the data

plt.figure(1, figsize=(9,6))
plt.scatter(log_fold_changes+sig_fold_changes, log_p_values+log_sig_p_values)
plt.xlabel("log2(FoldChange)")
plt.ylabel("-log10(p)")
plt.title("Volcano plot")
plt.tight_layout()

# Plot all of the data points in blue, then just the significant points in red

plt.figure(2, figsize=(9,6))
plt.scatter(log_fold_changes, log_p_values, c='#006B77', marker="+")
plt.scatter(sig_fold_changes, log_sig_p_values, c='#FF6900', marker="+")

# Label the axes, using TeX notation

plt.xlabel("$log_{2}(Fold Change)$")
plt.ylabel("$-log_{10}(p)$")
plt.title("Volcano plot")

# Now draw lines to show the values we use as significant

plt.axhline(-np.log10(0.05), linestyle="--", c='lightgray')
plt.axvline(1, linestyle="--", c='lightgray')
plt.axvline(-1, linestyle="--", c='lightgray')

plt.tight_layout()

plt.show()
