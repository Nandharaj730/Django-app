def upload(f):
    with open('nandhaapp/fileupload/'+ f.name , 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)