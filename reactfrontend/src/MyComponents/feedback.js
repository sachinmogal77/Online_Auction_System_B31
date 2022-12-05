import axios from 'axios'
import React from 'react'
import { useForm } from 'react-hook-form'



function Feedback(){
   const{handleSubmit,register,formState: { errors }}=useForm()
   
   const headers={
    'Content-Type':'multipart/form-data'

   }
 
   
   function addFeedback(obj){
    axios.post('http://127.0.0.1:8000/api3/feedback/',obj,{headers:headers})
    console.log(obj)
    alert("Your Feedback is Submitted!!!")
   }
   
   
  
    return (<>
    <div>
    <div className="container">
        <div className="row">
            <br></br>
            <div className="card col-md-6 offset-md-3 offset-md-3">
                <div className="card-body">
                    <form  onSubmit={handleSubmit(addFeedback)}>
                        <div className="form-group">
                            <input type="email" class="form-control" placeholder="Email" {...register("email",{ required: true, pattern: /^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}$/i })}/>
                            {errors.email && <span>Invalid email</span>}
                            
                        </div>
                        <br></br>
                        <div className="form-group">
                            <input type="text" class="form-control" placeholder="Response" {...register("response")}/>
                        </div>
                        <br></br>
                        <div className='mb-5 text-center'>
                            <input type="submit" class="btn btn-outline-success" />       
                        </div>
        
                    </form>
                </div>
            </div>
        </div>
    </div>
    </div>
        </>)
    
    }
export default Feedback;