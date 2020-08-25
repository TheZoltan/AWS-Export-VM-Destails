import sys
import json
import boto3
Version = '1.0'


# Start here
def main():
    print('AWS get VM details  v', Version)

    getListofVMs()



def getListofVMs():
    ec2 = boto3.resource('ec2')
    client = boto3.client('ec2')


    print('Retrieving AWS Tags...')

    for instance in ec2.instances.all():
        print(instance.tags)


    result = client.describe_subnets()

    var_list = []
    for i in result['Subnets']:
        var_list.append(
            {
                'EntryType': 'subnet',
                'CidrBlock': str(i['CidrBlock']),
                'AvailabilityZone': str(i['AvailabilityZone']),
                'AvailabilityZoneId': str(i['AvailabilityZoneId']),
                'SubnetId': str(i['SubnetId']),
                'VpcId': str(i['VpcId']),
                'SubnetArn': str(i['SubnetArn']),
                'AvailableIpAddressCount': i['AvailableIpAddressCount'],
                'Tags': str(i.get('Tags', 'No Tags Exist'))
            })

    for v in var_list:
        print('Subnet: ', v)

    # List Network Security Groups
    sec_grps = []
    sec_grps = client.describe_security_groups()

    print('SecGrp: ', sec_grps)

    # Get config of this security group
    print('\nIterating through list / dict: ')
    for key, value in sec_grps.items():
        #print('Key: ', key, ' Value: ', value)

        if (key == 'SecurityGroups'):
            for sg_rec in value:
                #print('Key: ', sg_rec)

                for name, setting in sg_rec.items():
                    print(name, ' -->  ', setting)



# Call main
if __name__ == '__main__':
    main()