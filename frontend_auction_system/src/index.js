import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import '../node_modules/bootstrap/dist/css/bootstrap.min.css';
import { BrowserRouter } from 'react-router-dom';
import AppRoutes from './Routing/AppRoutes';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  
  <div className='container bg-light'>
    <center>
  <BrowserRouter>
  <AppRoutes/>
  </BrowserRouter>
  </center>
  </div>
  
);
