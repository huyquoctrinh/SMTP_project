import React from "react";
import Achie from "../Component/Achie/Achie";
import Avar from "../Component/Avatar/Avar";
import Button_Card from "../Component/Button_Contact";
import Tab from "../Component/Tab-navigation/tab-navigation";
import "./Home.css"
import { lst } from "../Component/Achie/info";
const Home=()=>{
    return(
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
    )
}
export default Home