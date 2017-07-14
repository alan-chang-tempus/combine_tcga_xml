## Combine multiple TCGA BCR XML files into one CSV

Usage:  
Generate a list of xml files in the folder with the following bash command:
'find . -name "\*.xml" -type f > xml_files.txt'

Pass the resulting xml_files.txt to this script along with a name for the combined CSV file.

Notes:  
Script simplifies column names by removing {http://tcga.nci/bcr/xml/...} pattern from column names.  
In addition, all XML levels are flattened.  
Base code adapted from: http://www.austintaylor.io/lxml/python/pandas/xml/dataframe/2016/07/08/convert-xml-to-pandas-dataframe/


Example:  
```bash  
find . -name "*.xml" -type f > xml_files.txt
python xmlcombine.py xml_files.txt xml_combined.csv
```
