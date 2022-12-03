import GridLayout from "react-grid-layout";
import styled from "styled-components";
import Laptop from "../AuctionImages/laptop.jpg"
import { Responsive, WidthProvider } from "react-grid-layout";
import { useEffect, useState } from "react";
import axios from "axios";

const ResponsiveGridLayout = WidthProvider(Responsive);


const layout = [
  { i: "blue-eyes-dragon", x: 0, y: 0, w: 1, h: 1 },
  { i: "dark-magician", x: 1, y: 0, w: 1, h: 1 },
  { i: "kuriboh", x: 2, y: 0, w: 1, h: 1 },
  { i: "spell-caster", x: 3, y: 0, w: 1, h: 1 },
  { i: "summoned-skull", x: 4, y: 0, w: 1, h: 1 }
];

const GridItemWrapper = styled.div`
  background: Teal;
`;

const GridItemContent = styled.div`
  padding: 8px;
  color:white;
`;

const Root = styled.div`
  padding: 16px;
`;

function Grid ()  {

    useEffect(()=>{
        getAllAuctionData()
    },[])
    
    const [auctions,setAuctions]=useState([])
 
    async function getAllAuctionData(){
        const allAuctions= await axios.get("http://127.0.0.1:8000/apiauction/allauction/")
        console.log(allAuctions.data)
        setAuctions(allAuctions.data)
    }

  return (
    <Root>
        <ResponsiveGridLayout


            layouts={{ lg: layout }}
            breakpoints={{ lg: 1200, md: 996, sm: 768, xs: 480, xxs: 0 }}
            cols={{ lg: 5, md: 4, sm: 3, xs: 2, xxs: 1 }}
            rowHeight={380}
            width={1800}
            >

       
      {/* <GridLayout layout={layout} cols={5} rowHeight={300} width={1500}> */}

        <GridItemWrapper key="blue-eyes-dragon">
          <GridItemContent><h5><strong>LAPTOP</strong></h5>
            <center>
                <div><img src="https://m.media-amazon.com/images/I/41kRKVrKe2L._SY300_SX300_QL70_FMwebp_.jpg"  alt ="" height="150px" width="150px"/></div>
                Name:Lenovo
                <div>Description:Lenovo IdeaPad Intel Core i5 12th Gen 15.6" FHD Thin & Light Laptop </div>
                <div>Manufacture Year:2022</div>
                <div>Base Price:54490</div>
                <div> Owner:Sachin M. </div>
            </center>
          </GridItemContent>
        </GridItemWrapper>

        <GridItemWrapper key="dark-magician">
          <GridItemContent>
          <h5><strong>Freeze</strong></h5>
            <center>
                <div><img src="https://m.media-amazon.com/images/I/41rWJIn5HEL._SX342_SY445_QL70_FMwebp_.jpg"  alt ="" height="160px" width="160px"/></div>
                Name:Godrej
                <div>Description:Godrej 190 L 5 Star Inverter Direct-Cool Single Door Refrigerator</div>
                <div>Manufacture Year:2022</div>
                <div>Base Price: 16990</div>
                <div> Owner:user123 </div>
            </center>
          </GridItemContent>
        </GridItemWrapper>
        <GridItemWrapper key="kuriboh">
          <GridItemContent>Kuriboh</GridItemContent>
        </GridItemWrapper>
        <GridItemWrapper key="spell-caster">
          <GridItemContent>spell-caster </GridItemContent>
        </GridItemWrapper>
        <GridItemWrapper key="summoned-skull">
          <GridItemContent>Summoned Skull</GridItemContent>
        </GridItemWrapper>
        </ResponsiveGridLayout>
      {/* </GridLayout> */}
    </Root>
  );
};
export default Grid;