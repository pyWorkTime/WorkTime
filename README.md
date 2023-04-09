# WorkTime
# README File is under construction



<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/pyWorkTime/WorkTime/tree/master">
    <img src="images/logo.png" alt="Logo" width="160" height="160">
  </a>

<h3 align="center">WorkTime</h3>

  <p align="center">
    Work Time attempts to make it effortless to track time spent on various tasks or projects.  A very simple user interface driven by the mouse makes it easy to start and stop timers on projects.  All results are automatically exported to an excel sheet.
    <br />
    <a href="https://github.com/pyWorkTime/WorkTime"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/pyWorkTime/WorkTime">View Demo</a>
    ·
    <a href="https://github.com/pyWorkTime/WorkTime/issues">Report Bug</a>
    ·
    <a href="https://github.com/pyWorkTime/WorkTime/issues">Request Feature</a>
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
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://example.com)

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!--
### Built With

* [![Next][Next.js]][Next-url]
* [![React][React.js]][React-url]
* [![Vue][Vue.js]][Vue-url]
* [![Angular][Angular.io]][Angular-url]
* [![Svelte][Svelte.dev]][Svelte-url]
* [![Laravel][Laravel.com]][Laravel-url]
* [![Bootstrap][Bootstrap.com]][Bootstrap-url]
* [![JQuery][JQuery.com]][JQuery-url]
-->
<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* npm
  ```sh
  npm install npm@latest -g
  ```

### Installation


1. Clone the repo into an empty directory
   ```sh
   git clone https://github.com/pyWorkTime/WorkTime.git
   ```
3. Install required packages
   ```sh
   pip3 install -r requirements.txt
   ```
4. Create the input yaml file(s). You can use multiple files, where each file represents a collection of projects. This might be useful if there are multiple clients and you need to track individual projects under each client.  You can then bind the UI with these elements to individual hotkeys.

   ```yaml
   ---
   projects:
     - name: Helium
       id: 12345
     - name: Argon
       id: 54321
     - name: Neon
       id: 8675
     - name: Iron
       id: 5309
     - name: Mercury
       id: 777
     - name: Oxygen
       id: 888
   ```

5. Bind to a hotkey or key combination of your choosing. This can be done via a tool such as:
    - AutoHotKey
    - AutoIT
    - [Microsoft PowerToys - Keyboard Manager](https://learn.microsoft.com/en-us/windows/powertoys/keyboard-manager)
    - Keyboard manufacturer's software (ie Corsair's iCUE)

For example to bind the yaml file 'projects.yml' to cntrl+alt+p on Windows using AutoHotKey would look like this:

```
^!p::
RunWait, C:\Windows\pyw.exe "C:\some\path\here\worktime.py" "projects.yml"
return
```

Note that if you do not specify a .yml file name it will assume the file is title 'default.yml'.  The example below will use cntrl+alt+d to call the 'default.yml' file because no file argument is given.

```
^!d::
RunWait, C:\Windows\pyw.exe "C:\some\path\here\worktime.py"
return
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Create a new yaml file with .yml file extension.  You can create multiple yaml files you want to use multiple wheel menus on different binds.
An example of the contents of default.yml file is below.


This yaml file will produce a wheel menu with six items.  Each item will have a start/stop/remark button attached to it.

<!-- _For more examples, please refer to the [Documentation](https://example.com)_ -->

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [X] Cleaned excel output to remove unwanted entries
- [ ] Permissions problems if the excel file is currently in use by the user
- [ ] Customizable idle timeout (current default is 10 seconds)
- [ ] Theme support
- [ ] Install via pip
- [ ] It currently incorrectly calculates times that span multiple days as modulo of 24 hours, for example 134 hours (5 days and 14 hours) becomes 14 hours
- [ ] Add visual indicator to primary ring to indicate which projects are currently running a timer.
- [ ] Increase number of rings from 2 to 3
    - [ ] This should be dynamic based on user input

See the [open issues](https://github.com/pyWorkTime/WorkTime/issues) for a full list of proposed features (and known issues).

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

<!-- Your Name - [@twitter_handle](https://twitter.com/twitter_handle) - email@email_client.com -->

Project Link: [https://github.com/pyWorkTime/WorkTime](https://github.com/pyWorkTime/WorkTime)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [Simon Schneegans idea for a coral menu ](https://vimeo.com/51072812?embedded=true&source=vimeo_logo&owner=1313676)
* []()
* []()

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/pyWorkTime/WorkTime.svg?style=for-the-badge
[contributors-url]: https://github.com/pyWorkTime/WorkTime/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/pyWorkTime/WorkTime.svg?style=for-the-badge
[forks-url]: https://github.com/pyWorkTime/WorkTime/network/members
[stars-shield]: https://img.shields.io/github/stars/pyWorkTime/WorkTime.svg?style=for-the-badge
[stars-url]: https://github.com/pyWorkTime/WorkTime/stargazers
[issues-shield]: https://img.shields.io/github/issues/pyWorkTime/WorkTime.svg?style=for-the-badge
[issues-url]: https://github.com/pyWorkTime/WorkTime/issues
[license-shield]: https://img.shields.io/github/license/pyWorkTime/WorkTime.svg?style=for-the-badge
[license-url]: https://github.com/pyWorkTime/WorkTime/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/linkedin_username
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 