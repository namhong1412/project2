import type { NextPage } from "next";
import Head from "next/head";
import Image from "next/image";
import Link from "next/link";
import Header from "../components/header";
import Footer from "../components/footer";
import Banner from "../components/deapartmentSinglePage/banner";
import DepartmentList from "../components/deapartmentSinglePage/departmentList";

const Services: NextPage = () => {
  return (
    <>
      <Head>
        <title>Meddical - Health & Department-single page</title>
      </Head>
      <Header/>
      <Banner/>
      <DepartmentList/>
      <Footer/>
    </>)
};

export default Services;