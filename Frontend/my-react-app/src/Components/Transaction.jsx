import {useState} from 'react'; 
import TransactionURL from './Transactionurl';



const SubmitTransaction = () => {

    const[transaction, setTransaction] = useState({'sender': ' ',  'recipient': '', 'amount': 0})

    const handleSumbit = (e) => {
        e.preventdefault();

        TransactionURL(transaction)
    }

    return(
            <div className='Form'> 
                <form action={handleSumbit}>

                    <input type='text' value={transaction.sender} onChange={(e) => setTransaction({...transaction, sender : e.target.value})} placeholder='Sender'/>
                    <input type='text' value={transaction.recipient} onChange={(e) => setTransaction({...transaction, recipient : e.target.value})} placeholder='Recipient'/>
                    <input type='amount' value={transaction.amount} onChange={(e) => setTransaction({...transaction, amount : e.target.value})} placeholder='Amount'/>

                    <button type ="submit">Submit</button>
                    <p>Transactions are the heart of the blockchain. They represent the transfer of value or information from one party to another. Use this form to simulate sending a cryptocurrency transaction. Specify a sender, a recipient, and an amount to see how transactions are added to the blockchain pending the next block mining.</p>

                </form>
            </div>
        )
}

export default SubmitTransaction













