//import React from 'react'

// function About() {
//   return (
//     <div>About</div>
//   )
// }

// export default

import * as React from 'react';
import { styled } from '@mui/material/styles';
import Grid from '@mui/material/Grid';
import Paper from '@mui/material/Paper';
import Typography from '@mui/material/Typography';
import ButtonBase from '@mui/material/ButtonBase';
import axios from 'axios';
import { Card,CardContent, CardMedia,Stack } from '@mui/material';


 function ComplexGrid() {

  React.useEffect(()=>{
    getAllAuctionData()
},[])

const [auctions,setAuctions]=React.useState([])

async function getAllAuctionData(){
    const allAuctions= await axios.get("http://127.0.0.1:8000/apiauction/allauction/")
    console.log(allAuctions.data)
    setAuctions(allAuctions.data)

}
  

return(
  <>
        <Typography gutterBottom variant="subtitle1" component="div"/>
          <Stack direaction="row" justifyContent="space-evenly">
            {
               auctions.map(auct=>{
                return(
                  
                  <Card sx={{maxwidth: "200px",mb:2 }}>
                    <CardMedia
                    component="img"
                    height="200px"
                    image={auct.image}
                    alt="green iguana"
                    key = {auct.product}
                    />
                    <CardContent>
                      <Typography variant='h5'>
                        auction_date:{auct.auction_date}
                        <Typography variant='h5'>
                        auction_start_time:{auct.product_name}
                        </Typography>
                        <Typography variant='h5'>
                        auction_end_time:{auct.auction_end_time}
                        </Typography>
                        <Typography variant='h5'>
                        increment_amount:{auct.increment_amount}
                        </Typography>
                        
                        
                        
                       
                      </Typography>
                    </CardContent>
                  </Card>
                )
               })
            }
          </Stack>
          </>)
 }
 export default ComplexGrid;
