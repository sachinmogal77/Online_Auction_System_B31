import {NavLink, Route, Routes } from "react-router-dom"
import Feedback from "./feedback"
import { Grid } from "./grid"

const AppRoute=()=>{
    return (<>


<nav className="navbar navbar-expand-lg bg-dark navbar-dark">
        <div className="container-fliuid">
            <div className="collapse navbar-collapse" id="navbarNav">
                <ul className="navbar-nav">
                    
                    <li className="nav-item">
                        <NavLink className="nav-link" to="/feedback">Feedback</NavLink>
                    </li>
                    <li className="nav-item">
                        <NavLink className="nav-link" to="/layout">Grid</NavLink>
                    </li>
                    
                </ul>

            </div>
        </div>

    </nav>

<Routes>
        <Route path="/feedback" element={<Feedback/>}></Route>
        <Route path="/layout" element={<Grid/>}></Route>
</Routes>

</>)

}

export default AppRoute