// Initialize express
const express = require('express')
const app = express()
// require handlebars
const exphbs = require('express-handlebars');
const Handlebars = require('handlebars')
const {allowInsecurePrototypeAccess} = require('@handlebars/allow-prototype-access')
const bodyParser = require('body-parser');
const models = require('./db/models');

// Use "main" as our default layout
app.engine('handlebars', exphbs({ defaultLayout: 'main', handlebars: allowInsecurePrototypeAccess(Handlebars) }));
// Use handlebars to render
app.set('view engine', 'handlebars');
app.use(bodyParser.urlencoded({ extended: true }));


// Render the "home" layout for the main page and send the following msg
app.get('/', (req, res) => {
  res.render('home', { msg: 'Handlebars are Cool!' });
})

// INDEX
app.get('/new', (req, res) => {
  res.render('inventory-new', {});
})

app.get('/sign-up', function (req, res) {
  res.render('sign-up', {});
})

app.get('/log-in', function (req, res) {
  res.render('log-in', {});
})

app.post('/inventory', function (req, res) {
  res.send('POST request to the homepage')
})


app.get('/game.py', function (req, res) {
  res.render('game-new', {});
})

app.get('/game', function (req, res) {
  res.render('game-new', {});
})


// Choose a port to listen on
const port = process.env.PORT || 3000;

// Tell the app what port to listen on
app.listen(port, () => {
  console.log('App listening on port 3000!')
})
