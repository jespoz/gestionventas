$(function() {
    //Array para dar formato en español
    $.datepicker.regional['es'] =
    {
    closeText: 'Cerrar',
    prevText: 'Previo',
    nextText: 'Próximo',

    monthNames: ['Enero','Febrero','Marzo','Abril','Mayo','Junio',
    'Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre'],
    monthNamesShort: ['Ene','Feb','Mar','Abr','May','Jun',
    'Jul','Ago','Sep','Oct','Nov','Dic'],
    monthStatus: 'Ver otro mes', yearStatus: 'Ver otro año',
    dayNames: ['Domingo','Lunes','Martes','Miércoles','Jueves','Viernes','Sábado'],
    dayNamesShort: ['Dom','Lun','Mar','Mie','Jue','Vie','Sáb'],
    dayNamesMin: ['Do','Lu','Ma','Mi','Ju','Vi','Sa'],
    dateFormat: 'dd/mm/yy', firstDay: 1,
    initStatus: 'Selecciona la fecha', isRTL: false};
    $.datepicker.setDefaults($.datepicker.regional['es']);
});
