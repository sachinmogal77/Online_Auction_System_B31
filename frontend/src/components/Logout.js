import { useNavigate } from "react-router-dom";
import jwt_decode from 'jwt-decode';
import { createContext,useState, useEffect } from "react";

export const AuthContext = createContext();


export const LogOut = ({ children })=>{
    const navi =useNavigate()
    //const [setIsLoggedin] = useState(false);
    const [loading, setLoading] = useState(true);

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

    const logoutUser = (props) => {
        setAuthTokens(null);
        setUser(null);
        localStorage.removeItem("authTokens");
        navi("/home");
    };

    const contextData = {
      user,logoutUser}

    useEffect(() => {
      if (authTokens) {
        setUser(jwt_decode(authTokens.access));
      }
      setLoading(false);
    }, [authTokens, loading]);

    return(<>
     <AuthContext.Provider value={contextData}>
     {loading ? null : children}
    </AuthContext.Provider> 
      </>)
}