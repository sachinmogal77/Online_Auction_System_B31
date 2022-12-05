import React from 'react';
import ReactDOM from 'react-dom/client';
import { BrowserRouter } from 'react-router-dom';
import AppRoute from './MyComponents/AppRoute'
import '../node_modules/bootstrap/dist/css/bootstrap.min.css'

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <div className='container bg-light'>
  <BrowserRouter>
    <AppRoute/>
  </BrowserRouter>
</div>
);


