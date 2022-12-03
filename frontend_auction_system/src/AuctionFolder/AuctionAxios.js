import axios from 'axios'
import React from 'react'

function AuctionAxios() {
    const AllData=axios.get("http://127.0.0.1:8000/apiauction/auction/")
    console.log(AllData)
  return (
    <div>AuctionAxios</div>
  )
}

export default AuctionAxios