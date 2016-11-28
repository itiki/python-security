#!/bin/bash

my_ip=$(ip route get 8.8.8.8 | awk '/8.8.8.8/ {print $NF}')
echo "{
    \"server\":$my_ip,
    \"server_port\":8333,
    \"local_address\":\"127.0.0.1\",
    \"local_port\":8334,
    \"password\":\"thi,
    \"method\":\"aes-256-cfb\"
}" > ./test.txt
