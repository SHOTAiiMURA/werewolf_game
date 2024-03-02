import json

def lambda_handler(event, context):
    # TODO implement
    x=event["queryStringParameters"]["key"]
    try:

              # try converting to integer

        int(x)
        return {
            'statusCode': 200,
            'body': json.dumps(str(int(x)*int(x)))
        }
    except ValueError:

           
        return {
            'statusCode': 400,
            'body': json.dumps("invalid number")
        }
