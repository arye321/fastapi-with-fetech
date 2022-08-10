import { GoogleOAuthProvider } from "@react-oauth/google";
import { GoogleLogin } from "@react-oauth/google";
import jwt_deocde from "jwt-decode";

export default function GoogleLoginMain(){
  const successLogin = async (creds) =>{
  
        console.log("creds =",creds);
        let userCred = creds.credential;
        let payload = jwt_deocde(userCred);
        console.log("payload=",payload);
        await fetch('/singin', {
                method: "POST",
                headers:{
                  'Content-Type':'application/json',
              },
                body: JSON.stringify({
                email: payload.email ,
                }),
        }).then((res)=>res.json()).then(res=>{
          console.log(res)
        })
    }
    return (
        <div className="GoogleLogin">
          <GoogleOAuthProvider clientId="850364421534-9f2re6djtki6sm8dh02ml8j0dg11fvih.apps.googleusercontent.com">
            
            <GoogleLogin
              text="signin_with"
              theme="filled_blue"
              size="large"
              ux_mode="popup"
              onSuccess={successLogin}
              onError={() => {
                console.log("Login Failed");
              }}
            />
            
          </GoogleOAuthProvider>
        </div>
      );
}