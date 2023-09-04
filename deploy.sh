
# Define your AWS Lambda function name
FUNCTION_NAME="FastApiPuffin"


# Create a virtual environment
python3 -m venv menv
source myenv/bin/activate

# Install your FastAPI application and its dependencies
pip install fastapi uvicorn
pip install -r requirements.txt  # Include any additional dependencies

# Create a deployment package directory
mkdir deployment_package

# Copy your FastAPI application code into the package
cp -r myenv/lib/python3.8/site-packages/* deployment_package/
cp -r app.py deployment_package/
cp -r database.py deployment_package/
cp -r routes/ deployment_package/

# Zip the deployment package
cd deployment_package
zip -r deployment_package.zip .

# Add our FastAPI files
zip lambda_function.zip -u app.py
zip lambda_function.zip -u database.py 
zip lambda_function.zip -u database.py 
