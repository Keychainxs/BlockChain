import 'react';
import { BrowserRouter as Router, Link, Route,Routes } from 'react-router-dom';
import MineBlock from './Components/Mineblock';
import SubmitTransaction from './Components/Transaction';
import BlockChain from './Components/BlockChain';
import Home from './Components/Home';

import './App.css';
import './Home.css'


function App() {
 
    
    
   return  (
    <Router>
      <div>
        <nav className="navbar">
          <Link to="/">Home</Link>
          <Link to="/submit-transaction">Submit Transaction</Link>
          <Link to="/blockchain-data">Blockchain Data</Link>
          <Link to="/mine-block">Mine a Block</Link>
        </nav>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/submit-transaction" element={<SubmitTransaction />} />
          <Route path="/blockchain-data" element={<BlockChain />} />
          <Route path="/mine-block" element={<MineBlock />} />
        </Routes>
      </div>
    </Router>
  );
  
}

export default App;

