import time

def calcular_bpm():
    print("--- Taaz Music Tools: BPM Tapper ---")
    print("Pressione ENTER no ritmo do Groove. Digite 's' para sair.")
    taps = []
    while True:
        entrada = input(">> TAP <<")
        if entrada.lower() == 's': break
        taps.append(time.time())
        if len(taps) > 1:
            intervalo = sum([taps[i] - taps[i-1] for i in range(1, len(taps))]) / (len(taps) - 1)
            print(f"🔥 BPM Estimado: {round(60/intervalo, 1)}")
        if len(taps) > 10: taps.pop(0)

if __name__ == "__main__":
    calcular_bpm()