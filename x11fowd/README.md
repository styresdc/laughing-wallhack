# Problem
We want to be able to play audio over an ssh connection between linux boxes.

# Question
1. What will this include?
2. How will we setup?
3. Interacting via the end user.

# Resources
1. [Sound Is Confusing]
2. [Headless Setup]

### Mini-Abstract and relevance of [Sound Is Confusing]
SSH allows for connections to remote machines over the interne; the main advantage being stuctured source contorl and the ability for non UNIX systems to be able to build and develop code. In our case, while python and its related tasks may be run on a windows enviroment, at times it suits the developer to use a UNIX enviroment for development. 
The issue in our music example being that with many users operating on the same development system, we would all not have physical access to the system which would be required for local sound processing. This setup will allow for sound forwarding over a network connection with the use of pulse-audio, and x11 forwarding. 

It's finckey at best especially over WAN but should work flawless over LAN. Another option is to use VNC.

### 2. How will we setup
This setup involves the use of pulseaudio, a realativlety easy setup.

Assuming pulseaudio is already setup on both machines, and is configured to use the sound card on the server:

We need to enable some networking properties in 

```bash
$ paprefs
```

![alt text](http://i.stack.imgur.com/glDuy.png)

![alt text](http://i.stack.imgur.com/pdMMO.png)

These settings allow both sound sources and sinks to be published over the network, ideally to another pulseaudio server.

In case you have your server setup without desktop manager you will need to install a sound system first ([setup]). You can then edit /etc/pulse/default.pa uncommenting these lines in the Network access section:

load-module module-esound-protocol-tcp
load-module module-native-protocol-tcp
load-module module-zeroconf-publish

finally we need to start the audio daemon

```bash
$ start-pulseaudio-x11
```


### 3. User Setup
For the user, all we then need to do is open our pulseaudio local configuration and set ourselves to be locally availiable in paprefs the same way as before.

All following x11 sessions in which you want audio should have the format

```bash
$ ssh user@server -X
```
After which audio should play through local speakers


### Resources 

http://colin.guthr.ie/2009/08/sound-on-linux-is-confusing-defuzzing-part-2-pulseaudio/
http://askubuntu.com/questions/28176/how-do-i-run-pulseaudio-in-a-headless-server-installation
http://askubuntu.com/q/28176/3940

[Sound Is Confusing]: http://colin.guthr.ie/2009/08/sound-on-linux-is-confusing-defuzzing-part-2-pulseaudio/
[Headless Setup]: http://askubuntu.com/questions/28176/how-do-i-run-pulseaudio-in-a-headless-server-installation
[setup]: http://askubuntu.com/q/28176/3940
