from django.shortcuts import render
from newspaper import Article
from .text_preprocessing import text_pipe
import pickle

def index(request):
    return render(request, 'main.html')

# payment_id = request.POST.get('payment_id', '')
# In main.html: <form action={% url 'predict' %}  method="POST">
with open('./predict/gbcfull.pickle', 'rb') as model_f:
	model = pickle.load(model_f)

def predict(request, url):
    if request.method == 'POST':
        article = Article(url)
        article.download()
        article.parse()
        text = article.text
        text = text_pipe(text)
        pred = model.predict([text])

        return render(request, 'main.html',
                      predict_value='This news article is "{}"'.format(pred[0]))
