title: Self-hosting
date: 2020-09-06
modified: 2020-09-07

Okay, so at the bottom of this page there should be a picture that describes my setup, but to recap in text:

1. Internet comes into the house at the ISP modem. All incoming traffic meant for my services is forwarded to my own modem, where I can control
it better.
2. All external traffic is routed to the [nginx proxy manager](https://nginxproxymanager.com/), a so called *reverse proxy*, which decides where 
incoming network traffic should end up. So for instance [swnkls.nl](https://swnkls.nl) should end up in the nginx web server, while
[photo.swnkls.nl](https://photo.swnkls.nl/) should end up at pigallery. This also filters out most automated
attacks on my servers (as raw IP addresses with port number do not connect to anything anymore).
3. There are two main devices, the QNAP NAS (which I call *Helderder*), and my Raspberry Pi 4 (called *Aagje*). I use the build-in QNAP
suit as I would use the online part of Dropbox or Google Drive (only with more options and storage). [Syncthing](https://syncthing.net/) 
is used to actually sync folderd to my laptop/phone/whatever, but also between the two devices. The NAS is the 'main' storage for all of my data
but the important stuff is mirrored live to Aagje using Syncthing, so in case of a drive failure, I don't loose anything important. The NAS also does a weekly backup to
'regular' external hard drives.
4. The rest of the services I try to run in [Docker](https://www.docker.com/). Docker is a clever bit of software that basically creates a little
box on your computer called a *container* where another programme lives. The nice thing about this is that this software cannot be influenced
by other programmes on the same computer, and it does not care about the type of computer you are running it on. The programme can
only see the inside of the box, and should therefore not care (or hardly care) on what type of computer you run it. Best of all, people who
make software often also create a container with their software in it, ready to go. Meaning I need to do very little complex setup.
5. I run several services for myself (apart from the aforementioned Syncthing and Nginx proxy manager), on both Aagje and Helderder. Due
to the magic of Docker, it is not really important where these programs run exactly.
    * [Pigallery2](https://bpatrik.github.io/pigallery2/), a self-hosted clone of Google Photos basically.
    * [Jellyfin](https://jellyfin.org/), Netflix, but for your own movies.
    * [Recipes](https://github.com/vabene1111/recipes), basically a digital recipe book, where you can add notes, collect recipes from other sources,
    etc..
    * [Gitea](https://gitea.io/en-us/), a personal git server.
    * [Dokuwiki](https://www.dokuwiki.org/dokuwiki), a personal wikipedia, where you can put random knwoledge in an ordered way. Usefull for things you
    forget how to do every year.
    * [Transmission](https://transmissionbt.com/), to download files via a torrent (Linux ISOs, etc.) to my NAS, so these huge files do not clutter my tiny laptop
    memory.
    * [Pyload](https://pyload.net), same as transmission, but for regular downloads. Put in the link, and it will download. Usefull for big files, software, whatever.
    * [Nginx web server](https://www.nginx.com/), to serve you this website (and others).
  
Just a warning, before you trust all this information, this setup changes pretty much all the time (otherwise it would not be much of a hobby of course). Take what you
see here as a snapshot of the systems I have in place, which may or may not be very up to date.


![Network setup]({static}/images/network-setup.png "Network setup")


In this image, purple lines are physical internet cables, green lines are shared data, black lines indicate programmes that run on the machine, blue lines indicate applications
that run in a docker container.
