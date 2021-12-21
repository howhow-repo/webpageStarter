export DISPLAY=:0
xset s off
xset s noblank
xset -dpms
xdotool mousemove 0 0
python /usr/src/webpageStarter/main.py &
unclutter -idle 0.1 -root
