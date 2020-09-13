import axios from "axios";
export default (req) => {
  if (typeof window === "undefined") {
    // In server (browser refresh, reroute from different domain)
    // http://<name_of_service>.<name_of_namespace>.svc.cluster.local
    return axios.create({
      baseURL: "http://my-release-ingress-nginx-controller",
      headers: req.headers,
    });
  } else {
    return axios.create({ baseURL: "/" });
  }
};
