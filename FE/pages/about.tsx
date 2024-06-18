import type { NextPage } from "next";
import Head from "next/head";
import Image from "next/image";
import Link from "next/link";
import Header from "../components/header";
import Footer from "../components/footer";
import Banner from "../components/aboutPage/banner";
import AboutText from "../components/aboutPage/aboutText";
import Features from "../components/aboutPage/features";
import Awards from "../components/aboutPage/awards";
import Team from "../components/aboutPage/team";
import Testimonial from "../components/aboutPage/testimonial";

const About: NextPage = () => {
  return (
    <>
      <Head>
        <title>Meddical - Health & About us page</title>
      </Head>
        <Header/>
        <Banner/>
        <AboutText/>
        <Features/>
        <Awards/>
        <Team/>
        <Testimonial/>
        <Footer/>
    </>)};

export default About;