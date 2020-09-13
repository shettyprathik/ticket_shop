import "bootstrap/dist/css/bootstrap.css";
import buildClient from "../api/build-client";

const AppComponent = ({ Component, pageProps, current_user }) => {
  return (
    <div>
      <h1>{current_user && current_user.email}</h1>
      <Component {...pageProps} current_user={current_user}></Component>
    </div>
  );
};

AppComponent.getInitialProps = async (appContext) => {
  try {
    let resp = await buildClient(appContext.ctx.req).get(
      "/api/users/current_user"
    );
    console.log("In _app");

    let pageProps = {};
    if (appContext.Component.getInitialProps) {
      pageProps = await appContext.Component.getInitialProps(appContext.ctx);
    }
    return { pageProps, ...resp.data };
  } catch (err) {
    return {
      current_user: null,
    };
  }
};

export default AppComponent;
