const express = require('express');
const cors = require('cors');
const app = express();
const PORT = process.env.PORT||3000;
app.use(cors());
app.get('/random',(req,res)=>{
    const min = parseInt(req.query.min)|| 100;
    const max = parseInt(req.query.max)|| 1000;
    const creditScore = Math.floor(Math.random()*(max-min+1))+min;
    res.json({creditScore: creditScore});
});
app.listen(PORT,()=>{
    console.log(`Server is running on http://localhost:${PORT}`);
});