import type { NextPage } from "next";
import Head from "next/head";
import Image from "next/image";
import Link from "next/link";
import Header from "../components/header";
import Footer from "../components/footer";
import Confirmation_ from "../components/confirmationPage/confirmation";

const Confirmation: NextPage = () => {
  return (
    <>
      <Head>
        <title>Confirmation</title>
      </Head>
      <Header/>
      <Confirmation_/>
      <Footer/>
    </>)
};

export default Confirmation;
