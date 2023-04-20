from Bio import SeqIO


file_paths = ["path/to/file1.gbk", "path/to/file2.gbk", "path/to/file3.gbk"]

merged_file_name = "merged.gbk"


merged_records = []
for file_path in file_paths:
    with open(file_path, "r") as file:
        for record in SeqIO.parse(file, "genbank"):
            merged_records.append(record)


with open(merged_file_name, "w") as output_handle:
    SeqIO.write(merged_records, output_handle, "genbank")
