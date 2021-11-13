from django.http import HttpResponseRedirect
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, get_object_or_404
from .models import Movie
from .forms import addMovie, UpdateMovieForm

# Create your views here.

def home(request):
    movies = Movie.objects.all()
    return render(request, '../templates/mainPage.html',{'movies':movies})

def addNew(request):
    if request.method == "POST":
        form = addMovie(request.POST)
        if(request.FILES):
            print("here")
        # getting image
            imageName = request.FILES['img']
            fss = FileSystemStorage()
            img = fss.save(imageName.name, imageName)
            
            if form.is_valid():
                form.cleaned_data['img'] = fss.url(img)
                print("image url")
                print(form.cleaned_data['img'][7:])
                print(form.cleaned_data['img'])
                newMovie = Movie(
                    title=form.cleaned_data['title'],
                    img = form.cleaned_data['img'][7:],
                    description=form.cleaned_data['description']
                )
                newMovie.save()
        else: 
            if form.is_valid():
                newMovie = Movie(
                    title=form.cleaned_data['title'],
                    img = 'default-movie.png',
                    description=form.cleaned_data['description']
                )
                newMovie.save()
        
        return HttpResponseRedirect('/')
    else:
        form = addMovie()
        return render(request, '../templates/addNew.html', {"form":form})

def updateMovie(request, pk):
    movie = get_object_or_404(Movie,id=pk)
    if request.POST:
        form = UpdateMovieForm(request.POST or None, request.FILES or None, instance=movie)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            movie = obj
        return HttpResponseRedirect('/')    
    form = UpdateMovieForm(
            initial = {
                'title': movie.title,
                'description': movie.description,
                'img': movie.img,
            }
    )
    return render(request, '../templates/update.html', {'form':form})

def deleteMovie(request, pk):
    movie = get_object_or_404(Movie,id=pk)
    movie.delete()
    return HttpResponseRedirect('/')