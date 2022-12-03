import axios from 'axios'
import { useNavigate, useParams } from 'react-router-dom'
import React from 'react'
import { useForm } from 'react-hook-form'

function AddAuction() {

                 const {register,handleSubmit}=useForm()

                    const navi = useNavigate()

                 function getRegisterAuction(auctObj){
                  console.log(auctObj)
                  axios.post("http://127.0.0.1:8000/apiauction/auction/",auctObj)
                  console.log(auctObj)
                  navi('/detailauction')
                }
  return (
    <>
        
          <div className='row'>
            <div className='col-md-6'>
              <center>
              <center><h1><marquee className='text-info'>ADD AUCTION HERE</marquee></h1></center>
        
              <form onSubmit={handleSubmit(getRegisterAuction)}>
              <div className="mb-4">
              <label for="formGroupExampleInput2" className="form-label text-danger"><strong>PRODUCT ID</strong></label>
              <input type="text" className="form-control"  placeholder="product_id" {...register("product")}/>
            </div>
            <div className="mb-4">
            <label for="formGroupExampleInput2" className="form-label text-danger"><strong>AUCTION ID</strong></label>
              <input type="text" className="form-control"  placeholder="auction_id"{...register("auction_id")}/>
            </div>
            <div className="mb-4">
            <label for="formGroupExampleInput2" className="form-label text-danger"><strong>AUCTION DATE</strong></label>
              <input type="date" className="form-control"  placeholder="auction_date" {...register("auction_date")}/>
            </div>
            <div className="mb-4">
            <label for="formGroupExampleInput" className="form-label text-danger"><strong>AUCTION START TIME</strong></label>
              <input type="time" className="form-control"  placeholder="auction_start_time" {...register("auction_start_time")}/>
            </div>
            <div className="mb-4">
            <label for="formGroupExampleInput2" className="form-label text-danger"><strong>AUCTION END TIME</strong></label>
              <input type="time" className="form-control"  placeholder="auction_end_time" {...register("auction_end_time")}/>
            </div>
            <div className="mb-4">
            <label for="formGroupExampleInput2" className="form-label text-danger"><strong>INCREMENT AMOUNT</strong></label>
              <input type="text" className="form-control"  placeholder="increment_amount" {...register("increment_amount")}/>
            </div>
            <div className="mb-4">
              <input type="submit" className='btn btn-outline-success btn-lg' value="ADD AUCTION"/>

            </div>

              </form>
              </center>
            </div>
          </div>
    </>
  )
}

export default AddAuction

// function AddAuction() {
//     const {pid} =  useParams()

//     useEffect(()=>{
//         addAuctionById()
//     },[])
//     const [auctions,setAuction]=useState({}) 

//     async function addAuctionById(){
//         const auctions = await axios.post("http://127.0.0.1:8000/apiauction/auction/"+pid)
//         console.log(auctions.data)
//         setAuction(auctions.data)
        
//     }
    
//   return (
//     <>
//     <h1>{pid}</h1>
//     </>
//   )
// }

// export default AddAuction;