WORK_DIR=$(dirname $(dirname $0))
cd $WORK_DIR

docker build -f ./api/backend-api.Dockerfile -t backend-api ./api