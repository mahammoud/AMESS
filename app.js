const express = require('express')
const session = require('express-session')
const mongoose = require('mongoose');
const MongoStore = require('connect-mongo');
const passport = require('passport')
const bodyParser = require('body-parser');
const userController = require('./controllers/userController')

const app = express()

app.use(session({
  secret: 'hdjahnjd0949jijkldjkj2kFSFE#DIKEW)(0do3Di093dijqwie-03o012elpsl;x.mds,mfneoire3DEDw3',
  resave: true,
  saveUninitialized: true,
  store: MongoStore.create({
    mongoUrl: 'mongodb+srv://Mohammoud:cRe_diFoN22@amess.rxxgx.mongodb.net/?retryWrites=true&w=majority',
    autoRemove: 'disabled'
  }),
  cookie: ({
    maxAge: 100*60*60*10000
  })
}))
app.use(passport.initialize());
app.use(bodyParser.urlencoded({ extended: false }))
app.use(bodyParser.json())
app.use(passport.session());
app.use((req, res, next) => {
  res.locals.user = req.user;
  next();
});

mongoose.connect('mongodb+srv://Mohammoud:cRe_diFoN22@amess.rxxgx.mongodb.net/?retryWrites=true&w=majority', {
  useNewUrlParser: true, useUnifiedTopology: true 
})
app.post('/signup',userController.register)
app.post('/login',userController.loginPost)
app.get('/logout', async (req,res) =>{
  if(!req.session.identifier) {
    res.render('loginfirst')
  }
  else {
    req.session.destroy();
    res.redirect('/')
  }
})
const io = require('socket.io')(server)
io.on('connection', async (socket) =>{
  
})
app.listen(8080, ()=>{
    console.log('app listening on port 8080')
})