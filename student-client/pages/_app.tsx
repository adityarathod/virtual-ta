import { AppProps } from "next/app";
import "../styles/globals.css";

function VirtualTA({ Component, pageProps }: AppProps) {
  return <Component {...pageProps} />;
}

export default VirtualTA;
