import subprocess
import string

# Abbiamo aggiunto anche le parentesi graffe e i numeri, per coprire tutto il formato "flag{...}"
charset = string.ascii_letters + string.digits + "{}_-!?"

target_length = 23
known_flag = ""

print("[*] Inizio Brute-Force automatico con Frida (Versione Veloce)...")

while len(known_flag) < target_length:
    found_next_char = False
    
    # CORREZIONE: Vogliamo vedere il controllo SUCCESSIVO! 
    # Quindi se abbiamo 0 lettere, vogliamo 2 log. Se abbiamo 1 lettera, vogliamo 3 log.
    expected_logs = len(known_flag) + 2 
    
    for char in charset:
        # Costruiamo la stringa finta
        padding = "A" * (target_length - len(known_flag) - 1)
        test_flag = known_flag + char + padding
        
        # Aggiunto '-q' per non stampare il banner gigante di Frida, velocizza tantissimo!
        cmd = ["frida", "-q", "-l", "solve.js", "-f", "./morph", "--", test_flag]
        
        # Catturiamo l'output
        result = subprocess.run(cmd, capture_output=True, text=True)
        output = result.stdout + result.stderr
        
        # CORREZIONE: Contiamo la parola "p1:" per evitare problemi coi codici colore del terminale
        log_count = output.count("p1:")
        
        if log_count >= expected_logs:
            known_flag += char
            print(f"[+] Trovato carattere {len(known_flag)}: '{char}' -> Flag parziale: {known_flag}")
            found_next_char = True
            break # Passa a cercare la lettera successiva
            
    if not found_next_char:
        print(f"\n[-] Bloccato alla lettera {len(known_flag) + 1}.")
        # Se si blocca, stampiamo cosa ha visto Python per fare debug
        print("Ultimo output di Frida analizzato:")
        print(output)
        break

print(f"\n[!] PROCESSO TERMINATO. Risultato finale: {known_flag}")