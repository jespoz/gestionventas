$(document).ready(function(){
    $('#checkFinal').click(function(){
        enviar_check();
    });
    function enviar_check(){
        var proyecto = $('#id_proyecto').val();
        var avance = $('#id_avance').val();
        var ciclo = $('#id_ciclo').val();
        $.post('/balanced/check/add/', {proyecto: proyecto, avance: avance, ciclo: ciclo}, actualizar_check);
    }
    function actualizar_check(){
        location.reload();
    }
});
