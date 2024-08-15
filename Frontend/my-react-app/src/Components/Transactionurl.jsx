import axios from 'axios'; 
//import React from 'react';


//fetch the data from the newtranaction method, it uses post method 


const TransactionURL= (transaction) => {
   const baseURL = 'http://127.0.0.1:5000/newtransaction';
   
    axios.post(baseURL , transaction)
    .then(response => {
        console.log("The data has been submitted", response.data)
    })
    .catch(error => {
        console.error('Theres been an error: ' , error);
    });
}
export default TransactionURL




