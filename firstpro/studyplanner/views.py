from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
# Create your views here.
posts = [
    {
        'author': 'Dhanush',
         'title': 'Hobart',
         'content': 'Meta',
         'date_posted' : '24/3/2022',
         'link' : 'https://cdn.britannica.com/61/137061-050-7B320944/Hobart-Tasmania-Australia.jpg'
    },
    {   
        'author' : 'Chakku',
         'title': 'Perth',
         'content': 'Food',
         'date-posted': '3/3/2022',
         'link' : 'data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAoHCBUVFBcVFRUYFxcZFxkaGhoZGh0aHBwgGxkaGRwgICIaICwjHB0pIBoZJDUkKC0vMjIyGiI4PTgxPCwxMi8BCwsLDw4PHRERHTgpIygxMTcvMzMQAPdfyn7o61KlbMf+nFmd/tbp4VOPD/AN0sY7Z7RXPJpuamJIhtICmABoV/U+Ik5JqVKOhpJ+0EcwotKOx39B1IUnyMdqlSpSk8w5//2Q=='
    }

]
 

def home(request):
    context ={
        'posts': Post.objects.all()
    }
    return render(request, 'studyplanner/home.html', context)
 

def about(request):
    return render(request, 'studyplanner/about.html', {'title': 'Great_Title'})

# def weekly_timetable(request, day):
    # text =" "
    # if day == 'Monday':
        # text = "Today I will learn ML"
    # elif day =='Tuesday':
        # text = "Today I will learn AI"
    # return HttpResponse(text)