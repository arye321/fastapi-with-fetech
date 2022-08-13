import './Welcome.css';
import React, { useState, useEffect } from 'react';
import Test from './Test';


export default function Welcome(props){
  const [loggedin, setLoggedin] = useState(true);

    // console.log("welcome")
    const clicked = () =>{
        fetch('/logout',{ method: "GET"}).then((res)=>res.json())
        .then(res=>{
            // console.log(res)
            setLoggedin(false)

        }).catch((e)=>{console.log(e)})
    
    }
    if (loggedin){
    return(
    <div className="welcomeDiv">
        <h2>Welcome to zombocom {props.name}</h2>
        <input type="button" value="Logout" onClick={clicked} />
    </div>)

    }
    else{
        return (<Test />)
    }
}