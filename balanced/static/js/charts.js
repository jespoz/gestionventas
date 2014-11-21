$(function () {

    $(document).on('ready', main);

    function main() {
        $('[id^=proyectos]').on('click', 'a', cargar_historia_proyecto);
        $('[id^=tr-obs]').on('click', 'a', function(info){
            id = $(info.currentTarget).data('id');
            var datos = '/balanced/carga_observacion_proyecto/' + id;
            $.getJSON(datos, function (data) {
                $('#modalObs').modal('show');
                var contenido = $('#modal-body-observacion');
                contenido.html('');
                $('<span>' + data.observaciones[0].observacion + '</span>').appendTo(contenido);
                var titulo = $('#modal-title-observacion');
                titulo.html('');
                $('<span><i class="fa fa-eye"></i></span><strong style="font-family: "Open Sans",sans-serif,Helvetica,Arial; margin-left: 20px;" >Realizada por ' + data.observaciones[0].usuario__username + '</strong>').appendTo(titulo)
            });
        });
        $('[id^=tr-obs]').on('click', 'button', function(info){
            id = $(info.currentTarget).data('id');
            $('#id_proyecto').val(id);
            $('#nueva_observacion').val('');
            $('#myModal').modal('show');
            $('#nueva_observacion').focus();
        });
    }

    function cargar_historia_proyecto(info) {
        id = $(info.currentTarget).data('id');
        if ($('#tr' + id).hasClass('hidden')) {
            $('[id^=tr]').addClass('hidden');
            $('[id^=tr-obs]').addClass('hidden');
            var contenido = $('#contenido-proyecto-' + id);
            contenido.html('');
            $('<div style="height: 250px;" id="grafico' + id + '"></div>').appendTo(contenido);
            $('#proyectos').css('left', '-110%');
            contenido.css('left', '0');
            contenido.on('click', 'a', function () {
                contenido.css('left', '-110%');
                $('#proyectos').css('left', '0');
            });
            var observaciones = $('#contenido-observacion-' + id);
            observaciones.html('');
            $('<div style="height: 200px; overflow-y: scroll;" id="obs' + id + '"></div><div id="cont_button' + id + '" style="height: 50px; float:right;"><button data-id="' + id + '" class="btn btn-success" id="add_obs' + id + '" style="margin-top: 10px;"><i class="fa fa-plus"></i> Agregar</button></div>').appendTo(observaciones);
            observaciones.css('left', '0');
            observaciones.on('click', 'a', function () {
                observaciones.css('left', '-110%');
            });
            $('#tr' + id).removeClass('hidden');
            $('#tr-obs' + id).removeClass('hidden');
        } else {
            $('#tr' + id).addClass('hidden');
            $('#tr-obs' + id).addClass('hidden');
        }

        $.get('/balanced/carga_evolucion_proyecto/' + id, cargar_grafico)

    }

    function cargar_grafico(data) {
        chart_answer = new Highcharts.Chart({
            chart: {
                backgroundColor: '#ffffff',
                borderColor: '#a2a2a1',
                borderWidth: 0,
                borderRadius: 0,
                renderTo: 'grafico' + id,
                type: 'area',
                plotBackgroundColor: '#ffffff'
            },
            colors: ['#3399FF'],
            legend: {
                enabled: true
            },
            title: {
                text: '% Avances por ciclos'
            },
            tooltip: {
                borderRadius: 0,
                borderWidth: 0,
                shadow: false,
                style: {
                    fontSize: '7pt',
                    color: '#000000'
                },
                pointFormat: '{point.y:.2f} %'
            },
            plotOptions: {
                series: {
                    fillOpacity: 0.1
                }
            },
            xAxis: {
                labels: {
                    x: 0,
                    y: 40,
                    style: {
                        color: '#333333'
                    }
                },
                lineWidth: 1,
                lineColor: '#333333',
                minPadding: 0,
                maxPadding: 0,
                title: {
                    text: ''
                }
            },
            yAxis: {
                gridLineWidth: 0,
                lineWidth: 1,
                lineColor: '#333333',
                min: 0,
                minPadding: 0,
                maxPadding: 0,
                title: {
                    text: ''
                }
            }
        });

        var datosApi = '/balanced/carga_evolucion_proyecto/' + id;

        $.getJSON(datosApi, function (data) {
            var arr = [];
            var ciclos = [];
            var acum = [];
            $.each(data.avances, function (key, val) {
                arr.push(val.fields['avance']);
            });
            $.each(data.acumulado, function (key, val) {
                acum.push(val.promedio);
                ciclos.push('Ciclo ' + val.ciclo__clave);
            });
            chart_answer.xAxis[0].setCategories(ciclos);
            var series = {data: acum, name: 'Avance Global', color: '#A94442'};
            chart_answer.addSeries(series);
            series = {data: arr, name: 'Avance Proyecto'};
            chart_answer.addSeries(series);
            var obs_div = $('#obs' + id);
            obs_div.html('');
            $.each(data.observaciones, function (key, val) {
                if (val.fields['observacion'] != null) {
                    $('<div class="note note-success"><a data-id="' + val.pk + '" style="font-family: Open Sans; font-size: 12px; margin-bottom:0; cursor: pointer;">' + val.fields['observacion'].substr(0, 80) + '... </a>').appendTo(obs_div)
                }
            });
            var new_obs = $('#row' + id);
            new_obs.html('');

        });

    }
});
