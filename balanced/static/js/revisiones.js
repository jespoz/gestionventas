$(document).on('ready', main);

function main() {

    $.ajaxSetup({
        beforeSend: function(xhr, settings){
            if(settings.type == 'POST'){
                xhr.setRequestHeader('X-CSRFToken', $('[name="csrfmiddlewaretoken"]').val());
            }
        }
    });
    $('[id^=contenido-proyecto-]').on('click', 'a', enviar_revision);
    $('[id^=proyectos]').on('click', 'a', cargar_revision);
    $('[id^=revision]').on('click', 'a', mostrar_revision);



}

function mostrar_revision(data){
    var id = $(data.currentTarget).data('id');
    if($('#tr' + id).hasClass('hidden')) {
        $('[id^=tr]').addClass('hidden');
        $('#tr' + id).removeClass('hidden');
        $('#contenido-proyecto-' + id).load('/balanced/carga_check/' + id);
    }else{
        $('#tr' + id).addClass('hidden');
        $('#tr-obs' + id).addClass('hidden');
         $('#contenido-proyecto-' + id).empty()
    }
}

function cargar_revision(data){
    var id = $(data.currentTarget).data('id');
    if($('#tr' + id).hasClass('hidden')) {
        $('[id^=tr]').addClass('hidden');
        $('#tr' + id).removeClass('hidden');
        $('#contenido-proyecto-' + id).load('/balanced/carga_revision/' + id);
    }else{
        $('#tr' + id).addClass('hidden');
        $('#tr-obs' + id).addClass('hidden');
         $('#contenido-proyecto-' + id).empty()
    }
}

function enviar_revision(){
    var proyecto = $('#proyecto').val();
    var valor = $('#id_ciclo').val();
    var obs = $('#observacion').val();
    if(obs==''){
        $('#form-group span').text('* Debe ingresar una observación');
    }else{
        $.post('/balanced/revisiones/add/', {proyecto: proyecto, valor: valor, obs: obs}, actualizar_observaciones);
    }
}

function actualizar_observaciones(){
    location.reload();
}