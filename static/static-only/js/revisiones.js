$(document).on('ready', main);

function main(){
    $('input[type="range"]').rangeslider();
    $('[id^=proyectos]').on('click', 'a', function(info){
        id = $(info.currentTarget).data('id');
        alert(id);
        if ($('#tr' + id).hasClass('hidden')) {
            $('[id^=tr]').addClass('hidden');
            $('#tr' + id).removeClass('hidden');
            var contenido = $('#contenido-proyecto-' + id);
            contenido.html('');
            $('<h2>Hola Mundo ' + id + '</h2>').appendTo(contenido);
        }else{
            $('#tr' + id).addClass('hidden');
            $('#tr-obs' + id).addClass('hidden');
        }
    });
}