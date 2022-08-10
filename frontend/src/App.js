import React, { useState, useRef } from "react";
import './App.css';

function App() {
  const [user, setuser] = useState('xd');
  const [count, setCount] = useState(1);

  const submited = async (e) =>{
    e.preventDefault();
    setCount(count+1)
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
        
      <h1>1count: {count}</h1>

      <div className='formdiv'>
          <form onSubmit={submited}>
            <label htmlFor="fname">First name:</label><br/>
              <input type="text" id="fname" name="fname" defaultValue="John"/><br/>
                <input type="submit" value="Submit"/>
          </form>
        </div>
      </header>
    </div>
  );
}

export default App;
