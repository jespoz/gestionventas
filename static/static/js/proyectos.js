$('#id_objetivo').css('width', '100%');
$('#balanced_home').removeClass('active');
$('#balanced_proyectos').addClass('active');
$('.vDateField').datepicker({ dateFormat: "dd/mm/yy" });
$('#id_dimension').on('change', filtro_dimension);

function filtro_dimension(){
    var id = this.value
    $.get('/balanced/objetivos_filtro/' + id, cargar_objetivos);
}

function cargar_objetivos(data){
    var contenido = $('#id_objetivo');
    contenido.html('');
    $('<option value="" selected="selected">---------</option>').appendTo(contenido);
    $.each(data.objetivos, function (key, val) {
        id = val.pk;
        value = val.fields['objetivo']
        $('<option value="' + id + '">' + value + '</option>').appendTo(contenido)
    });
    $('#id_objetivo').css('width', '100%');
}