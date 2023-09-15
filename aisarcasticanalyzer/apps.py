from django.apps import AppConfig
from django.conf import settings
import os
import pickle


class AisarcasticanalyzerConfig(AppConfig):
    name = "aisarcasticanalyzer"
    path = os.path.join(settings.MODELS,"models.p")
    with open(path,"rb") as pickled:
        data = pickle.load(pickled)
    bi_lstm_model = data['bi_lstm_model']
    tokenizer=data['tokenizer']
    
