'use strict';

const http = require('http');

const server = http.createServer(function(req, resp) {
    resp.writeHead(200, {'Content-Type': 'text/plain'});
    resp.end('hello');
});

function start(port) {
    server.listen(port, '0.0.0.0');
}

exports.start = start;
