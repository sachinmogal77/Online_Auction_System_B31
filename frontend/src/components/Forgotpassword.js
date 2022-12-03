

export const ForgotPassword=()=>{

   
        const form = useRef();
        const checkBtn = useRef();
        const [email, setEmail] = useState("");
        const [loading, setLoading] = useState(false);
        const [message, setMessage] = useState("");
        const onChangeUsername = (e) => {
            const email = e.target.value;
            setEmail(email);
        };
        const handleSubmit = (e) => {
            e.preventDefault();
            setMessage("");
            setLoading(true);
            form.current.validateAll();
            if (checkBtn.current.context._errors.length === 0) {
               
                        setLoading(false);
                     }
                    (error) => {
                        const resMessage =
                            (error.response &&
                                error.response.data &&
                                error.response.data.message) ||
                            error.message ||
                            error.toString();
                        setLoading(false);
                        setMessage(resMessage);
                    }
            }

    return(<>
        <div className="col-md-14">
                    <div className="page_heading text-center">
                        <h1>Reset your password</h1>
                    </div>
                    <div className="form-content_text text-center">
                        <p>We will send you an email to reset your password.</p>
                    </div>
                    <hr></hr>
                        <form>
                            <center>
                        <div className="form-group col-md-4">
                        <input type="email" className="form-control" placeholder="Email Address"/>
                        </div>
                        <br></br><br></br>
                        </center>
                        <center><button type="submit" className="btn btn-outline-success col-2">SEND EMAIL</button></center>
                        </form>
                        </div>
    </>)
}