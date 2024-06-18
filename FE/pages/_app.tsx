import type { AppProps } from 'next/app'
import Script from 'next/script';
import Head from "next/head";
import "/public/css/style.css";
import "/public/plugins/bootstrap/bootstrap.min.css";
import "/public/plugins/icofont/icofont.min.css";
import "/public/plugins/slick-carousel/slick/slick.css";
import "/public/plugins/slick-carousel/slick/slick-theme.css";

function MyApp({ Component, pageProps }: AppProps) {
  return <>
  <Component {...pageProps} />
    <Head><link rel="shortcut icon" type="image/x-icon" href="/images/logo-icon.svg" /></Head>
    <Script src="/plugins/jquery/jquery.js" strategy="beforeInteractive"></Script>
    <Script src="/plugins/bootstrap/bootstrap.min.js"></Script>
    <Script src="/plugins/slick-carousel/slick/slick.min.js"></Script>
    <Script src="/plugins/shuffle/shuffle.min.js"></Script>
    <Script src="/js/script.js"></Script>
  </>
}

export default MyApp
