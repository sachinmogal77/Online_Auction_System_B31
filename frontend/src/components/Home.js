import { NavLink,useNavigate, Route, Routes } from "react-router-dom";
import { useState } from "react";
import jwt_decode from "jwt-decode"
import { ForgotPassword } from "./Forgotpassword";

const Home=()=>{
    const navi=useNavigate()
    const [authTokens, setAuthTokens] = useState(() =>
    localStorage.getItem("authTokens")
      ? JSON.parse(localStorage.getItem("authTokens"))
      : null
  );
  const [user, setUser] = useState(() =>
    localStorage.getItem("authTokens")
      ? jwt_decode(localStorage.getItem("authTokens"))
      : null
  );

    const loginUser = async (username, password) => {

        const response = await fetch("http://127.0.0.1:8000/uapi/access_token/", 
        
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json"
          },
          body: JSON.stringify({
            username,
            password
          })
          
          
        });
        console.log(response)
        const data = await response.json();

        if (response.status === 200) {
          setAuthTokens(data);
          setUser(jwt_decode(data.access));
          localStorage.setItem("authTokens", JSON.stringify(data));
          navi('/products')
        } else {
          alert("Something went wrong!");
        }
      };
      const handleSubmit = e => {
        e.preventDefault();
        const username = e.target.username.value;
        const password = e.target.password.value;
        username.length > 0 && loginUser(username, password);
      };

    return(<>
    <section>
      <div className="col-md-14">
      <form onSubmit={handleSubmit}>
      <center><h1>Login </h1></center>
        <hr />
        <center>
          <div  className="form-group col-md-4">
        <input type="text" id="username" className="form-control" placeholder="Enter Username" />
        </div>
        <br></br><br></br>
        <div  className="form-group col-md-4">
        <input type="password" id="password" className="form-control" placeholder="Enter Password" />
        </div>
        <br></br><br></br>
        </center>
        <center><button type="submit" class="btn btn-outline-primary bth-lg col-2">Login</button></center><br></br>
        <div>
        <center>
        <NavLink to="/forgotpassword">Forgot Password?</NavLink>
        <Routes>
        <Route path='/forgotpassword' element={<ForgotPassword/>}></Route>
        </Routes>
        </center>
        </div>
      </form>
      </div>
    </section>
    </>)
}

export default Home;