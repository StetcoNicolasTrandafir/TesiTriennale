import os

def process_txt_files(input_folder, output_file):
    unique_strings = set()  # Utilizziamo un set per evitare duplicati

    # Iteriamo attraverso tutti i file nella cartella
    for filename in os.listdir(input_folder):
        if filename.endswith(".txt"):
            file_path = os.path.join(input_folder, filename)
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:  # Ignora caratteri non validi
                for line in file:
                    # Facciamo lo split sulla prima occorrenza di ":"
                    split_line = line.split(":", 1)
                    if split_line:
                        first_part = split_line[0].strip()  # Rimuoviamo spazi bianchi
                        if first_part not in unique_strings:
                            unique_strings.add(first_part)

    # Scriviamo le stringhe uniche su un file di output
    with open(output_file, 'w', encoding='utf-8') as output:
        for item in sorted(unique_strings):  # Ordinamento opzionale
            output.write(item + '\n')


# Esempio di utilizzo:
input_folder = 'C:\\Users\\39388\\Desktop\\Tesi\\NervousGPT\\Nervous-main\\python_code\\musicaEmpiricalProb\\genres'  # Sostituisci con il percorso della cartella di input
output_file = 'C:\\Users\\39388\\Desktop\\Tesi\\attributes.txt'  # Sostituisci con il percorso del file di output

process_txt_files(input_folder, output_file)
