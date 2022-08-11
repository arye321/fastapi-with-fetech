import React, { useState, useRef } from "react";
import './App.css';
import GoogleLoginMain from "./GoogleLoginMain";

function App() {
  const [user, setuser] = useState('xd');


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
      <GoogleLoginMain />

      </header>
    </div>
  );
}

export default App;