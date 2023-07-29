import React from 'react'
import { NavLink } from 'react-router-dom';
import styled, { css } from 'styled-components';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Login from "./Login"
import Register from "./Register"

const Nav = () => {

     
  return (
    
   <Wrapper className="section">
<nav class="navbar navbar-expand-lg navbar-light ">
        <a class="navbar-brand" href="homepage.html"><span class="material-symbols-outlined">
            agriculture
            </span>FarmFresh</a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
      
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav mr-auto">
            <li class="nav-item active">
              <a class="nav-link" href="web.html">Home</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#">Shop</a>
            </li>
            <li class="nav-item dropdown">
              <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                New Arrival
              </a>
              <div class="dropdown-menu" aria-labelledby="navbarDropdown">
                <a class="dropdown-item" href="#">Vegetables</a>
                <a class="dropdown-item" href="#">Fruits</a>
                <div class="dropdown-divider"></div>
                <a class="dropdown-item" href="#">Other</a>
              </div>
            </li>
           
          </ul>
          <form class="form-inline my-2 my-lg-0">
          <NavLink to="/Login">
                Shop Now
             </NavLink>
          
            <button class="btn my-2 my-sm-0 mr-4" type="submit" id="btn-navbar"><a >Login</a></button>
            <button class="btn  my-2 my-sm-0" type="submit" id="btn-navbar"><a href="ContactUs.html">Contact</a></button>
          </form>
        </div>
      </nav>

      </Wrapper>
     
    
  );
};

const Wrapper = styled.section`

nav{

    background-color: #446e35;
  
  }

.dropdown-menu
{
  opacity: 0.8;
  color: black;
  background-color:  #446e35;
}
.dropdown-menu a{
  
  color: black;
}
#btn-navbar{

    border: 1px solid  #3a5d28;;
    background-color: #3a5d28;;
}

#btn-navbar:hover{
    background-color: #446e35;
}

#btn-navbar a{
    color: black;
    text-decoration: none;
}
  

`

export default Nav
