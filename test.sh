#!/usr/bin/env bash

END_POINT_URL="http://192.168.49.2:30001/ping"

for x in $(seq 2000);
do
    echo "# Request: ${x}"
    curl "${END_POINT_URL}" | json_pp
    sleep 0.1
done
