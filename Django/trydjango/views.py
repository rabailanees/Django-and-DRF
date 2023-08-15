#To render html web pages
from django.http import HttpResponse
import random
from articles.models import Article
from django.template.loader import render_to_string

def home_view(request):
    #Take in request (Django sends request)
    #Return HTML as a response (We pick to return the response)
    name='Rabail' #Hard coded
    number=random.randint(8,4526779) #psuedo random
    random_id=random.randint(1,4)
    article_obj=Article.objects.get(id=random_id)
    my_list=[102,13,34,678,1000]
    my_list_str=""
    for x in my_list:
        my_list_str += f"number is {x}"
        

    context={
        "my_list_str":my_list_str,
        "object":article_obj,
        "title":article_obj.title,
        "id":article_obj.id,
        "content":article_obj.content
    }
    #API call to some REST API with python and pthon requests
    #Django templates
    HTML_STRING=render_to_string("home-view.html",context=context)
    
    #HTML_STRING="""<h1>{title} (id : {id})</h1> <p> {content}</p>""".format(**context)
    #print(100*100)
    return HttpResponse(HTML_STRING)