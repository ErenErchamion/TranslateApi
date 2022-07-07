from django.http import HttpResponse
from transformers import pipeline

def translate(request,lang):
    if lang=="en-tr":
        modelname="Helsinki-NLP/opus-mt-tc-big-en-tr"
    else:
        modelname="Helsinki-NLP/opus-mt-"+lang
    data = str(request.body)


    pipe = pipeline("translation", model=modelname)
    translatedtext=(pipe(data))

    return HttpResponse(translatedtext)
