ffmpeg -stream_loop -1 -re -i v.mp4 \
-c:v libx264 -preset veryfast -maxrate 3000k -bufsize 6000k \
-c:a aac -b:a 128k \
-f flv rtmp://a.rtmp.youtube.com/live2/c7bb-s6p5-8prx-dyxs-4g6w
