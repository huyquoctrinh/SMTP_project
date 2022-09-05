import React from "react";
import "./form.js"
const Form=()=>{
    return(
    <form action="/action_page.php">
        <label for="fname" className="Iname">Your name: </label>
         <input type="text" id="fname" name="fname"></input>
         
            <br></br>
        <label for="lname">Your message: </label>
        <textarea className="mes" placeholder="Message..." rows="5"></textarea>
            <br></br>
        </form>
    );
}
export default Form