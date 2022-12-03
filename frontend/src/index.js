import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import '../node_modules/bootstrap/dist/css/bootstrap.min.css'
import { BrowserRouter } from 'react-router-dom';
import AppRoutes from './components/AppRoutes';

const root = ReactDOM.createRoot(document.getElementById('root'));

root.render(
  <>
 
  <BrowserRouter>
    <AppRoutes/>
  </BrowserRouter>
  </>
 
 
);
