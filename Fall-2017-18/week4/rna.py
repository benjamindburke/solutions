rna_letters = {'A':'U', 'T':'A', 'C':'G', 'G':'C'}
rna_codon_list = {'UUU':'F', 'CUU':'L', 'AUU':'I', 'GUU':'V',
		  'UUC':'F', 'CUC':'L', 'AUC':'I', 'GUC':'V',
		  'UUA':'L', 'CUA':'L', 'AUA':'I', 'GUA':'V',
		  'UUG':'L', 'CUG':'L', 'AUG':'M', 'GUG':'V',
		  'UCU':'S', 'CCU':'P', 'ACU':'T', 'GCU':'A',
		  'UCC':'S', 'CCC':'P', 'ACC':'T', 'GCC':'A',
		  'UCA':'S', 'CCA':'P', 'ACA':'T', 'GCA':'A',
		  'UCG':'S', 'CCG':'P', 'ACG':'T', 'GCG':'A',
		  'UAU':'Y', 'CAU':'H', 'AAU':'N', 'GAU':'D',
		  'UAC':'Y', 'CAC':'H', 'AAC':'N', 'GAC':'D',
		  'UAA': '', 'CAA':'Q', 'AAA':'K', 'GAA':'E',
		  'UAG': '', 'CAG':'Q', 'AAG':'K', 'GAG':'E',
		  'UGU':'C', 'CGU':'R', 'AGU':'S', 'GGU':'G',
		  'UGC':'C', 'CGC':'R', 'AGC':'S', 'GGC':'G',
		  'UGA': '', 'CGA':'R', 'AGA':'R', 'GGA':'G',
		  'UGG':'W', 'CGG':'R', 'AGG':'R', 'GGG':'G'}

def byThrees(text):
    threes = []
    for i in range(0, len(text), 3):
	threes.append(text[i:i+3])
    return threes

def convert(text):
    letters = [letter for letter in text]
    rna = []
    for letter in letters:
	rna.append(rna_letters[letter])
    return rna

def main():
    dna = "TACCGGTACCGCGGGTCTTGACTCTAGTTATCATGGGCATAATTGCCCACT"
    rna = "".join(letter for letter in [rna_letters[letter] for letter in dna])
    rna = [triplet for triplet in byThrees(rna)]

    protein = "".join(letter for letter in[rna_codon_list[triplet] for triplet in rna])

    print(protein)

if __name__ == "__main__":
    main()