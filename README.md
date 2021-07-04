# Chippy Buttons

Requires:
- [Circuit Python](https://circuitpython.readthedocs.io/projects/mpr121/en/latest/examples.html)
    - `pip3 instal adafruit-circuitpython-mpr121`
- [pydub](http://pydub.com)
    - `pip3 install pydub`
- [simpleaudio](https://pypi.org/project/simpleaudio/)
    - `pip3 install simpleaudio`
- ffmpeg
    - `apt install ffmpeg`

## How to install

Copy the systemd service file into location and enable it:
```sh
sh install.sh
```

## Check on status of service
```sh
systemctl status chippy-buttons.service
```

or

```sh
tail -f /home/pi/chippy-buttons.log
```