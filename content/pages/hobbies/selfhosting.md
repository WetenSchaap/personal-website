title: Self-hosting
date: 2020-09-06
modified: 2020-09-06

Okay, so below there is a picture that describes my setup, but to recap in text:
  1. Internet comes into the house at the ISP modem.
  2. The ISP modem is connected to my own modem, so I have better control
  3.  All external traffic is routed to the [nginx proxy manager](https://nginxproxymanager.com/), which decides where the
  traffic should end up. So for instance [swnkls.nl](https://swnkls.nl) should end up in the nginx web server, while
  [photo.swnkls.nl](https://photo.swnkls.nl/) should end up at pigallery. This also filters out most automated
  attacks on mys servers (as raw IP addresses with port number do not connect to anything anymore).
  4. There are two main devices, the QNAP NAS (which I call Helderder), and my Raspberry Pi 4 (4GB). I use the build-in QNAP
  suit as I would use the online part of Dropbox or Google Drive (only with a huge more options and storage). [Syncthing](https://syncthing.net/) 
  is used to actually sync folderd to my laptop/phone/whatever.
  5. The rest of the services I try to run in [Docker](https://www.docker.com/). Docker is a clever bit of software that basically creates a little
  box on your computer called a *container* where another programm lives, like a web server. The nice thing about this is that this siftware cannot be influenced
  by other programms on the same computer, and it does not care about the type of computer you are running it on. The programm can
  only see the inside of the box, and should therefore not care (or hardly care) on what type of computer you run it. Best of all, people who
  make software often also create a container with their software in it, ready to go. Meaning  I need to do very little complex setup.
  6. Okay, I should finnish this later!
  
Just a warning, befoire you trust all this, this setup changes pretty much all the time (otherwise it would not be much of a hobby of course). Take what you
see here as a snapshot of the systems I have in place, which may or may not be very up to date.
 ![Network setup]({static}/images/network-setup.png "Network setup")
