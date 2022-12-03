// import axios from 'axios'
// import React, { useEffect, useState } from 'react'

import axios from 'axios'
import React, { useEffect, useState } from 'react'
import { NavLink } from 'react-router-dom'




function CurrentAuction() {
    useEffect(()=>{
        getCurrentauctionData()
    },[])
    
    const [auctions,setAuctions]=useState([])
 
    async function getCurrentauctionData(){
        const allcurrentAuctions= await axios.get("http://127.0.0.1:8000/apiauction/cauction/")
        console.log(allcurrentAuctions.data)
        setAuctions(allcurrentAuctions.data)

    }
  return (
    <>
    {/* <center><h1 className='text-warning'><marquee>These are the current auctions</marquee></h1></center> */}
    <center><h1 className='text-primary'><marquee> <strong>CURRENT AUCTIONS</strong></marquee></h1></center>
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

</>
  )
  
}
export default CurrentAuction;





// function CurrentAuction() {

//   useEffect(()=>{
//     getCurrentAuction()
//   },[])
//   const[current,setcurrent]=useState({})
 
//   async function getCurrentAuction(currObj){
//     console.log(currObj)
//     const allcurrentData = await axios.get("http://127.0.0.1:8000/apiauction/cauction/")
//     console.log(allcurrentData.data)
//     setcurrent(allcurrentData.data)
//   }
//   return (
//     <>
//     </>
//   )
// }

// export default CurrentAuction