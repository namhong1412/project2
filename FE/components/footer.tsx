import Link from 'next/link';

const Footer = () => (
  <footer className="footer section gray-bg">
    <div className="container">
      <div className="row">
        <div className="col-lg-4 mr-auto col-sm-6">
          <div className="widget mb-5 mb-lg-0">
            <div className="logo mb-4">
              <img src="/images/logo.svg" alt="Logo" width={150} height={50} />
            </div>
            <p>Health is a state of complete physical, mental and social well-being, and not merely the absence of disease or infirmity.</p>

            <ul className="list-inline footer-socials mt-4">
              <li className="list-inline-item">
                <Link href="#"><i className="icofont-facebook"></i></Link>
              </li>
              <li className="list-inline-item">
                <Link href="#"><i className="icofont-twitter"></i></Link>
              </li>
              <li className="list-inline-item">
                <Link href="#"><i className="icofont-linkedin"></i></Link>
              </li>
            </ul>
          </div>
        </div>

        <div className="col-lg-2 col-md-6 col-sm-6">
          <div className="widget widget-contact mb-5 mb-lg-0">
            <h4 className="text-capitalize mb-3">Get in Touch</h4>
            <div className="divider mb-4"></div>

            <ul className="list-unstyled footer-contact-list">
              <li className="d-flex align-items-center">
                <i className="icofont-location-pin"></i>
                <span>Address : Ta-134/A, New York, USA</span>
              </li>
              <li className="d-flex align-items-center">
                <i className="icofont-phone"></i>
                <span>Phone : +23-345-67890</span>
              </li>
              <li className="d-flex align-items-center">
                <i className="icofont-envelope"></i>
                <span>Email : support@meddical.com</span>
              </li>
            </ul>
          </div>
        </div>

        <div className="col-lg-2 col-md-6 col-sm-6">
          <div className="widget widget-links mb-5 mb-lg-0">
            <h4 className="text-capitalize mb-3">Quick Links</h4>
            <div className="divider mb-4"></div>

            <ul className="list-unstyled footer-contact-list">
              <li><Link href="#">Support</Link></li>
              <li><Link href="#">Helpline</Link></li>
              <li><Link href="#">Courses</Link></li>
              <li><Link href="/about">About</Link></li>
              <li><Link href="#">Career</Link></li>
              <li><Link href="#">Mobile App</Link></li>
            </ul>
          </div>
        </div>

        <div className="col-lg-4 col-sm-6">
          <div className="widget widget-subscribe mb-5 mb-lg-0">
            <h4 className="text-capitalize mb-3">Newsletter</h4>
            <div className="divider mb-4"></div>

            <p>Subscribe to our newsletter for the latest updates, special offers, and promotions.</p>
            <form action="#" className="subscribe-form">
              <input type="text" className="form-control mb-3" placeholder="Your Email address" />
              <button type="submit" className="btn btn-main btn-round-full">Subscribe</button>
            </form>
          </div>
        </div>
      </div>
    </div>
  </footer>
);

export default Footer;