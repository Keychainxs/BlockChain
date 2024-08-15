import axios from 'axios'
import {useState} from 'react'

import'react'


const MineBlock = () => {
    const [minedBlock, setMinedBlock] = useState('null')
    const [error, setError] = useState('')
    
    const handleMineBlock = () => {
    axios.get('http://127.0.0.1:5000/mineblock')
            .then(response => {
                setMinedBlock(response.data)
                setError('')
            })
            .catch(error => console.error("erro fetching block", error))
            setError("erro mining new block" );
            setMinedBlock(null)
    }

    return(<div>
        <h1>Mine a New Block </h1>
        <button onClick={handleMineBlock}>MineBlock</button>
        {minedBlock && (
        <div>
          <h3>Block Mined Successfully</h3>
          <p><strong>Index:</strong> {minedBlock.index}</p>
          <p><strong>Timestamp:</strong> {new Date(minedBlock.timestamp * 1000).toLocaleString()}</p>
          <p><strong>Proof:</strong> {minedBlock.proof}</p>
          <p><strong>Previous Hash:</strong> {minedBlock.previous_hash}</p>
        </div>
      )}
      {error && <p style={{ color: 'red' }}>{error}</p>}
      <p>Mining is the process of validating new transactions and recording them on the blockchain. When you mine a block, you simulate the action of verifying all pending transactions and securing them in the blockchain. Miners are rewarded for this work with cryptocurrency, incentivizing network support and security.</p>

    </div>)

}
export default MineBlock


