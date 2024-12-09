def create_codon_dict(file_path):
    codon_dict = {}
    file = open(file_path)
    lines = file.readlines()
    file.close()
    for line in lines:
        line = line.strip()
        if line:
            parts = line.split()
            codon = parts[0]
            amino_acid = parts[1]
            codon_dict[codon] = amino_acid
        else:
            print("invalid line")
    return codon_dict

