import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import robinhood from '../assets/robinhood.png';
import { Search } from 'tabler-icons-react';

import Auth from '../utils/auth';

const Header = () => {
  const [searchValue, setSearchValue] = useState('');
  const [loggedIn, setLoggedIn] = useState(false)
  const logout = (event: React.FormEvent)  => {
    event.preventDefault();
    Auth.logout();
  };

  const handleSearch = async (e: { preventDefault: () => void }) => {
    e.preventDefault();
    
    await fetch('/api/quote')
      .then(res => res.json())
      .then(data => console.log(data));
  };

  return (
    <header className="w-full flex justify-between items-center border-b border-gray-200 py-2 px-4">
      <div className='w-[100px] md:w-[130px]'>
        <Link to="/">
          <img src={robinhood} alt="robinhood logo" />
        </Link>
      </div>

      <div className='relative hidden md:block'>
        <form
          onSubmit={handleSearch}
          className='absolute md:static top-10 -left-20 bg-white'
        >
          <input
            value={searchValue}
            onChange={(e) => setSearchValue(e.target.value)}
            className='bg-primary p-3 md:text-md font-medium border-2 border-gray-100 focus:outline-none focus:border-2 focus:border-gray-300 w-[300px] md:w-[350px] rounded  md:top-0'
            placeholder="Search stocks and ETF's"
          />
          <button
            onClick={handleSearch}
            className='absolute md:right-5 right-6 top-4 border-l-2 border-gray-300 pl-4 text-2xl text-gray-400'
          >
            <Search />
          </button>
        </form>
      </div>

      <div className="flex gap-5 md:gap-10">
        <nav className="">
          {loggedIn ? (
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
