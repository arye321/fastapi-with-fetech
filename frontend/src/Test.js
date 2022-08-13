import React, { useState, useEffect } from 'react';
import App from './App';
import Welcome from './Welcome';

export default function Test(){
  const [loggedin, setLoggedin] = useState(false);
  const [email, setEmail] = useState("");
  const [loading, setLoading] = useState(true);


    useEffect(() => {
        // console.log('loaded')
        const check_login =  (e) =>{
             fetch('/showcase',{ method: "GET"})
        .then((res)=>res.json()).then(res=>{
          // console.log('res=',res)
          if (res.includes('gmail')){
            // console.log('lol',res)
            setEmail(res)
            setLoggedin(true)
          }
          else{
            setLoading(false)
          }
        }).catch((erorr)=>{
            setLoading(false)

        })
        }
        check_login()
      }, []); // Only re-run the effect if count changes
    if (loggedin){
        return(<Welcome name={email}></Welcome>)
    }
    if(loading){
        return(<>Loading</>)
    }
    return(
        <div className="Test">
            <App />
        </div>

    )
}
