import buildClient from "../api/build-client";

const LandingPage = ({ current_user }) => {
  return current_user ? (
    <h1>You are signed in</h1>
  ) : (
    <h1>You are not signed in</h1>
  );
};

export default LandingPage;
