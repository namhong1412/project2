import Link from 'next/link';

const Header = () => (
  <header>
    <div className="header-top-bar">
      <div className="container">
        <div className="row align-items-center">
          <div className="col-lg-6">
            <ul className="top-bar-info list-inline-item pl-0 mb-0">
              <li className="list-inline-item">
                <Link href="mailto:support@gmail.com">
                  <i className="icofont-support-faq mr-2"></i>
                  support@meddical.com
                </Link>
              </li>
              <li className="list-inline-item">
                <i className="icofont-location-pin mr-2"></i>
                Address Ta-134/A, New York, USA
              </li>
            </ul>
          </div>
          <div className="col-lg-6">
            <div className="text-lg-right top-right-bar mt-2 mt-lg-0">
              <Link href="tel:+23-345-67890">
                <span>Call Now : </span>
                <span className="h4">823-4565-13456</span>
              </Link>
            </div>
          </div>
        </div>
      </div>
    </div>

    <nav className="navbar navbar-expand-lg navigation" id="navbar">
      <div className="container">
          <Link href="/" className="navbar-brand">
            <img src="/images/logo.svg" alt="Logo" width={150} height={50} />
          </Link>

        <button className="navbar-toggler collapsed" type="button" data-toggle="collapse" data-target="#navbarmain"
          aria-controls="navbarmain" aria-expanded="false" aria-label="Toggle navigation">
          <span className="icofont-navigation-menu"></span>
        </button>

        <div className="collapse navbar-collapse" id="navbarmain">
          <ul className="navbar-nav ml-auto">
            <li className="nav-item active">
                <Link href="/" className="nav-link">Home</Link>
            </li>
            <li className="nav-item">
              <Link href="/about" className="nav-link">About</Link>
            </li>
            <li className="nav-item">
                <Link href="/services" className="nav-link">Services</Link>
            </li>
            <li className="nav-item dropdown">
                <Link href="/department" className="nav-link dropdown-toggle" id="dropdown02" data-toggle="dropdown"
                  aria-haspopup="true" aria-expanded="false">Department <i className="icofont-thin-down"></i></Link>
              <ul className="dropdown-menu" aria-labelledby="dropdown02">
                <li>
                    <Link href="/department" className="dropdown-item">Departments</Link>
                </li>
                <li>
                    <Link href="/departmentSingle" className="dropdown-item">Department Single</Link>
                </li>
              </ul>
            </li>
            <li className="nav-item dropdown">
                <Link href="/doctors" className="nav-link dropdown-toggle" id="dropdown03" data-toggle="dropdown"
                  aria-haspopup="true" aria-expanded="false">Doctors <i className="icofont-thin-down"></i></Link>
              <ul className="dropdown-menu" aria-labelledby="dropdown03">
                <li>
                    <Link href="/doctors" className="dropdown-item">Doctors</Link>
                </li>
                <li>
                    <Link href="/doctorsSingle" className="dropdown-item">Doctor Single</Link>
                </li>
                <li>
                    <Link href="/appointment" className="dropdown-item">Appointment</Link>
                </li>
              </ul>
            </li>
            <li className="nav-item">
                <Link href="/contact" className="nav-link">Contact</Link>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  </header>
);

export default Header;