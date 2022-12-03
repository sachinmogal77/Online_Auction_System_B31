import { useForm }  from 'react-hook-form'
import { useNavigate } from 'react-router-dom'
import axios from 'axios'
axios.defaults.withCredentials = true

const Register=()=>{

    const {register , handleSubmit} = useForm()

    const navi = useNavigate()

     function getUserRegister(userOBJ){
        console.log(userOBJ)
        userOBJ.pan_card=userOBJ.pan_card[0]
        userOBJ.aadhar_card=userOBJ.aadhar_card[0]
        userOBJ.passport_back = userOBJ.passport_back[0]
        userOBJ.passport_front = userOBJ.passport_front[0]

        // const headers = {
        //   'Content-Type':'multipart/form-data'
        // }
        //  const resp = await axios.get('http://localhost:8000/uapi/uv/4/', userOBJ, {headers:headers})
        //  console.log(resp.status)
      //  const resp = await axios.put('http://127.0.0.1:8000/uapi/uv/',userOBJ,{headers:headers})
      //  console.log(resp.status)

        axios.post('http://127.0.0.1:8000/uapi/uv/', userOBJ)
        navi('/home')

        }

    return(<>
        <div className="col-md-4">

        <form onSubmit={handleSubmit(getUserRegister)}>
            <div className="mb-4">
              <input type="text" className="form-control" placeholder="First Name" {...register('first_name')}/>
            </div>
            <div className="mb-4">
              <input type="text" className="form-control" placeholder="Last Name" {...register('last_name')}/>
            </div>
            <div className="mb-4">
              <input type="text" className="form-control" placeholder="Username" {...register('username')}/>
            </div>
            <div className="mb-4">
              <input type="password" className="form-control" placeholder="Password" {...register('password')}/>
            </div>
            <div className="mb-4">
              <input type="password" className="form-control" placeholder="Confirm Password" {...register('confirm_password')}/>
            </div>
            <div className="mb-4">
              <input type="email" className="form-control" placeholder="Email Address" {...register('email')}/>
            </div>

            <div className="mb-4">
              <select className='form-select text-center' aria-label='Default select example' {...register('role')}>
              <option value="">Select User Category</option>
              <option value="ADMIN">ADMIN</option>
              <option value="USER">USER</option>
              </select>
            </div>

            <div className="mb-4">
              <input type="file" className="form-control" {...register('aadhar_card')}/>
            </div>
            <div className="mb-4">
              <input type="file" className="form-control" {...register('pan_card')}/>
            </div>
            <div className="mb-4">
              <input type="file" className="form-control" {...register('passport_front')}/>
            </div>
            <div className="mb-4">
              <input type="file" className="form-control" {...register('passport_back')}/>
            </div>
            <div className="mb-4">
              <input type="text" className="form-control" placeholder="Contact Number" {...register('contact_no')}/>
            </div>
            <div className="mb-4">
              <input type="text" className="form-control" placeholder="Address" {...register('address')}/>
            </div>
            <div className="mb-4">
              <input type="text" className="form-control" placeholder="City" {...register('city')}/>
            </div>
            <div className="mb-4">
              <input type="text" className="form-control" placeholder="Code" {...register('code')}/>
            </div>
            <div className="mb-4">
              <input type="text" className="form-control" placeholder="State" {...register('state')}/>
            </div>
            <div className="mb-4">
              <input type="text" className="form-control" placeholder="Country" {...register('country')}/>
            </div>
            <div className="mb-4">
              <input type="text" className="form-control" placeholder="Pincode" {...register('pincode')}/>
            </div>
            <div>
              <button type="submit" className="btn btn-primary">Submit</button>
            </div>
        </form>
        </div>
    </>)
}

export default Register;