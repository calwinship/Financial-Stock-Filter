document.getElementById('ticker-form').addEventListener('submit', function(event) {
    event.preventDefault();
    
    let tickers = document.getElementById('tickers').value.split(',');

    fetch('/filter_companies', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({tickers: tickers})
    })
    .then(response => response.json())
    .then(data => {
        let resultsDiv = document.getElementById('results');
        resultsDiv.innerHTML = '';
        data.forEach(ticker => {
            let p = document.createElement('p');
            p.textContent = ticker;
            resultsDiv.appendChild(p);
        });
    });
});
