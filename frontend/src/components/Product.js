import { NavLink, Route, Routes } from "react-router-dom";
import { ChangePassword } from './Chnagepassword';

const Product=()=>{
    return(<>
            <h1>Product Page</h1>
            <form>
            <div>
                
                <NavLink to="/changepassword">Chanage Password?</NavLink>
                <Routes><Route path='/changepassword' element={<ChangePassword/>}></Route></Routes>
                
                </div>
            </form>
    </>)
}

export default Product;