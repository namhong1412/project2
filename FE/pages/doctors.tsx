import type { NextPage } from "next";
import Head from "next/head";
import Image from "next/image";
import Link from "next/link";
import Header from "../components/header";
import Footer from "../components/footer";
import Banner from "../components/doctorsPage/banner";
import Portfolio from "../components/doctorsPage/portfolio";

const Doctors: NextPage = () => {
  return (
    <>
      <Head>
        <title>Meddical - Health & Doctors page</title>
      </Head>
      <Header/>
      <Banner/>
      <Portfolio/>
      <Footer/>
    </>)
};

export default Doctors;