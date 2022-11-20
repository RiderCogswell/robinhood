import React, { useState } from 'react'

const Login = () => {
  const [formState, setFormState] = useState({ email: '', password: '' });

  const handleFormSubmit = (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    console.log(formState);

    try {
      fetch('/api/users/login', {
        method: 'POST',
        body: JSON.stringify(formState),
        headers: { 'Content-Type': 'application/json' },
      });
    } catch (err) {
      console.log(err);
    }
  }

  const handleChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value } = event.target;
    setFormState({
      ...formState,
      [name]: value,
    });
  };

  return (
    <div className="container my-1">


    <h2>Login</h2>
    <form onSubmit={handleFormSubmit}>
      <div className="flex-row space-between my-2">
        <label htmlFor="email">Email address:</label>
        <input
          placeholder="youremail@test.com"
          name="email"
          type="email"
          id="email"
          onChange={handleChange}
        />
      </div>
      <div className="flex-row space-between my-2">
        <label htmlFor="pwd">Password:</label>
        <input
          placeholder="******"
          name="password"
          type="password"
          id="pwd"
          onChange={handleChange}
        />
      </div>
      <div className="flex-row flex-end">
        <button type="submit">Submit</button>
      </div>
    </form>
  </div>
  )
}

export default Login