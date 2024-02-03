from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from pytube import Playlist, YouTube

class ListasView(View):
    template_name = 'listas/listas.html'

    def get(self, request):
        return render(request, self.template_name)
    
    def post(self, request):
        if request.method == 'POST':
            try:
                url = request.POST.get('url')
                list_info = []
                p = Playlist(url)
                for urlvideo in p.video_urls:
                    yt= YouTube(urlvideo)
                    video_info = {
                        'url':urlvideo,
                        'title':yt.title,
                    }
                    list_info.append(video_info)
                return JsonResponse({'list_info':list_info})
            except Exception as e:
                error_message = f'Ha ocurrido un error: {str(e)}'
                return JsonResponse({'error': error_message})
        return JsonResponse({'error': 'Método no permitido'}, status=400)