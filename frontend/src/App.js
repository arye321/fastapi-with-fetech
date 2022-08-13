import React, { useState, useRef } from "react";
import './App.css';
import GoogleLoginMain from "./GoogleLoginMain";
import Welcome from "./Welcome";

function App() {
  const [user, setuser] = useState('xd');
  const [loggedin, setLoggedin] = useState(false);
  const [email, setEmail] = useState('xd');


  const submited = async (e) =>{
    e.preventDefault();

    await fetch('/cookie', {
      method: "POST",
            headers: {
            Accept: "application/json, text/plain, */*",
            "Content-Type": "application/json",
            },
            body: JSON.stringify({
            username: "asdf",
            }),
    }).then((res)=>res.json()).then(res=>{
      console.log(res)
      
    })
    
  }
  if (loggedin){
    return (<Welcome name={email}/>)
  }
  else{
    return (
      <div className="App">
        <header className="App-header">
        <div className='formdiv'>
            <form onSubmit={submited}>
              <label htmlFor="fname">First name:</label><br/>
                <input type="text" id="fname" name="fname" defaultValue="John"/><br/>
                  <input type="submit" value="Submit"/>
            </form>
          </div>
        <GoogleLoginMain loggedin={(gmail)=>{
          console.log('logged in')
          setEmail(gmail)
          setLoggedin(true)
          
          }}/>
  
        </header>
      </div>
    );
  }

}

export default App;
