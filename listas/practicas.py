from pytube import Playlist, YouTube

url_lista = 'https://www.youtube.com/playlist?list=PL4yIeklk7xDoM3unGx3Yvkik53N8KhnEN'
lista = Playlist(url_lista)
list_info = []

for url in lista.video_urls:
    yt = YouTube(url)
    video_info = {
        'url':url,
        'title':yt.title,
    }
    list_info.append(video_info)
    print(video_info)

print('Lista info')
print(list_info)

#---------------------------------------
def info_lista_rep(request):
    if request.method == 'POST' and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        url = request.POST.get('url')
        if url:
            try:
                list_info = []
                p = Playlist(url)
                for url2 in p.video_urls: 
                    yt = YouTube(url2)
                    video_info={
                        'url':url2,
                        'title':yt.title,
                    }
                    list_info.append(video_info)
                return JsonResponse({'list_info':list_info})

            except Exception as e:
                error_message = f'Ha ocurrido un error: {str(e)}'
                return JsonResponse({'error': error_message})
    return JsonResponse({'error': 'Método no permitido'}, status=400)