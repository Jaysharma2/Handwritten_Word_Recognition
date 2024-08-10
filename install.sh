
# Install Virtual environment
virtualenv venv
source venv/bin/activate


# Install All the dependencies
pip install pandas
pip install pybind11
pip install fastwer

# Update the Submodule and Initialize
git submodule init --update

# Install Submodule dependencies
pip install -e ./doctr/.
pip install -e ./doctr/.[torch]
cd ./doctr/
pip install -r ./references/requirements.txt
cd ..