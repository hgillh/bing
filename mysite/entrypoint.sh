#!/bin/sh

GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

# Check if DynamoDB has started
if [ "$DYNAMO_DB_HOST" = "http://dynamodb:8000" ]
then
  echo "${YELLOW}Waiting for DynamoDB server...${NC}"
  while ! nc -z $DYNAMO_DB_HOST; do
    sleep 0.1
  done
  echo "DynamoDB server [${GREEN}OK${NC}]"
else
  echo "${YELLOW}Skipping DynamoDB server waiting.${NC}"
fi

# Run Django migration
python manage.py migrate

exec "$@"