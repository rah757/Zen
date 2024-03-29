var chrt = document.getElementById("chartId").getContext("2d");

var sleepDetails = {
   labels: ["Day 1", "Day 2", "Day 3", "Day 4", "Day 5", "Day 6", "Day 7"],
      datasets: [{
         label: "Hours of sleep",
         base: 0,
         data: [0],
         backgroundColor: [
            'rgba(255, 99, 132, 0.2)',
            'rgba(255, 159, 64, 0.2)',
            'rgba(255, 205, 86, 0.2)',
            'rgba(75, 192, 192, 0.2)',
            'rgba(54, 162, 235, 0.2)',
            'rgba(153, 102, 255, 0.2)',
            'rgba(155, 203, 245, 0.2)'
         ],
         borderColor: [
            'rgb(255, 99, 132)',
            'rgb(255, 159, 64)',
            'rgb(255, 205, 86)',
            'rgb(75, 192, 192)',
            'rgb(54, 162, 235)',
            'rgb(153, 102, 255)',
            'rgb(155, 203, 245)'
         ],
         borderWidth: 1.3,
         pointRadius: 2.69,
      }],
}

sleeplen = sleep.length;
let q = 0;

for (let p = Math.min(6,sleeplen-1); p >= 0; p--, q++) {
   sleepDetails.datasets[0].data[q] = sleep[p];
//   sleepDetails["datasets"]["data"][q] = sleep[p];
}

var sleepChartConfig = {
   type: 'line',
   data: sleepDetails,
   options: {
      responsive: false,
      scales: {
         y: {
           beginAtZero: true
         }
       },
   },
}

var chartId = new Chart(chrt, sleepChartConfig);
