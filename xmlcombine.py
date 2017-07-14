#! /usr/bin/env python
"""
Usage:
Generate a list of xml files in the folder with the following bash command:
'find . -name "*.xml" -type -f > xml_files.txt'

Pass xml_files.txt to this script along with a name for the combined CSV file.
"""
import sys
import numpy as np
import pandas as pd
from xml.etree import ElementTree

def xml2df(xml_filename):
    xml_data = open(xml_filename).read()
    root = ElementTree.XML(xml_data)  # element tree
    all_records = []
    for i, child in enumerate(root):
        record = {}
        for subchild in child:
            record[subchild.tag] = subchild.text
            all_records.append(record)
    # At this point, all_records is a list of dicts corresponding to each level
    # Flatten all key, value pairs to one large dictionary
    all_records = {k: v for d in all_records for k, v in d.items()}

    # Convert to DataFrame, index=[0] is required when passing dictionary
    xml_df = pd.DataFrame(all_records, index=[0])
    # Clean up column names and replace newline characters with trailing
    # spaces with NaNs
    xml_df.columns = xml_df.columns.str.replace(
        '\{http://tcga.nci/bcr/xml/.*\}', '')
    xml_df.replace('\\n.*', np.NaN, regex=True, inplace=True)
    return xml_df

def process_xmls(xml_files_txt, outputname):
    files = [line.rstrip('\n') for line in open(xml_files_txt)]
    df_total = pd.DataFrame()
    for xml_file in files:
        df_each = xml2df(xml_file)
        df_total = df_total.append(df_each)
    df_total.to_csv(outputname, index=False)

if __name__ == '__main__':
    xml_files_txt = sys.argv[1]
    outputname = sys.argv[2]
    process_xmls(xml_files_txt, outputname)
