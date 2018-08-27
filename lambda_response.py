# Michael Zarate via acloud.guru
def lambda_handler(event, context):
    print("In lambda handler")

    response = {
        "statusCode": 200,
        "headers": {
            "Access-Controll-Allow-Origin": "*",
        },
        "body": "Michael Zarate"
    }

    return response