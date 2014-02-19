'use strict';

const NewspaperSite = require('./lib/NewspaperSite');

const port = parseInt(process.argv[2], 10) || 5000;
NewspaperSite.start(port);
console.log('Listening to http://localhost:'+port);

