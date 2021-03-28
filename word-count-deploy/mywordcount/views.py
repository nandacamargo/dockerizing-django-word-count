from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render


""" 
Read a given file and return its content
Parameters => file_name: the name of the file
Returns => result: the file content 
"""
def read_file(file_name):
    file_name = "media/" + file_name
    with open(file_name, 'r') as input_file:
        result = input_file.readlines()
    return result

""" 
It contains the logic for counting the number of words
Parameters => request: the request to count the words
Returns => renders count page 
"""
def count_page(request):

    words_count = 0
    file_to_read = request.session['file_name']
    full_text = ""

    if (file_to_read != None):
        user_input = read_file(file_to_read)

        for i in range(len(user_input)):
            full_text += user_input[i]

        words_count = len(full_text.split())

    return render(request, '../templates/count.html', 
    { 'input_text' : full_text, 'words_count' : words_count })


""" 
It contains the logic for uploading and saving the given file
Parameters => request: the request to upload the file
Returns => renders home page 
"""
def upload(request):
    context = {}
    if request.method == 'POST':
        if 'document' in request.FILES:
            uploaded_file = request.FILES['document']
            context['uploaded'] = uploaded_file
            fs = FileSystemStorage()
            name = fs.save(uploaded_file.name, uploaded_file)
            context['url'] = fs.url(name)

            file_to_read = ".." + context['url']
            context['file_name'] = file_to_read
            request.session['file_name'] = file_to_read
                
    return render(request, 'home.html', context)