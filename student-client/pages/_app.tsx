import { AppProps } from "next/app";
import "../styles/globals.css";
import "katex/dist/katex.min.css";

function VirtualTA({ Component, pageProps }: AppProps) {
  return <Component {...pageProps} />;
}

export default VirtualTA;
