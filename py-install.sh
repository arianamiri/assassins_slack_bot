BASEDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

TARGET_DIR="$BASEDIR/target/"
SOURCE_DIR="$BASEDIR/src/"
REQUIREMENTS_FILE="$BASEDIR/requirements.txt"
VENV_DIR="$BASEDIR/venv"

if [ -d $TARGET_DIR ]; then
  rm -rf $TARGET_DIR
fi

mkdir $TARGET_DIR

if [ ! -d $VENV_DIR ]; then
  virtualenv venv
fi

source "$VENV_DIR/bin/activate"
  pip install -r requirements.txt -t $TARGET_DIR
deactivate

cp -r $SOURCE_DIR $TARGET_DIR
