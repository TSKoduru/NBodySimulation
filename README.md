<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<!-- README template taken from    https://github.com/othneildrew/Best-README-Template/blob/master/README.md. -->
<a name= NBodySimulation></a>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/TSKoduru/NBodySimulation">
    <img src="Images/Logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">NBody Simulator</h3>

  <p align="center">
    A fun physics simulation where you can draw planets and watch them interact!
    <br />
    <a href="https://github.com/TSKoduru/NBodySimulation"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/TSKoduru/NBodySimulation">View Demo</a>
    ·
    <a href="https://github.com/TSKoduru/NBodySimulation/issues">Report Bug</a>
    ·
    <a href="https://github.com/TSKoduru/NBodySimulation/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

It all started when I had the bright idea of making a planetary simulation. After doing a bit of research, I came across the n-body problem. The rest was history. Anyhow, this is a basic simulation of n-body physics using a KSK method
(Kick, Step, Kick) to model planetary motion. I hope you have fun playing with it!
<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [![Python][Python]][Python-url]


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

There's a few libraries that you'll need to get installed before you can start messing around with playlists.
To get a local copy up and running follow these simple example steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* pip
  ```sh
   pip install numpy
   pip install pygame
  ```

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/TSKoduru/NBodySimulation.git
   ```
<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->
## Usage

All you'll need to do is run the program, which will lead to a popup containing the simulation. Click and drag to release a new planet; A white line will be drawn containing the trajectory. Planet masses are random, but are
fairly similar. Each body will have a trail behind it; As you add more bodies, you'll be able to visualize them interact as their trails distort. Here's an example simulation with 5 bodies: <br>

 ![ExampleSim](Images/Example.png) <br>

 * KEYBINDS:
    * Press 'esc' to exit the simulation.
    * Press 'r' to reset the simulation to 0 bodies.
    * Click and drag to add a new body.


<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ROADMAP -->
## Roadmap

- Add a system to combine planets; i.e, when they collide, insert a planet with their combined mass
- Fix bug where two planets that collide head-on get launched off map (This is because as their distance goes to 0, the gravitational force on them goes to infinity.)
- Add system to allow user to choose planet sizes

_Note: I've stopped developing this proejct, so open source contributions are welcome. See the contributions section below._

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CONTACT -->
## Contact

Teja Koduru - tkoduru@umich.edu

Project Link: [https://github.com/TSKoduru/NBodySimulation](https://github.com/TSKoduru/NBodySimulation)

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/TSKoduru/NBodySimulation.svg?style=for-the-badge
[contributors-url]: https://github.com/TSKoduru/NBodySimulation/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/TSKoduru/NBodySimulation.svg?style=for-the-badge
[forks-url]: https://github.com/TSKoduru/NBodySimulation/network/members
[stars-shield]: https://img.shields.io/github/stars/TSKoduru/NBodySimulation.svg?style=for-the-badge
[stars-url]: https://github.com/TSKoduru/NBodySimulation/stargazers
[issues-shield]: https://img.shields.io/github/issues/TSKoduru/NBodySimulation.svg?style=for-the-badge
[issues-url]: https://github.com/TSKoduru/NBodySimulation/issues
[license-shield]: https://img.shields.io/github/license/TSKoduru/NBodySimulation.svg?style=for-the-badge
[license-url]: https://github.com/TSKoduru/NBodySimulation/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/tskoduru

[Python]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB

[Python-url]: https://www.python.org/
[React-url]: https://reactjs.org/


