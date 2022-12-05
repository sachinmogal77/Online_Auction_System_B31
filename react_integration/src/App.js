import { BrowserRouter } from 'react-router-dom';
import '../node_modules/bootstrap/dist/css/bootstrap.min.css'
import './App.css';
import image from "./img/buil.jpg"; 
import AppRouters from './MyComponent/AppRouters';


function App() {
  return (
    <>
   
 <div style={{ backgroundImage:`url(${image})`,backgroundPosition: "center",
                                        backgroundSize: "cover",backgroundRepeat: "no-repeat",
                                        width: "100vw",height: "185vh",}}>
     <BrowserRouter>
    <AppRouters/>
    
    </BrowserRouter>
  
    </div>
</>
  );
}

export default App;
