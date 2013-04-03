from django.shortcuts import render

from .forms import ExampleForm


def home(request):
	example_form = ExampleForm();
	context = {
		'example_form': example_form,
	}
	return render(request, 'index.jade', context)
