    google.load('visualization', '1', {'packages':['corechart']});
    google.setOnLoadCallback(drawChart);
    function drawChart() {
        // define a new datatable
        dataset = renderTable(data)
        // define where the graph must be paint
        var chart = new google.visualization.ColumnChart(
            document.getElementById('columnchart_div')
        );
        // effectively draw the graph
        chart.draw(dataset);
    }
