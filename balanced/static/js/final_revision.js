$(document).ready(function(){
    $('#registerAll').click(function() {
        var boolean = confirm('¿Desea ingresar los proyectos no revisados a este ciclo?')
        if(boolean == true){
            reg();
            alert('Datos correctamentes actualizados');
            reload();
        }
    });
    function reg(){
        $('#tableRevisiones tr').each(function () {
            var row = $(this);
            if (row.data('visible') == 1) {
                if (row.data('revisado') == 'no') {
                    var proyecto = row.data('id');
                    var avance = row.data('avance');
                    var ciclo = $('#clave_activa').val();
                    $.post('/balanced/check/add/full/', {
                        proyecto: proyecto,
                        avance: avance,
                        ciclo: ciclo
                    }, actualizar_check(proyecto));
                }
            }
        });
    }
    function actualizar_check(proyecto){
    }
    function reload(){
        location.reload();
    }
});
