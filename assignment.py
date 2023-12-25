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
    if record_number == 2:
        print(record.id)
        print(record.seq)
        break

    
Seq2
GCTAGCTAGCTA
from Bio.Seq import reverse_complement
input_file = "C:/Users/Dana/Documents/projects/assigment.fasta"
records = list(SeqIO.parse(input_file, "fasta"))
index_to_update = 1
sequence_to_update = records[index_to_update].seq
sequence_rc = reverse_complement(sequence_to_update)
records[index_to_update].seq = sequence_rc
>>> SeqIO.write(records, input_file, "fasta")
10
>>> print(f"Updated FASTQ file: {input_file}")
... 
Updated FASTQ file: C:/Users/Dana/Documents/projects/assigment.fasta
