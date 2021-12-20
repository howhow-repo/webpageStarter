export DISPLAY=:0
xset s off
xset s noblank
xdotool mousemove 0 0
python /usr/src/initWebWhenBoot/main.py &
unclutter -idle 0.1 -root

// xset -dpms
// chromium-browser --start-fullscreen https://www.cwb.gov.tw/V8/C/ 
