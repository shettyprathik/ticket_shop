import buildClient from "../api/build-client";

const LandingPage = ({ current_user }) => {
  return current_user ? (
    <h1>You are signed in</h1>
  ) : (
    <h1>You are not signed in</h1>
  );
};

LandingPage.getInitialProps = async ({ req }) => {
  try {
    let resp = await buildClient(req).get("/api/users/current_user");
    return resp.data;
  } catch (err) {
    return { current_user: null };
  }
};
export default LandingPage;
