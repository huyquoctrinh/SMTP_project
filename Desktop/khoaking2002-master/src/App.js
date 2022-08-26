import React from 'react';
import './App.css';
import Avar from './Component/Avatar/Avar';
import Tab from './Component/Tab-navigation/tab-navigation';
import Home from './Home/HomePage';
import Achie from './Component/Achie/Achie';
import { lst } from './Component/Achie/info';
function App() {
  return (
    <div className="mainPage">
    <div className="Home">
        <Avar className="Av"></Avar>
        <Tab className="Av"></Tab>
    </div>
    <div className="list_Achie">
        {lst.map((item,index)=>{
            return(
                <Achie key={item.id} caption={item.caption} smr={item.summary} link={item.link} src1={item.src} ></Achie>
            )
        })}
    </div>
</div>
  );
}

export default App;
