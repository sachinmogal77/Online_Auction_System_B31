import React from 'react'
import { NavLink, Route, Routes } from 'react-router-dom'
import About from '../AuctionFolder/About';
import AddAuction from '../AuctionFolder/AddAuction';

import CurrentAuction from '../AuctionFolder/CurrentAuction';
import DetailAuction from '../AuctionFolder/DetailAuction';
import  Grid  from '../AuctionFolder/Grid';
import Home from '../AuctionFolder/Home';
import PreviousAuction from '../AuctionFolder/PreviousAuctions';
import UpcomingAuction from '../AuctionFolder/UpcomingAuction';


 const AppRoutes=()=> {
  return (<>
    <nav class="navbar navbar-expand-lg bg-dark navbar-dark">
  <div class="container-fluid">
    <a class="navbar-brand">Navbar</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
      <div class="navbar-nav">
        <NavLink className="nav-link" to = "/homeauction">HomeAuction</NavLink>
      </div>
    </div>
    <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
      <div class="navbar-nav">
        <NavLink className="nav-link" to = "/addauction">Add Auction</NavLink>
      </div>
    </div>
    <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
      <div class="navbar-nav">
        <NavLink className="nav-link" to = "/detailauction">DetailAuction</NavLink>
      </div>
    </div>
    <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
      <div class="navbar-nav">
        <NavLink className="nav-link" to = "/aboutauction">AboutAuction</NavLink>
      </div>
    </div>   
    <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
      <div class="navbar-nav">
        <NavLink className="nav-link" to = "/grid">Grid</NavLink>
      </div>
    </div>   
    
    
  </div>
</nav>
<Routes>
  <Route path='/homeauction' element={<Home/>}></Route>
  <Route path='/aboutauction' element={<About/>}></Route>
    <Route path="/detailauction" element={<DetailAuction/>}></Route>
    <Route path="/addAuction" element={<AddAuction/>}></Route>
    <Route path="/currentauction" element={<CurrentAuction/>}></Route>
    <Route path="/previousauction" element={<PreviousAuction/>}></Route>
    <Route path="/upcomingauction" element={<UpcomingAuction/>}></Route>
    <Route path="/grid" element={<Grid/>}></Route>
</Routes>

</>
  )
}
export default AppRoutes;