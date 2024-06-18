import type { NextPage } from "next";
import Head from "next/head";
import Image from "next/image";
import Link from "next/link";
import Header from "../components/header";
import Footer from "../components/footer";
import Banner from "../components/contactPage/banner";
import ContactInfo from "../components/contactPage/contactInfo";
import ContactForm from "../components/contactPage/contactForm";

const Contact: NextPage = () => {
  return (
    <>
      <Head><title>Meddical - Health & Contact page</title></Head>
      <Header />
      <Banner/>
      <ContactInfo/>
      <ContactForm/>
      <Footer/>
    </>)
};

export default Contact;