// express 모듈 가져옴.
const express = require('express')
// 미들웨어 선언
const app = express()

//크로스도메인 이슈 해결
//const cors = require('cors');

//Python 파일 경로
const path = require('path')
const pyPath = path.join(__dirname, 'faucet_info.py')

const port = 6060;
app.listen(port, function () {
    console.log(pyPath)
})

app.get('/metrics', function (req, res) {
    try{
        const spawn = require("child_process").spawn
        const process = spawn('python3',[pyPath] )
        process.stdout.on('data', function(data) {
            console.log(data.toString());
            res.send(data.toString())
            res.end()
            return
        })
        // process.stdout.pipe(res)
    } catch(error) {
        console.error(error)
        res.status(500).send({error: error.message})
        res.end()
        return
    }
})
