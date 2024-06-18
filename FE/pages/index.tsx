import type { NextPage } from "next";
import Head from "next/head";
import Image from "next/image";
import Link from "next/link";
import Header from "../components/header";
import Banner from "../components/homePage/banner";
import Features from "../components/homePage/features";
import Footer from "../components/footer";
import About from "../components/homePage/about";
import CTA from "../components/homePage/cta";
import Service from "../components/homePage/service";
import Appointment from "../components/homePage/appointment";
import Testimonial from "../components/homePage/testimonial";
import Clients from "../components/homePage/clients";


const Home: NextPage = () => {
  return (
    <>
      <Head>
        <title>Meddical - Health & Home page</title>
      </Head>
      <Header />
      <Banner />
      <Features />
      <About />
      <CTA />
      <Service />
      <Appointment />
      <Testimonial />
      <Clients />
      <Footer />
    </>
  );
};

export default Home;
