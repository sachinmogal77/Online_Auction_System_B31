import React, { useEffect, useState } from 'react'
import axios from 'axios'

function WishListDetails() {
  useEffect(()=>{
    getAllWishlistData()
  },[])

  const [Wishlists, setWishlist]= useState([])

  async function getAllWishlistData(){
    const allWishlists = await axios.get("http://127.0.0.1:8000/buyer/wishlist/")

    console.log(allWishlists.data)
    setWishlist(allWishlists.data)
    
  }
  
    
  return (<>
  <h1 className="text-primary">Wishlist Details!!</h1>

    <table className="table table-dark">
     <thead>
        <tr>
            <th scope="col">#</th>
            <th scope="col">User</th>
            <th scope="col">Apply Auction</th>
            {/* <th scope="col">Action</th> */}
        </tr>
     </thead>
 
      <tbody className="table-info">
        {
            Wishlists.map(wishlist=>{
             return(
                <tr key={Math.random()}>
                    <th scope="row">{wishlist.id}</th>
                    <td>{wishlist.user}</td>    
                    <td>{wishlist.auctions}</td>  
                </tr>
             )
            })
           }
     </tbody>
    </table>
    
  </>)
}

export default WishListDetails;
// .auction_id
// .username