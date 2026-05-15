import os
import shutil

def organizar_samples(diretorio):
    # Dicionário focado em Psytrance (Kicks, Bass, FX, etc.)
    categorias = {
        "Kicks": ["kick", "kck", "bd_"],
        "Snares_Claps": ["snare", "snr", "clap", "clp"],
        "Hats": ["hihat", "hat", "hh_", "openhh", "closedhh"],
        "Bass": ["bass", "bs_", "sub", "groove"],
        "FX": ["fx", "sweep", "riser", "downlifter", "impact", "noise"],
        "Synths_Leads": ["lead", "synth", "saw", "plp", "arpeggio", "acid"],
        "Percussion": ["perc", "rim", "shaker", "tamb"]
    }

    print(f"--- Taaz Sample Organizer ---")
    print(f"Organizando arquivos em: {diretorio}")

    if not os.path.exists(diretorio):
        print("Erro: Pasta não encontrada.")
        return

    for arquivo in os.listdir(diretorio):
        nome_lower = arquivo.lower()
        caminho_origem = os.path.join(diretorio, arquivo)

        if os.path.isdir(caminho_origem):
            continue

        moveu = False
        for categoria, keywords in categorias.items():
            if any(key in nome_lower for key in keywords):
                pasta_destino = os.path.join(diretorio, categoria)
                
                if not os.path.exists(pasta_destino):
                    os.makedirs(pasta_destino)
                
                shutil.move(caminho_origem, os.path.join(pasta_destino, arquivo))
                print(f" [OK] {arquivo} -> {categoria}")
                moveu = True
                break
        
        if not moveu:
            print(f" [!] Ignorado (sem categoria): {arquivo}")

if __name__ == "__main__":
    caminho = input("Digite o caminho da sua pasta de samples: ")
    organizar_samples(caminho)