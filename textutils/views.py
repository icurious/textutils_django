# Created by me

import os
from django.http import HttpResponse
from django.shortcuts import render



def index(request):
    return render(request,'index.html')
    # return HttpResponse("Hello there...")

def analyzer(request):
    # Get text from HTML
    get_text = request.GET.get('text','default')

    # Create text object
    text_object = AnalyzeText(get_text)

    # GET Flags from html page
    remove_punc_flag = request.GET.get('removepunc', 'off')
    remove_new_line_flag = request.GET.get('removenewline', 'off')
    remove_extra_space_flag = request.GET.get('removeextraspace', 'off')
    capitalize_flag = request.GET.get('capsall', 'off')
    character_count_flag = request.GET.get('charcount', 'off')

    # Check flags and analyze
    if remove_punc_flag == 'on':
        analyzed_text = text_object.remove_punctuations()
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed_text}
        return render(request, 'analyzer.html', params)

    elif remove_new_line_flag == 'on':
        analyzed_text = text_object.remove_newline()
        params = {'purpose': 'Removed New Lines', 'analyzed_text': analyzed_text}
        return render(request, 'analyzer.html', params)

    elif remove_extra_space_flag == 'on':
        analyzed_text = text_object.remove_extra_space()
        params = {'purpose': 'Removed Extra Spaces', 'analyzed_text': analyzed_text}
        return render(request, 'analyzer.html', params)

    elif capitalize_flag == 'on':
        analyzed_text = text_object.capitalize()
        params = {'purpose': 'Capitalized', 'analyzed_text': analyzed_text}
        return render(request, 'analyzer.html', params)

    elif character_count_flag == 'on':
        analyzed_text = "Your Character Count is {}" .format(text_object.character_counter())
        params = {'purpose': 'Capitalized', 'analyzed_text': analyzed_text}
        return render(request, 'analyzer.html', params)

    else:
        return HttpResponse("Error")


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
            if character != '\n':
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

    def character_counter(self):
        return str(len(self.text))














# def about(request):
#     original_path = os.getcwd()
#     path = 'C:\\Users\\GS-3348\\Desktop\\Django\\textutils'
#     filename = 'one.txt'
#     os.chdir(path)
#
#     for root, dirs, files in os.walk(path):
#         for name in files:
#             if name == filename:
#                 with open(filename, 'r') as f:
#                     lines = f.readlines()
#     _about = "".join(lines)
#     print(_about)
#     return HttpResponse(_about)
#
# def navigator(request):
#     html = '''
#             <h1>Site Navigator </h1>
#             <br>
#             <ol>
#             <li><a href = https://www.google.com/>Google</a></li>
#             <li><a href = https://linuxize.com/>Linux</a></li>
#             <li><a href = https://www.geeksforgeeks.org/>GeeksForGeeks</a></li>
#             </ol>
#             '''
#     return HttpResponse(html)
#
#
# def home(request):
#     return HttpResponse("Home")
#
# def removepunc(request):
#     # Get text from html
#     get_text = request.GET.get('text', 'default')
#     print(get_text)
#     return HttpResponse("Remove Punctuation")
#
# def newlineremove(request):
#     return HttpResponse("Remove New Line")
#
# def capitalizefirst(request):
#     return HttpResponse("Capitalize First")
#
# def spaceremover(request):
#     return HttpResponse("Space Remover")
#
# def charcount(request):
#     return HttpResponse("Character Count")