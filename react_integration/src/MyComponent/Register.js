import React, { useState } from 'react'

import countrydata from './../CountryData.json'
import 'react-phone-number-input/style.css'
import PhoneInput from 'react-phone-number-input'
import axios from 'axios'
import { useForm } from 'react-hook-form'



function Register() {

  const [Number, setNumber] = useState()

  //console.log(Number)
  
  // const[countryid,setCountryId]=useState('')

   const[state,setState]=useState([])

  // const[stateid,setStateId]=useState('')

  const handlecountry=(e)=>{
       const getcountryID=e.target.value;
       //console.log(getcountryID)

       const getStateData=countrydata.find(country=>country.country_id===getcountryID).states;
       setState(getStateData);
         }

    const{handleSubmit,register}=useForm()

     function getUserReg(obj){
      console.log(obj)

     }
  return (
    <>
         <center>
    <br/>
    <form onSubmit={handleSubmit(getUserReg)}>
    <div className='row-ml-6'>
       <div className='col-md-6 text-center'>
    <h2 className='text-light'><b>Create User</b></h2>


    <div className="mb-4">
    <input type='text' className='form-control text-center' placeholder='First name' {...register('first_name')}/>
    </div>

    <div className="mb-4">
    <input type='text' className='form-control text-center' placeholder='Last name'{...register('last_name')}/>
    </div>

    <div className="mb-4">
    <input type='text' className='form-control text-center' placeholder='Username'{...register('username')}/>
    </div>

    <div className="mb-4">
    <input type='text' className='form-control text-center' placeholder='Password'{...register('password')}/>
    </div>

    
  {/* <div className="mb-4">
    <input class="form-check-input" type="radio" name="gender" value='Male'{...register('gender')}/>
    <label class="form-check-label">Male</label>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
    <input class="form-check-input" type="radio" name="gender" value='Female'{...register('gender')}/>
    <label class="form-check-label">Female</label>
  </div> */}


    <div className="mb-4">
    <input type='text' className='form-control text-center' placeholder='Email Address'{...register('email')}/>
    </div>

    <div class="mb-3">
  <label  className='text-light'><b>Aadhar card</b></label>
  <input class="form-control" type="file"{...register('aadhar_card')} />
</div>

<div class="mb-3">
  <label  className='text-light'><b>Pan Card</b></label>
  <input class="form-control" type="file"{...register('pan_card')} />
</div>

<div class="mb-3">
  <label  className='text-light'><b>Passport Front</b></label>
  <input class="form-control" type="file" {...register('passport_front')}/>
</div>

<div class="mb-3">
  <label  className='text-light'><b>Passport Back</b></label>
  <input class="form-control" type="file" {...register('passport_back')}/>
</div>
<div className="mb-4">
<PhoneInput placeholder="Enter Phone Number" className='form-control text-center' value={Number} onChange={setNumber} {...register('contact_no')}/>
</div>

  
  <div className="mb-4">
    <select class="form-select text-center" aria-label="Default select example" onChange={(e)=>handlecountry(e)}>
        <option value="">Select Country</option>
        {
          countrydata.map((getcountry,index)=>(
            <option value={getcountry.country_id} key={index}>{getcountry.country_name}</option>
          ))
        }
        
   </select>
    </div>

    <div className="mb-4">
    <select class="form-select text-center" aria-label="Default select example">
        <option value="">Select State</option>
        {
          state.map((getstate,index)=>(
            <option value={getstate.state_id} key={index}>{getstate.state_name}</option>
          ))
        }
        
    </select>
    </div>

   

    <div className="mb-4">
    <input type='textarea' className='form-control text-center' placeholder='Address'{...register('address')}/>
    </div>


    <div className="mb-4">
    <input type='text' className='form-control text-center' placeholder='City'{...register('city')}/>
    </div>


    <div className="mb-4">
    <input type='number' className='form-control text-center' placeholder='Pin Code'{...register('pincode')}/>
    </div>

  


  <div className="mb-4">
    <input type='submit' className='btn btn-outline-success btn-lg' value='Create User'/>
  </div>


       </div>
    </div>
    </form>
    </center>
    </>
  )
}

export default Register