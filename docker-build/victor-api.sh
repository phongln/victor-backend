WORK_DIR=$(dirname $(dirname $0))
cd $WORK_DIR

docker build -f ./api/Dockerfile -t victor-api ./api

