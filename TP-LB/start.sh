#!/bin/bash 

echo "Création Docker "

docker network create tplb 

docker build -t im-nginx-lb ./tp-A

mkdir -p shared1 shared2

echo "Création des fichiers index.html"

echo "<h1> Hello 1 </h1>" > shared1/index.html
echo "<h1> Hello 2 </h1>" > shared2/index.html

docker run -d --rm \
	--name nginx1 \
	--network tplb -p 81:80 \
    -v "$(pwd)/shared1:/usr/share/nginx/html" \
	nginx

docker run -d --rm \
	 --name nginx2 \
	--network tplb -p 82:80 \
    -v "$(pwd)/shared2:/usr/share/nginx/html" nginx


docker run -d --rm \
	--name nginx-lb \
	--network tplb -p 83:80 \
	im-nginx-lb
	for ((i=0;i<500;i++));do curl localhost:83;done:
		if [[ $resp == *"Hello 1"* ]]; then
        ((count1++))
    	elif [[ $resp == *"Hello 2"* ]]; then
        ((count2++))
    	fi
	done 

