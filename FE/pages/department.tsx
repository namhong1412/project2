import type { NextPage } from "next";
import Head from "next/head";
import Image from "next/image";
import Link from "next/link";
import Header from "../components/header";
import Footer from "../components/footer";
import Banner from "../components/departmentPage/banner";
import Departments from "../components/departmentPage/departments";

const Department: NextPage = () => {
  return (
    <>
      <Head>
        <title>Meddical - Health & Departments page</title>
      </Head>
      <Header/>
      <Banner/>
      <Departments/>
      <Footer/>
    </>)
};

export default Department;