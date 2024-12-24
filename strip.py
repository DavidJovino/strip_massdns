import argparse

def process_file(input_file, output_file):
    results = []
    
    # Abrir o arquivo para leitura
    with open(input_file, 'r') as file:
        for line in file:
            # Ignorar linhas vazias
            if line.strip():
                # Dividir a linha em palavras
                words = line.split()
                
                # Remover o ponto final da primeira e última palavra, se existir
                first_word = words[0].rstrip('.')
                last_word = words[-1].rstrip('.')
                
                # Adicionar ao resultado
                results.append(f"{first_word}\n{last_word}")
    
    # Escrever os resultados no arquivo de saída
    with open(output_file, 'w') as file:
        for result in results:
            file.write(result + '\n')

def main():
    # Configurar o parser de argumentos
    parser = argparse.ArgumentParser(description="Processa um arquivo para extrair a primeira e a última palavra de cada linha.")
    parser.add_argument('input_file', help="Arquivo de entrada a ser processado.")
    parser.add_argument('-o', '--output_file', required=True, help="Arquivo de saída onde os resultados serão salvos.")
    
    # Parse dos argumentos
    args = parser.parse_args()
    
    # Processar o arquivo
    process_file(args.input_file, args.output_file)
    print(f"Processamento concluído! Resultados salvos em {args.output_file}.")

if __name__ == "__main__":
    main()
