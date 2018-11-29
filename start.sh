#!/bin/sh
/opt/sfc_flask/server.py
cd /opt/sfc/sfc-py
./start_agent.sh 127.0.0.1:8181 &
