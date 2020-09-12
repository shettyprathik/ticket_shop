import { useState } from "react";
import axios from "axios";

export default () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [errors, setErrors] = useState([]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    console.log(email, password);
    try {
      const resp = await axios.post("/api/users/signup", { email, password });
    } catch (err) {
      setErrors(err.response.data.errors);
    }
  };
  return (
    <form onSubmit={handleSubmit}>
      <h1>Sign up</h1>
      <div className="form-group">
        <label>Email Address</label>
        <input
          type="email"
          className="form-control"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
        ></input>
      </div>
      <div className="form-group">
        <label>Password</label>
        <input
          type="password"
          className="form-control"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        ></input>
      </div>
      {errors.length > 0 && (
        <div className="alert alert-danger">
          <h4>Oops..</h4>
          <ul>
            {errors.map((err) => (
              <li key={err.message}>{err.message}</li>
            ))}
          </ul>
        </div>
      )}

      <button type="submit" className="btn btn-primary">
        Sign Up
      </button>
    </form>
  );
};
