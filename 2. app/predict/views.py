from django.shortcuts import render
from newspaper import Article
from .text_preprocessing import text_pipe
import pickle

def index(request):
    return render(request, 'main.html')


with open('./predict/gbcfull.pickle', 'rb') as model_f:
	model = pickle.load(model_f)

def predict(request):
    if request.method == 'POST':
        url=request.POST.get('url')
        article = Article(str(url))
        article.download()
        article.parse()
        text = article.text
        text = text_pipe(text)
        pred = model.predict([text])
        pred_text = "True" if pred[0]==1 else "False"
        predict_value='This news article is "{}"'.format(pred_text)
        context = {'predict_value': predict_value}

        return render(request, 'main.html',
                      context)
