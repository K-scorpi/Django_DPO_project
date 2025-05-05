from django.http import HttpResponse
from django.shortcuts import render
import logging
import datetime


logger = logging.getLogger(__name__)
def my_view(request):
    logger.info('This is an information message.')
    logger.warning('This is a warning message.')
    logger.error('This is an error message.')
    return HttpResponse('Hello, world!')

def welcome_page(request):
    logger.warning('Homepage was accessed at '+str(datetime.datetime.now())+ 'hours!')
    return HttpResponse("<h1>Welcome to web application development course 2023 (URFU/RTF) :)</h1>")