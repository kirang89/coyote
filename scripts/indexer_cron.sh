#!/usr/bin/env bash

CRON_DIR=/etc/cron.d
CRON_FILE=indexer

touch $CRON_DIR/$CRON_FILE
echo "*/2 * * * * root ~/path/to/indexer.py" >> $CRON_DIR/$CRON_FILE
echo "Indexer job created"
