const { userModel } = require('../models/userModel');
const passport = require('passport')

exports.register = async (req, res) => {
    const username = req.body.username
    const password = req.body.password

    let newUser = new userModel({
        username: username,
        password: password
    })
    userModel.findOne({username: newUser.username}, async (err, doc) =>{
        if(doc) return res.status(400).send()
        await newUser.save(async (err,user) => {
            if(err) return res.status(500).send()
            req.logIn(err, user => {
                if(err) return res.sendStatus(500)
                req.session.identifier = user.id;
                req.session.username = user.username;
                res.redirect('/home')
            });
        })
    })
}

exports.loginPost = (req, res) => {
    passport.authenticate('local', (err, user, info) => {
        if(err) return res.Status(500).send(err)
        req.logIn(user, err => {
            if(err) return res.Status(500).send(err)
            if(!user){
                return res.send('username or password wrong')
            }
            req.session.identifier = user.id;
            req.session.username = user.username;
            res.redirect('/home')
        });
      })(req, res);
}