import type { NextPage } from "next";
import Head from "next/head";
import Image from "next/image";
import Link from "next/link";
import Header from "../components/header";
import Footer from "../components/footer";
import Banner from "../components/appointmentPage/banner";
import Appointment_ from "../components/appointmentPage/appointment";

const Appointment: NextPage = () => {
  return (
    <>
      <Head>
        <title>Meddical - Health & Appointment page</title>
      </Head>
      <Header />
      <Banner />
      <Appointment_/>
      <Footer />
    </>)
};

export default Appointment;