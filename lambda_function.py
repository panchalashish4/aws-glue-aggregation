from generate_mock_data import generate_data
from upload_to_s3 import upload_to_s3
from create_rds_schema import connect_and_create_db
from datetime import date, timedelta

# Define date range (modify as needed)
start_date = date(2024, 3, 18)  # Adjust start date
end_date = date.today()


def lambda_handler(event, context):
    for current_date in range((end_date - start_date).days + 1):
        # Generate Data
        date_str = str(start_date + timedelta(days=current_date))
        generate_data(start_date, end_date, date_str)
        # Upload the generated CSV to S3
        upload_to_s3(f"transactions_{date_str}.csv", date_str)

    # Connect to RDS, create customers database and customer_transactions table
    connect_and_create_db()
    return


lambda_handler('', date.today())
