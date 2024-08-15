import "react";
 import blockchainimagegif from './images/blockchainimage.gif'

const Home = () => {
    return(
        <div className="home-container">
        <h1 className="title">Blockchain</h1>
        <p className="pronunciation">[bläk-chān]</p>
        <p className="definition">A digital database or ledger that is distributed among the nodes of a peer-to-peer network.</p>
        <div className="image-container">
            <img src={blockchainimagegif} alt="Block chain visual" className="blockchain-gif"/>
        </div>
    </div>
    );
}

export default Home



