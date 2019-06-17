from __future__ import print_function
def lambda_handler(event, context):

    # Send post authentication data to Cloudwatch logs
    print ("Trigger function =", event['triggerSource'])
    if event['userName'] !="" :
        # TODO: write code...
        print ("User authentication in progress : User ID = ", event['userName'])
    elif event['callerContext']['clientId'] !="" :
        print ("Application authentication in progress : App client ID = ", event['callerContext']['clientId'])  
    else:
        print ("Unkown authentication format : ", event)  

    # Return to Amazon Cognito
    return event
