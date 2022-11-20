import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Footer from './components/Footer';
import Header from './components/Header';
import Buy from './pages/Buy';
import Home from './pages/Home';

import Login from './pages/Login';
import NoMatch from './pages/NoMatch';
import Portfolio from './pages/Portfolio';
import Signup from './pages/Signup';

function App() {


  return (
    <Router>
        <div className="flex-column justify-flex-start h-100">
          <Header />
          <div className="container">
            <Routes>
              <Route 
                path="/" 
                element={<Home />} 
              />
              <Route 
                path="/login" 
                element={<Login />} 
              />
              <Route 
                path="/signup" 
                element={<Signup />} 
              />
              <Route 
                path="/portfolio" 
                element={<Portfolio />} 
              />
              <Route 
                path="/purchase/:ticker" 
                element={<Buy />} 
              />
              <Route 
                path="*"
                element={<NoMatch />} 
              />
            </Routes>
          </div>
          <Footer />
        </div>
    </Router>
  );
}

export default App;