import React from 'react';
import { Link } from 'react-router-dom';
import robinhood from '../assets/robinhood.png';

import Auth from '../utils/auth';

const Header = () => {
  const logout = (event: React.FormEvent)  => {
    event.preventDefault();
    Auth.logout();
  };

  return (
    <header className="w-full flex justify-between items-center border-b border-gray-200 py-2 px-4">
      <div className='w-[100px] md:w-[130px]'>
        <Link to="/">
          <img src={robinhood} alt="robinhood logo" />
        </Link>
      </div>
      <div className="flex gap-5 md:gap-10">
        <nav className="">
          {Auth.loggedIn() ? (
            <>
              <Link to="/portfolio">My Shares</Link>
              <a href="/" onClick={logout}>
                Logout
              </a>
            </>
          ) : (
            <div className='flex gap-5 md:gap-10'>
            <div className='border px-2 py-1 md:px-4 text-md font-semibold flex items-center gap-2 hover:bg-primary hover:bg-opacity-25 active:bg-opacity-100'>
              <Link to="/login">Login</Link>
            </div>
            <div className='border px-2 py-1 md:px-4 text-md font-semibold flex items-center gap-2 hover:bg-primary hover:bg-opacity-25 active:bg-opacity-100'>
              <Link to="/signup">Signup</Link>
            </div>
            </div>
          )}
        </nav>
      </div>
    </header>
  );
};

export default Header;
