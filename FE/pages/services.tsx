import type { NextPage } from "next";
import Head from "next/head";
import Image from "next/image";
import Link from "next/link";
import Header from "../components/header";
import Footer from "../components/footer";
import Banner from "../components/servicesPage/banner";
import Main from "../components/servicesPage/main";
import CTA from "../components/servicesPage/cta";

const Services: NextPage = () => {
  return (
    <>
      <Head>
        <title><title>Meddical - Health & Services page</title></title>
      </Head>
      <Header />
      <Banner/>
      <Main/>
      <CTA/>
      <Footer />
    </>)
};

export default Services;