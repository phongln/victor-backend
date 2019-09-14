WORK_DIR=$(dirname $(dirname $0))
cd $WORK_DIR

docker build -f ./nginx/Dockerfile -t victor-nginx ./nginx