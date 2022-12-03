import axios from 'axios'
import React, { useEffect, useState } from 'react'
import { NavLink } from 'react-router-dom'




function UpcomingAuction() {
    useEffect(()=>{
        getAllAuctionData()
    },[])
    
    const [auctions,setAuctions]=useState([])
 
    async function getAllAuctionData(){
        const allAuctions= await axios.get("http://127.0.0.1:8000/apiauction/uauction/")
        console.log(allAuctions.data)
        setAuctions(allAuctions.data)

    }
  return (
    <>
    <center><h1 className='text-primary'><marquee> <strong>UPCOMING AUCTIONS</strong></marquee></h1></center>
    <table class="table">
  <thead>
    <tr>
      <th scope="col">ID</th>
      <th scope="col">PRODUCT</th>
      <th scope="col">AUCTION_ID</th>
      <th scope="col">AUCTION_DATE</th>
      <th scope="col">AUCTION START TIME</th>
      <th scope="col">AUCTION END TIME</th>
      <th scope="col">INCREMENT AMOUNT</th>
    </tr>
  </thead>
  <tbody>
    {
      auctions.map(auct=>{
        return(

          <tr key={auct.product}>
          <th scope="row">{auct.product}</th>
          <td>{auct.product}</td>
          <td>{auct.auction_id}</td>
          <td>{auct.auction_date}</td>
          <td>{auct.auction_start_time}</td>
          <td>{auct.auction_end_time}</td>
          <td>{auct.increment_amount}</td>
          {/* <td>
                <NavLink to={`/addAuction/${auct.product}`}>
                <button type="button" class="btn btn-success">ADD AUCTION</button>
                </NavLink>
          </td> */}
        </tr>
        
        )
      })
    } 
   
  </tbody>
</table>
{/* <div class="d-grid gap-2 col-6 mx-auto">
  <button class="btn btn-warning" type="button">SEE UPCOMING AUCTION</button>
  <NavLink to="/previousauction">
  <button class="btn btn-primary" type="button">SEE PREVIOUS AUCTION</button>
  </NavLink>

  <NavLink to ="/currentauction">
  <button class="btn btn-info" type="button">SEE CURRENT AUCTION</button>
  </NavLink>
</div> */}
</>
  )
  
}
export default UpcomingAuction;
