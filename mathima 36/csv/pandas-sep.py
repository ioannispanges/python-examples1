import pandas as pd

custom_data = pd.read_csv('PRAD_TCGA_RNA_seq.txt', sep=",")

print("\nCustom Delimiter Data:")
print(custom_data.head())
