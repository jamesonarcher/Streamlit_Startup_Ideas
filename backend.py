from appwrite.client import Client
from appwrite.services.database import Database
import streamlit as st

client = Client()
client.set_endpoint('https://cloud.appwrite.io/v1') 
client.set_project('64e7d83f77da01e698aa')
client.set_key('58a700f1b7dfc9a776dfaf6e0ae9917438a2eeefa59b872a7da4cfec30dbc1240df686aa4ecd87b594f3608cb5508ce331d5da9c64f7d543f9d26bd67d805714173a26e419aadf5868e25f73c907c2d18772b89678af7039f1229a0ce52c7f28fffffde60f537be6f042b52b816b023d4f8603d5177add039101b3acdc5741a6')

database = Database(client)

def add_idea_to_appwrite(idea_text):
    data = {
        "idea": idea_text
    }
    response = database.create_document('64e7d86865aea5e8e02e', data)
    return response

# Continue with the Streamlit code...
