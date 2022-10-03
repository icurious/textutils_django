# Created by me

import os
from django.http import HttpResponse
from django.shortcuts import render



def index(request):
    return render(request,'index.html')
    # return HttpResponse("Hello there...")

def analyzer(request):
    # Get text from HTML
    get_text = request.POST.get('text','default')

    # Create text object
    text_object = AnalyzeText(get_text)

    # GET Flags from html page
    remove_punc_flag = request.POST.get('removepunc', 'off')
    remove_new_line_flag = request.POST.get('removenewline', 'off')
    remove_extra_space_flag = request.POST.get('removeextraspace', 'off')
    capitalize_flag = request.POST.get('capsall', 'off')

    # Check flags and analyze
    if remove_punc_flag == 'on':
        analyzed_text = text_object.remove_punctuations()
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed_text}
        text_object = AnalyzeText(analyzed_text)

    if remove_new_line_flag == 'on':
        analyzed_text = text_object.remove_newline()
        params = {'purpose': 'Removed New Lines', 'analyzed_text': analyzed_text}
        text_object = AnalyzeText(analyzed_text)

    if remove_extra_space_flag == 'on':
        analyzed_text = text_object.remove_extra_space()
        params = {'purpose': 'Removed Extra Spaces', 'analyzed_text': analyzed_text}
        text_object = AnalyzeText(analyzed_text)

    if capitalize_flag == 'on':
        analyzed_text = text_object.capitalize()
        params = {'purpose': 'Capitalized', 'analyzed_text': analyzed_text}

    if remove_punc_flag != 'on' and remove_new_line_flag != 'on' and remove_extra_space_flag != 'on' and capitalize_flag != 'on':
        return HttpResponse("Error")

    return render(request, 'analyzer.html', params)


class AnalyzeText:
    def __init__(self,text):
        self.text = text

    def remove_punctuations(self):
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        result = ''
        for character in self.text:
            if character not in punctuations:
                result+=character
        return result

    def remove_newline(self):
        result = ''
        print(self.text)
        for character in self.text:
            if character != '\n' and character!='\r':
                result+=character
        return result

    def remove_extra_space(self):
        result = ''
        for i, char in enumerate(self.text):
            if not (self.text[i] == " " and self.text[i+1] == " "):
                result+=char
        return result

    def capitalize(self):
        result = ''
        for letter in self.text:
            result+=letter.upper()
        return result
















