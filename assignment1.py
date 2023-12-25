Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
from Bio import SeqIO
from Bio.Seq import Seq

from Bio.SeqRecord import SeqRecord

sequence1 = Seq("ATCGATCGATCG")

sequence2 = Seq("GCTAGCTAGCTA")

sequence3 = Seq("GATCGATCGATC")

sequence4 = Seq("CTAGCTAGCTAG")

sequence5 = Seq("ATCGATCGATCG")

sequence6 = Seq("GCTAGCTAGCTA")

sequence7 = Seq("ATCGATCGATCG")


sequence8 = Seq("GCTAGCTAGCTA")

sequence9 = Seq("ATCGATCGATCG")

sequence10 = Seq("GCTAGCTAGCTA")

output_file = "C:/Users/Dana/Documents/projects/assigment.fasta"

record1 = SeqRecord(sequence1, id="Seq1", description="First sequence")

record2 = SeqRecord(sequence2, id="Seq2", description="Second sequence")

record3 = SeqRecord(sequence3, id="Seq3", description="Third sequence")

record4 = SeqRecord(sequence4, id="Seq4", description="Fourth sequence")

record5 = SeqRecord(sequence5, id="Seq5", description="Fifth sequence")

record6 = SeqRecord(sequence6, id="Seq6", description="Sixth sequence")

record7 = SeqRecord(sequence7, id="Seq7", description="Seventh sequence")

record8 = SeqRecord(sequence8, id="Seq8", description="Eighth sequence")

record9 = SeqRecord(sequence9, id="Seq9", description="Ninth sequence")

record10 = SeqRecord(sequence10, id="Seq10", description="Tenth sequence")

SeqIO.write([record1, record2, record3, record4, record5, record6, record7, record8, record9, record10], output_file, "fasta")

10
record_number = 0

for record in SeqIO.parse(output_file, "fasta"):
    record_number += 1
    if record_number == 6:
        print(record.id)
        print(record.seq)
        break
    

    
Seq2
GCTAGCTAGCTA
from Bio.Seq import reverse_complement
records = list(SeqIO.parse(output_file, "fasta"))
SyntaxError: multiple statements found while compiling a single statement
records = list(SeqIO.parse(output_file, "fasta"))

record_number
2
index_to_update = record_number-1
sequence_to_update = records[index_to_update].seq
... 
>>> sequence_rc = reverse_complement(sequence_to_update)
... 
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    sequence_rc = reverse_complement(sequence_to_update)
NameError: name 'reverse_complement' is not defined
>>> from Bio.Seq import reverse_complement
... 
>>> sequence_rc = reverse_complement(sequence_to_update)
... 
>>> records[index_to_update].seq = sequence_rc
... 
>>> SeqIO.write(records, input_file, "fasta")
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    SeqIO.write(records, input_file, "fasta")
NameError: name 'input_file' is not defined. Did you mean: 'output_file'?
>>> SeqIO.write(records, output_file, "fasta")
10
>>> print(f"Updated FASTQ file: {input_file}")
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    print(f"Updated FASTQ file: {input_file}")
NameError: name 'input_file' is not defined. Did you mean: 'output_file'?
>>> print(f"Updated FASTQ file: {output_file}")
Updated FASTQ file: C:/Users/Dana/Documents/projects/assigment.fasta
>>> record_number = 0
... 
>>> for record in SeqIO.parse(output_file, "fasta"):
...     record_number += 1
...     if record_number == 2:
...         print(record.id)
...         print(record.seq)
...         break
... 
...     
Seq2
TAGCTAGCTAGC
