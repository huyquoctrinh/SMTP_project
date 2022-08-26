import React from "react";
import Contact from "../Contact/contact";
import "./tabStyle.css";
import Form from "../form/form";
const Tab=()=>{
    return(
        <div>
        <div className="intro_text">
            <span className="intro">
            I am a student of hornor program at University of Science, HCMC. I have a spirit of inquiry in many fields. Specially, I interested in technology and economic. My strongs point are opportunistic, team-working, creativity and persevere.
            </span>
            <br></br>
            <span className="Chamngon">
             "when you want something, all the universe conspires in helping you to achieve it - Paulo Coelho"
            </span>
        </div>
        <div className="listButton">
            <a href="https://drive.google.com/file/d/1aB6IkDt0OXKoXPAI7VUKqJzyZ1vyEnjL/view?usp=sharing">
            <button className="button">
                See My CV
            </button>
            </a>
            <a href="https://forms.gle/VGehiWBPgWojrracA">
            <button className="button">
                Message for me
            </button>
            </a>
        </div>
        <Contact></Contact>
        </div>
    );
}
export default Tab;