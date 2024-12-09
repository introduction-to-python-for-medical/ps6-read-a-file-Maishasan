def create_codon_dict(file_path):
    path = "data/codons.txt"
    codon_dict = {}
    file = open(path)
    lines = file.readlines()
    file.close()
    for line in lines:
        line = line.strip()
        parts = line.split('\t')
        codon = parts[0]
        amino_acid = parts[2]
        codon_dict[codon] = amino_acid
    return codon_dict

