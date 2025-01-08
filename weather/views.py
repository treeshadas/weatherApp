from django.shortcuts import render
from django.template.loader import get_template

def index(request):
    # Debug template discovery
    try:
        template = get_template('weather/index.html')
        print(f"Template found at: {template.origin}")  # Prints the template path if found
    except Exception as e:
        print(f"Template error: {e}")  # Prints the error if not found

    return render(request, 'weather/index.html')
