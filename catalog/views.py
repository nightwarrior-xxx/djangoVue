from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.decorators import api_view


def public(request):
    return HttpResponse("You don't need to be authenticated to see this message")


@api_view(["GET"])
def private(request):
    return HttpResponse("You should only see this message if you are authenticated")
