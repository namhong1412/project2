import type { NextPage } from "next";
import Head from "next/head";
import Image from "next/image";
import Link from "next/link";
import Header from "../components/header";
import Footer from "../components/footer";
import Banner from "../components/doctorsSinglePage/banner";
import DoctorCard from "../components/doctorsSinglePage/doctorCard";
import DoctorSkills from "../components/doctorsSinglePage/doctorSkills";
import DoctorQualification from "../components/doctorsSinglePage/doctorQualification";

const DoctorsSingle: NextPage = () => {
  return (
    <>
      <Head>
        <title>Meddical - Health & Doctors Single</title>
      </Head>
      <Header />
      <Banner />
      <DoctorCard/>
      <DoctorQualification/>
      <DoctorSkills/>
      <Footer/>
    </>)
};

export default DoctorsSingle;