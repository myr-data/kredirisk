1. Build docker image:
    $ docker build -t credit-risk-api .

2. Run container:
    $ docker run --name credit-risk-container -p 8000:8000 credit-risk-api

3. output will contain:
INFO:   Uvicorn running on http://localhost:8000
    - use this url in chrome to see model frontend
    - use for testing the model

4. Query model

    4.1 Via web interface (chrome):
        http://localhost:8000/docs -> test model
    
    4.2 Via python client:
        client.py
    
    4.3 Via curl request:
        $ curl -X POST "http://localhost:8000/predict" \
        -H "Content-Type: application/json" \
        -d '{
        "person_age": 25,
        "person_income_log": 10.9,
        "person_home_ownership": "RENT",
        "person_emp_length": 3.0,
        "loan_intent": "EDUCATION",
        "loan_grade": "B",
        "loan_amnt": 5000,
        "loan_int_rate": 11.5,
        "loan_percent_income": 0.2,
        "cb_person_default_on_file": 0,
        "cb_person_cred_hist_length": 4
        }'

    4.4 Example response:
        {
        "prediction": 0,
        "probability": 0.24
        }

    4.5 Health check:
        $ curl http://localhost:8000/
    
    4.6 Response:
        {
        "status": "API running"
        }
    
    