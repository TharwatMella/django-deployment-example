from django.shortcuts import render
from basic_app import models, forms


# Create your views here.
def index(request):
    return render(request, "basic_app/index.html")


def relative(request):
    print(request)
    return render(request, "basic_app/relative_url_templates.html")


def home(request):
    return render(request, "basic_app/base.html")


def other(request):
    return render(request, "basic_app/other.html")


def name_Form(request):

    nameForm = forms.NameForm()
    if request.method == "POST":
        nameForm = forms.NameForm(request.POST)
        print(nameForm)
        # print(nameForm.data)
        if nameForm.is_valid():
            name = nameForm.cleaned_data["name_field"]

            models.NameModel.objects.get_or_create(name_field=name)
    content = {"names": models.NameModel.objects.all(), "number": 200}
    return render(request, "basic_app/nameForm.html", context=content)
