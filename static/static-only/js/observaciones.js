$(document).on('ready', main);

function main() {
    $.ajaxSetup({
        beforeSend: function(xhr, settings){
            if(settings.type == 'POST'){
                xhr.setRequestHeader('X-CSRFToken', $('[name="csrfmiddlewaretoken"]').val());
            }
        }
    });
    $('#observacion_new button').on('click', enviar_observacion);
}

function enviar_observacion(){
    var input = $('#agregar_observacion textarea:visible');
    var id = $('#agregar_observacion input:hidden');
    if(input.val() != ''){
        $.post('/balanced/observaciones/add/', {observacion: input.val(), id: id.val()}, actualizar_observaciones);
    }
}

function actualizar_observaciones(data){
    id = 0;
    $.each(data.observaciones, function (key, val) {
        id = val.fields['proyecto'];
    });
    var obs_div = $('#obs' + id);
    obs_div.html('');
    $.each(data.observaciones, function (key, val) {
        if (val.fields['observacion'] != null) {
            $('<div class="note note-success"><a data-id="' + val.pk + '" style="font-family: Open Sans; font-size: 12px; margin-bottom:0; cursor: pointer;">' + val.fields['observacion'].substr(0, 80) + '... </a>').appendTo(obs_div)
        }
    });
    $('#myModal').modal('hide');
}
