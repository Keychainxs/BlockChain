import axios from 'axios'; // Ensure axios is imported
import { useState, useEffect } from "react";

function BlockChain() {
    const [chain, setChain] = useState([]);

    useEffect(() => {
        axios.get('https://blockchain-a382.onrender.com/getblock')         
        .then(response => {
            setChain(response.data.chain); 
        })
        .catch(error => console.error("Error trying to fetch", error));
    }, []);

    return (
        <div>
            <h1>Block Chain</h1>
            <ul>
                {chain.map((block, index) => ( 
                    <li key={index}> 
                        <h2>Block: {block.index}</h2>
                        <p>Proof: {block.proof}</p>
                        <p>Previous Hash: {block.previous_hash}</p>
                    </li>
                ))}
            </ul>
        </div>
    );
}

export default BlockChain;
