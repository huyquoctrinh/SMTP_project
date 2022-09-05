import React from "react";
import "./style.css"
import AK from "../Avatar/khoa.jpg"
const Achie=(props)=>{
    return(
        <div className="Achi_card">
			<div className="Achi_image">
                <img className="main_image" src={props.src1} alt={props.alt1}></img>
			</div>
			<div className="Achie_Sub">
                <div className="Achie_text">
                    <h1 className="caption">{props.caption}</h1>
                </div>
			</div>
            <div className="main_text">
                <span className="summary">{props.smr}</span>
                <br></br>
                <a href={props.link}>
                <button className="link">
                    Go to project
                </button>
                </a>
            </div>
        </div>
    )
}
export default Achie