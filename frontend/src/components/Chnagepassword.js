import axios from "axios";
import { useForm } from "react-hook-form";
import { useNavigate } from "react-router-dom";


export const ChangePassword=()=>{
    const navi = useNavigate();

    const {register , handleSubmit} = useForm()

    const token =localStorage.getItem('jwt token');

    const data= {
        "old_password":"sometext",
        "new_password":"othertext"
    }

    var formData = new FormData();
    
    for(var name in data){
        formData.append(name, data[name])
    }

    const headers = {
        'authorization': `Token ${token}`
    };

    const ChangePassword=(newPass)=>{
        
        fetch("http://127.0.0.1:8000/uapi/access_token/",{
            headers,

            'body':formData,
        })
        .then(res=>{
            axios.post('http://127.0.0.1:8000/uapi/change_password/', newPass)
            if(res.ok){
                console.log('Succefully changed password');
                return res.json();
            } else{
                console.log('error changing password');
            }
        })
        .then(res=>{
            console.log('change password res',res);
        });
        navi('/home')
    }

    return(
    <><div className="col-md-14">
        <form onSubmit={handleSubmit(ChangePassword)}> 
        <center><h1>Change Password</h1></center>
        <hr />
        <center>
            <div className="form-group col-md-4">
                <input type="password" className="form-control" placeholder="Old Password" {...register('old_password')}/>
            </div>
            <br></br>
            <div className="form-group col-md-4">
                <input type="password" className="form-control" placeholder="New Password" {...register('new_password')}/>
            </div>
            <br></br>
            
            <div className="mb-4">
            <center><button type="submit" className="btn btn-outline-primary col-2">Submit</button></center>
            </div></center>
        </form>
        
        
    </div>
    </>)
};