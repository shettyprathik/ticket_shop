import "bootstrap/dist/css/bootstrap.css";
import buildClient from "../api/build-client";
import Header from "../components/header";

const AppComponent = ({ Component, pageProps, current_user }) => {
  return (
    <div>
      <Header currentUser={current_user}></Header>
      <Component {...pageProps} currentUser={current_user}></Component>
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
