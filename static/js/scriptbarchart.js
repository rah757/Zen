//Bar chart js
// setup data
const labels = ['Day 1', 'Day 2', 'Day 3', 'Day 4', 'Day 5', 'Day 6', 'Day 7']
const data = {
    labels: labels,
    datasets: [{
        label: 'Your average health score',
        borderRadius: 15,
        base: 0,
        hoverBorderRadius: 17,
        data: [0, 0, 0, 0, 0, 0, 0],
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
        borderWidth: 1
    }]
};

let len = entries.length;
let numElements = Math.min(7,len);
let j = 0;

for (let i = len-numElements; i < len; i++, j++) {
    data["datasets"][0]["data"][j] = entries[i];
}

//configuration here    
const config = {
    type: 'bar',
    data,
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
};

// rendering stuff
const myChart = new Chart(
    document.getElementById('myChart'),
    config
);
