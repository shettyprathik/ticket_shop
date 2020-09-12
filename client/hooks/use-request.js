import axios from "axios";
import { useState } from "react";
export default ({ url, method, body, onSuccess }) => {
  const [errors, setErrors] = useState(null);
  const doRequest = async () => {
    try {
      setErrors(null);
      const resp = await axios[method](url, body);
      onSuccess && onSuccess();
    } catch (err) {
      setErrors(
        <div className="alert alert-danger">
          <h4>Oops..</h4>
          <ul>
            {err.response.data.errors.map((err) => (
              <li key={err.message}>{err.message}</li>
            ))}
          </ul>
        </div>
      );
    }
  };
  return { doRequest, errors };
};
