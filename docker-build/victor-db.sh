WORK_DIR=$(dirname $(dirname $0))
cd $WORK_DIR

docker build -t victor-db ./scripts