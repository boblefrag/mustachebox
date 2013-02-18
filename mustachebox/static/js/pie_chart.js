    google.load('visualization', '1', {'packages':['corechart']});
    google.setOnLoadCallback(drawChart);
    function drawChart() {
        // define a new datatable
        dataset = new google.visualization.DataTable();
        for(var i=0; i< piedata.label.length; i++){
            if(i == 0){
                // first column is a string type
                dataset.addColumn('string', piedata.label[i]);
            }else{
            dataset.addColumn('number', piedata.label[i]);}
        }
        rows = []
        for(var i=0; i<piedata.activities.length; i++){
            rows.push(piedata.activities[i])

        }
        // add every rows to the dataset
        dataset.addRows(rows)
        // define where the graph must be paint
        var chart = new google.visualization.PieChart(
             document.getElementById('piechart_div')
        );
         // effectively draw the graph
        chart.draw(dataset);
    }
