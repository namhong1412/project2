import Link from 'next/link';

const Team = () => (
<section className="section team">
  <div className="container">
    <div className="row justify-content-center">
      <div className="col-lg-6">
        <div className="section-title text-center">
          <h2 className="mb-4">Meet Our Specialist</h2>
          <div className="divider mx-auto my-4"></div>
          <p>Today’s users expect effortless experiences. Don’t let essential people and processes stay stuck in the past. Speed it up, skip the hassles</p>
        </div>
      </div>
    </div>

    <div className="row">
      <div className="col-lg-3 col-md-6 col-sm-6">
        <div className="team-block mb-5 mb-lg-0">
          <img src="/images/team/1.jpg" alt="" className="img-fluid w-100"/>

          <div className="content">
            <h4 className="mt-4 mb-0"><Link href="/doctorsSingle">John Marshal</Link></h4>
            <p>Internist, Emergency Physician</p>
          </div>
        </div>
      </div>

      <div className="col-lg-3 col-md-6 col-sm-6">
        <div className="team-block mb-5 mb-lg-0">
          <img src="/images/team/2.jpg" alt="" className="img-fluid w-100"/>

          <div className="content">
            <h4 className="mt-4 mb-0"><Link href="/doctorsSingle">Marshal Root</Link></h4>
            <p>Surgeon, Сardiologist</p>
          </div>
        </div>
      </div>

      <div className="col-lg-3 col-md-6 col-sm-6">
        <div className="team-block mb-5 mb-lg-0">
          <img src="/images/team/3.jpg" alt="" className="img-fluid w-100"/>

          <div className="content">
            <h4 className="mt-4 mb-0"><Link href="/doctorsSingle">Siamon john</Link></h4>
            <p>Internist, General Practitioner</p>
          </div>
        </div>
      </div>
      <div className="col-lg-3 col-md-6 col-sm-6">
        <div className="team-block">
          <img src="/images/team/4.jpg" alt="" className="img-fluid w-100"/>

          <div className="content">
            <h4 className="mt-4 mb-0"><Link href="/doctorsSingle">Rishat Ahmed</Link></h4>
            <p>Orthopedic Surgeon</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>
        );

export default Team;