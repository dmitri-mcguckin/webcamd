# octoprint-stuff

octoprint-stuff is a collection of bits and bobs that make running Octoprint
a tad easier.

The most notable component is webcam.py.  It is a minimalist drop-in replacement
for mjpg-streamer, written in python, that addresses the following issues:

* Octoprint appends a seemingly-random session ID to the camera URI, which confuses the hell out of mjpg-streamer,
* mjpg-streamer doesn’t appear to handle multiple simultaneous streams, resulting in the infuriating “403: Forbidden! frame already sent” error,
* mjpg-streamer itself is complete overkill here.

webcam.py is based on Igor Maculan’s “Simple Python Motion Jpeg” daemon (https://gist.github.com/n3wtron/4624820).  It has been reworked to run under python-3.x, accept command-line tunables, IPv6 support, and so forth.

Please note that the webcam.py process needs read/write access to the video device (typically /dev/video0).  Adding the user that webcam.py runs as to the "video" group will usually suffice.

webcam@.service is a systemd unit file for webcam.py.

haproxy.cfg is a configuration file for haproxy that actually works with non-ancient versions of haproxy, and enforces SSL connections to Octoprint.

