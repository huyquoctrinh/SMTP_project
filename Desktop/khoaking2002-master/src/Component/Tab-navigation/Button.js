import React from "react";
const Button=(props)=>{
    return(
        <a href={props.src}>
         <img style={{height:"2rem"}} alt={props.alt} src={props.src_img}></img>
      </a>
    );
}
export default Button