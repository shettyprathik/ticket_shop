import { useEffect } from "react";
import Router from "next/router";
import useRequset from "../../hooks/use-request";

export default () => {
  const { doRequest } = useRequset({
    url: "/api/users/signout",
    method: "post",
    body: {},
    onSuccess: () => Router.push("/"),
  });

  useEffect(() => {
    doRequest();
  }, []);
  return <div>Signing you out...</div>;
};
