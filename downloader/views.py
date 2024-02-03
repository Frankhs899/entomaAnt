from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, JsonResponse
import os
from pytube import YouTube

#Funcion para descargar video
def video(request):
    if request.method == 'POST' and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        url = request.POST.get('url')
        try:
            yt = YouTube(url)
            video_stream = yt.streams.get_highest_resolution()
            video_stream.download(output_path='media/yt/video/')
            file_name = video_stream.default_filename
            file_path = os.path.join('media/yt/video/', file_name)
            # Devolver la ruta del archivo para su posterior descarga
            print(file_path)
            return JsonResponse({'file_path': file_path}) 

        except Exception as e:
            error_message = f'Ha ocurrido un error: {str(e)}'
            return JsonResponse({'error': error_message})

    return JsonResponse({'error': 'Método no permitido'}, status=400)

#Funcion para descargar audio
def audio(request):
    if request.method == 'POST' and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        url = request.POST.get('url')
        try:
            yt = YouTube(url)
            audio_stream = yt.streams.filter(only_audio=True).first()
            audio_stream.download(output_path='media/yt/audio/')
            file_name = audio_stream.default_filename
            file_path = os.path.join('media/yt/audio/', file_name)
            # Devolver la ruta del archivo para su posterior descarga
            print(file_path)
            return JsonResponse({'file_path': file_path}) 

        except Exception as e:
            error_message = f'Ha ocurrido un error: {str(e)}'
            return JsonResponse({'error': error_message})

    return JsonResponse({'error': 'Método no permitido'}, status=400)
    pass

#Funcion obtener info de el video
def obtener_informacion(request):
    if request.method == 'POST' and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        url = request.POST.get('url')
        if url:
                try:
                    yt = YouTube(url)
                    video_info = {
                        'url':url,
                        'title':yt.title,
                        'duration':yt.length
                    }
                    print(video_info)
                    return JsonResponse({'video_info':video_info})
                except Exception as e:
                    error_message = f'Error: {str(e)}'
                    return JsonResponse({'error': error_message})
    return JsonResponse({'error': 'Método no permitido'}, status=400)

# Renderizado de pagina
class HomePageView(View):

    template_name = 'home_page.html'

    def get(self, request):
        return render(request, self.template_name)

