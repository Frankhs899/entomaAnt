from django.shortcuts import render
from django.views import View
from django.http import JsonResponse, HttpResponse
import os
from pytube import YouTube


#Renderizando HomeView o pagina principal
class HomeView(View):
    template_name = 'home.html'

    def get(self, request):
        return render(request, self.template_name)
    
####################DESCARGA DE ARCHIVOS#####################################################################

def video(request):
    if request.method == 'POST' and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        url = request.POST.get('url')
        try:
            yt = YouTube(url)
            video_stream = yt.streams.get_highest_resolution()
            video_stream.download(output_path='media/yt/video/')
            file_name = video_stream.default_filename

            # Obtener la extensión del archivo
            _, file_extension = os.path.splitext(file_name)

            titulo = f'{yt.title}-{yt.author}'

            # Nuevo nombre del archivo
            nuevo_nombre = titulo + file_extension

            # Ruta original del archivo
            file_path_original = os.path.join('media/yt/video/', file_name)

            # Ruta nueva del archivo
            file_path_nuevo = os.path.join('media/yt/video/', nuevo_nombre)

            # Renombrar el archivo
            os.rename(file_path_original, file_path_nuevo)

            # Devolver la ruta del archivo para su posterior descarga
            return JsonResponse({'file_path': file_path_nuevo}) 
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

            # Obtener la extensión del archivo
            _, file_extension = os.path.splitext(file_name)

            titulo = f'{yt.title}-{yt.author}'

            # Nuevo nombre del archivo
            nuevo_nombre = titulo + file_extension

            # Ruta original del archivo
            file_path_original = os.path.join('media/yt/audio/', file_name)

            # Ruta nueva del archivo
            file_path_nuevo = os.path.join('media/yt/audio/', nuevo_nombre)

            # Renombrar el archivo
            os.rename(file_path_original, file_path_nuevo)

            # Devolver la ruta del archivo para su posterior descarga
            return JsonResponse({'file_path': file_path_nuevo}) 

        except Exception as e:
            error_message = f'Ha ocurrido un error: {str(e)}'
            return JsonResponse({'error': error_message})

    return JsonResponse({'error': 'Método no permitido'}, status=400)

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
                        'autor':yt.author,
                        'duration':yt.length
                    }
                    print(video_info)
                    return JsonResponse({'video_info':video_info})
                except Exception as e:
                    error_message = f'Error: {str(e)}'
                    return JsonResponse({'error': error_message})
    return JsonResponse({'error': 'Método no permitido'}, status=400)

# Renderizado de pagina
class ArchivosView(View):

    template_name = 'archivos.html'

    def get(self, request):
        return render(request, self.template_name)