var express = require('express');
var app = express();

// Middleware для парсинга JSON тел запросов
app.use(express.json());

app.use(function (req, res, next) {
    console.log('Time:', req.method, req.path);
    console.log('Json:', req.body);
    next();
});

app.get('/', function(req, res) {
    res.send('Hello World!');
});

app.post('/data', function(req, res) {
    res.send('Received data: ' + JSON.stringify(req.body));
});

app.listen(3000, function() {
    console.log('Example app listening on port 3000!');
});
