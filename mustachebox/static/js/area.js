    google.load('visualization', '1', {'packages':['corechart']});
    google.setOnLoadCallback(drawChart);
    function drawChart() {
        dataset = new google.visualization.DataTable();
        i = 0;
        indexes = []
        for(var index in data) {
            indexes.push(index);
            i++;
        };
        indexes.reverse();
        for(var i=0;i<indexes.length;i++) {
            dataset.addColumn('number', indexes[i]);
        }
        rows = [];
        for(var j=0;j<i+1;j++){
            row = [];
            for(var index in data){
                row.push(data[index][j]);
            }
            rows.push(row.reverse());
        }
        dataset.addRows(rows)
        var chart = new google.visualization.AreaChart(
            document.getElementById('chart_div'));
        chart.draw(dataset);


    }


