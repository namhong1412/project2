import Link from "next/link";

const DoctorCard = () => (
<section className="section doctor-single">
  <div className="container">
    <div className="row">
      <div className="col-lg-4 col-md-6">
        <div className="doctor-img-block">
          <img src="/images/team/1.jpg" alt="" className="img-fluid w-100"/>

          <div className="info-block mt-4">
            <h4 className="mb-0">Alexandar james</h4>
            <p>Orthopedic Surgary</p>

            <ul className="list-inline mt-4 doctor-social-links">
              <li className="list-inline-item"><Link href="#!"><i className="icofont-facebook"></i></Link></li>
              <li className="list-inline-item"><Link href="#!"><i className="icofont-twitter"></i></Link></li>
              <li className="list-inline-item"><Link href="#!"><i className="icofont-skype"></i></Link></li>
              <li className="list-inline-item"><Link href="#!"><i className="icofont-linkedin"></i></Link></li>
              <li className="list-inline-item"><Link href="#!"><i className="icofont-pinterest"></i></Link></li>
            </ul>
          </div>
        </div>
      </div>

      <div className="col-lg-8 col-md-6">
        <div className="doctor-details mt-4 mt-lg-0">
          <h2 className="text-md">Introducing to myself</h2>
          <div className="divider my-4"></div>
          <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quam tempore cumque voluptate beatae quis
            inventore sapiente nemo, a eligendi nostrum expedita veritatis neque incidunt ipsa doloribus provident ex,
            at ullam. Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ipsam, perferendis officiis esse quae,
            nobis eius explicabo quidem? Officia accusamus repudiandae ea esse non reiciendis accusantium voluptates,
            facilis enim, corrupti eligendi?</p>
          <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Nemo recusandae veritatis minus optio quod
            obcaecati laborum temporibus, deleniti vero perferendis molestias, ducimus facilis, sunt minima. Tempora,
            amet quasi asperiores voluptas?</p>

          <Link href="/appointment" className="btn btn-main-2 btn-round-full mt-3">Make an Appoinment<i
              className="icofont-simple-right ml-2  "></i></Link>
        </div>
      </div>
    </div>
  </div>
</section>
  );

export default DoctorCard;