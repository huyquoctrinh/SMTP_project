import React from "react";
import "./Avar.css"
import AK from "./khoa.jpg"
const Avar=()=>{
    return(
        <div>
            <div>
                <img src={AK} alt="Ảnh cá nhân" className="avar">
                </img>
            </div>
            <div className="Card">
                <span className="welcome">
                    Hello, my name is...
                </span>
                <br></br>
                <span className="name">
                    Nguyễn Anh Khoa
                </span>
            </div>
        </div>
    )
}
export default Avar