import Auctionhome from "../AuctionImages/Auctionhome.png"
import Apple from "../AuctionImages/Apple.jpeg"
import Images from "../AuctionImages/images.jpeg"
import Laptop from "../AuctionImages/laptop.jpg"
import Sofa from "../AuctionImages/sofa.png"
import Watch from "../AuctionImages/watch.jpeg"
const Home=()=>{
    return(
        <>

                <div>
                <img src={Auctionhome} height="20%" width="100%"/>
                <br></br>
                <center>
                <h1><label>Live Auctions</label></h1>
                </center>
                <hr></hr>
                <center><h5>Hp Laptop</h5></center>
                <center><img src={Laptop} height="20%" width="20%"/>
                <h5>Selling Price:67000</h5></center>
                <hr></hr>
                <center><h5>Branded Sofa</h5></center>
                <center><img src={Sofa} height = "20%" width="20%"/>
                <h5>Selling Price:25000</h5>
                </center>
                <br></br>
                <hr></hr>
                <center>
                    <h1>Upcoming Auctions</h1>
                    <center><img src={Apple} height="20%" width="20%"></img>
                            <img src={Watch} height="20%" width="20%"></img>
                    </center>
                </center>

                </div>
                
        </>
    )
}
export default Home;