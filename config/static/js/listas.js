// Asumiendo que tienes una función para manejar la solicitud AJAX
function obtenerInformacionListaReproduccion(url) {
    $.ajax({
        type: 'POST',
        url: 'tu-url-de-vista',  // Asegúrate de reemplazar 'tu-url-de-vista' con la URL de tu vista de Django
        headers: { 'X-Requested-With': 'XMLHttpRequest' },
        data: { 'url': url },
        success: function (data) {
            // Manipula los datos devueltos por la vista Django
            if ('list_info' in data) {
                // Itera sobre los elementos de la lista de información
                data.list_info.forEach(function (video) {
                    console.log('URL:', video.url);
                    console.log('Título:', video.title);
                    // Puedes hacer lo que quieras con la información aquí
                });
            } else if ('error' in data) {
                console.error('Error:', data.error);
            }
        },
        error: function (xhr, errmsg, err) {
            console.error('Error en la solicitud AJAX:', errmsg);
        }
    });
}

// Llamada de ejemplo
var urlDeLaLista = 'tu-url-de-lista';  // Reemplaza 'tu-url-de-lista' con la URL real de la lista
obtenerInformacionListaReproduccion(urlDeLaLista);
