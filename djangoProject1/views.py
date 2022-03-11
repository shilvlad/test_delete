import numpy as np

from django.http import HttpResponse

def main(request):
    print(np.array([1, 2, 3]))

    return HttpResponse("Hello")