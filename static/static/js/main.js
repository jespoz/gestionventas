$(document).on('ready', main);

function main(){
    $('[id^=proyectos]').on('click', 'a', cargar_historia_proyecto);
}

function cargar_historia_proyecto(data){
    var id = $(data.currentTarget).data('id');
    if($('#tr' + id).hasClass('hidden')) {
        $('[id^=tr]').addClass('hidden');
        $('[id^=tr-obs]').addClass('hidden');
        $.get('/balanced/carga_evolucion_proyecto/' + id, cargar_proyecto);
        $('#tr' + id).removeClass('hidden');
        $('#tr-obs' + id).removeClass('hidden');
    }else{
        $('#tr' + id).addClass('hidden');
        $('#tr-obs' + id).addClass('hidden');
    }
}

function cargar_proyecto(data){

    var contenido = $('#contenido-proyecto-' + data.id);
    contenido.html('');
    $('<img class="img-responsive" src="/static/img/descarga.png"/>').appendTo(contenido);
    $('#proyectos').css('left', '-110%');
    contenido.css('left', '0');
    contenido.on('click', 'a', function(){
       contenido.css('left', '-110%');
        $('#proyectos').css('left', '0');
    });
}


function cargar_observaciones(data){
    var contenido = $('#observacion-proyecto-' + data.id);
    contenido.html('');
}

