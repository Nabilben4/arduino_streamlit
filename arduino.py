import streamlit as st
import subprocess

def discover_devices():
    try:
        result = subprocess.check_output(["hcitool", "scan"]).decode("utf-8").splitlines()
        devices = [line.split("\t") for line in result[2:] if "\t" in line]
        return devices
    except subprocess.CalledProcessError as e:
        st.error(f"Erreur lors de la découverte des périphériques : {e}")
        return []

def send_data_to_device(device_address, message):
    # Implémentez la logique d'envoi de données ici
    st.success(f"Données envoyées à l'adresse {device_address} : {message}")

# Interface utilisateur avec Streamlit
st.title("Communication Bluetooth avec Streamlit")

# Liste des appareils Bluetooth à proximité
device_list = discover_devices()

# Demander à l'utilisateur de choisir un appareil dans la liste
selected_device = st.selectbox("Sélectionnez un appareil Bluetooth", [f"{name} ({address})" for address, name in device_list])

# Demander à l'utilisateur le message à envoyer
message = st.text_input("Entrez le message à envoyer")

# Bouton pour envoyer le message au périphérique sélectionné
if st.button("Envoyer"):
    if selected_device and message:
        # Extraire l'adresse MAC à partir de la sélection
        selected_address = selected_device.split(" ")[-1][1:-1]
        send_data_to_device(selected_address, message)
    else:
        st.warning("Veuillez sélectionner un appareil et saisir le message.")
