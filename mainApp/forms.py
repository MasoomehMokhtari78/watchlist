from django import forms
from .models import Movie
class addMovie(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
        }
    ))
    description = forms.CharField(required=False,
        widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'style': 'height: 100px;',
        }
    )
    )
    img = forms.ImageField(required=False)
    class Meta:
        model = Movie
        fields = ('title','img','description')

class UpdateMovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'img', 'description']
    # custom save method
    def save(self, commit=True):
        movie = self.instance
        movie.title = self.cleaned_data['title']
        movie.description = self.cleaned_data['description']

        if self.cleaned_data['img']:
            print(self.cleaned_data['img'])
            movie.img = self.cleaned_data['img']
        if commit:
            movie.save()
        return movie