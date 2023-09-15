from django.shortcuts import render
from .apps import AisarcasticanalyzerConfig
from django.http import JsonResponse
from rest_framework.views import APIView
# Create your views here.
class call_model(APIView):
    def get(self,request):
        if request.method == 'GET':
            text = request.GET.get("text")
            input_encoded = AisarcasticanalyzerConfig.tokenizer.encode_plus(text)#,add_special_tokens=True,max_length=128,return_attention_mask=True,padding='max_length',truncation=True,return_tensors='tf')
            prediction = AisarcasticanalyzerConfig.bi_lstm_model.predict(input_encoded['input_ids'])
            response = {'text_sentiment':prediction}
            return JsonResponse(response)