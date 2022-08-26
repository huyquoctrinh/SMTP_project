import React from "react";
import "./contact.css"
import Button from "../Tab-navigation/Button";
import { data } from "./data";
const Contact=()=>{
    return(
        <div className="list_contact g-0">
            {data.map((item,index)=>{
                    return(
                        <Button className="item" key={item.id} src={item.src} src_img={item.img_src}></Button>
                    )
            })}
        </div>
    );
}
export default Contact