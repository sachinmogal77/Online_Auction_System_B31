import { NavLink, Route, Routes } from 'react-router-dom'
import {LogOut, AuthContext} from './Logout';
import Home from './Home';
import Product from './Product';
import Register from './Register';
import { useContext } from 'react';
import { ChangePassword } from './Chnagepassword';
import { ForgotPassword } from './Forgotpassword';
//import logoutUser from './Logout'

const AppRoutes=()=>{

    //const { user, logoutUser } = useContext(AuthContext);

    return (
        <>
        <nav className="navbar navbar-expand-lg navbar-dark bg-info bg-container">
            <div className="container-fluid">
            <div>
          
            <NavLink className="navbar-brand" to="/home"><b>HOME</b></NavLink>
            <NavLink className="navbar-brand" to="/products"><b>PRODUCTS</b></NavLink>
            <NavLink className="navbar-brand" to="/register"><b>REGISTER</b></NavLink>
            <button onClick={LogOut}>LOGOUT</button>
            
            </div>
            </div>
            </nav>

            <Routes>
                <Route path='/home' element={<Home/>}></Route>
                <Route path='/products' element={<Product/>}></Route>
                <Route path='/register' element={<Register/>}></Route>
                <Route path='/changepassword' element={<ChangePassword/>}></Route>
                <Route path='/forgotpassword' element={<ForgotPassword/>}></Route>
            </Routes>
        </>
    )

}

export default AppRoutes;