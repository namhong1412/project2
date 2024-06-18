import Link from 'next/link';

const CTA = () => (
<section className="section cta-page">
  <div className="container">
    <div className="row">
      <div className="col-lg-7">
        <div className="cta-content">
          <div className="divider mb-4"></div>
          <h2 className="mb-5 text-lg">We are pleased to offer you the <span className="title-color">chance to have the healthy</span></h2>
          <Link href="/appointment" className="btn btn-main-2 btn-round-full">Get appoinment<i className="icofont-simple-right  ml-2"></i></Link>
        </div>
      </div>
    </div>
  </div>
</section>);

export default CTA;