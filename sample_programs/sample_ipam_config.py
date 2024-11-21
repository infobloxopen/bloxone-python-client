import sys
sys.path.append("../src")

import ipam.models as models
from ipam.api import NewApiClient  
 

def sample_ipam():
    api_client = NewApiClient()

    try:
        ip_space_response=api_client.ip_space_api.create(
            body=models.IPSpace(
                name="example_ip_space"
            )
        )
        if ip_space_response is not None :
            print("IP Space Created")
        else:
            raise Exception("IP Space not created")

        address_block_response=api_client.address_block_api.create(
            body=models.AddressBlock(
                address="192.168.0.0",
                cidr=16,
                asm_config=models.ASMConfig(
                    asm_threshold       = 90,
                    enable              = True,
                    enable_notification = True,
                    forecast_period     = 10,
                    growth_factor       = 10,
                    growth_type         = "percent",
                    history             = 30,
                    min_total           = 2,
                    min_unused          = 10,
                    reenable_date       = "2024-01-24T10:10:00+00:00"
                ),
                space=ip_space_response.result.id
            )
        )
        if address_block_response is not None :
            print("Address Block Created")
        else:
            raise Exception("Address Block not created")
        
        subnet_response=api_client.subnet_api.create(
            body=models.Subnet(
                address="192.168.1.0",
                cidr=24,
                space=ip_space_response.result.id
            )
        )

        if subnet_response is not None :
            print("Subnet Created")
        else:
            raise Exception("Subnet not created")
        
        range_response=api_client.range_api.create(
            body=models.Range(
                space=ip_space_response.result.id,
                start = "192.168.1.15",
                end   = "192.168.1.30",
                name="example",
                exclusion_ranges = [
                        models.ExclusionRange(
                            start = "192.168.1.17",
                            end   = "192.168.1.20"
                )
            ])
        )

        if range_response is not None:
            print("Range created")
        else:
            raise Exception("Range not created")
        
        fixed_address_response=api_client.fixed_address_api.create(
            body=models.FixedAddress(
                ip_space=ip_space_response.result.id,
                address="192.168.1.10",
                match_type="mac",
                match_value="00:00:00:00:00:00"
            )
        )

        if fixed_address_response is not None:
            print("Fixed Address created")
        else:
            raise Exception("Fixed Address not created")

        reservation_response=api_client.address_api.create(
            body=models.Address(
                address="192.168.1.1",
                space=ip_space_response.result.id,
                comment = "reservation for Site A"
            )
        )

        if reservation_response is not None:
                    print("Reservation created")
        else:
            raise Exception("Reservation not created")

        ipam_host_response=api_client.ipam_host_api.create(
            body=models.IpamHost(
                name="example_ipam_host",
                addresses=[
                    models.HostAddress(
                        address="192.168.1.1",
                        space=ip_space_response.result.id
                    )
                ])
        )

        if ipam_host_response is not None:
                    print("IPAM host created")
        else:
            raise Exception("IPAM host not created")

        option_space_response=api_client.option_space_api.create(
            body=models.OptionSpace(
                name="example_dhcp_option_space",
                protocol="ip4"
            )
        )

        if option_space_response is not None:
                    print("Option Space created")
        else:
            raise Exception("Option Space not created")

        option_code_response=api_client.option_code_api.create(
            body=models.OptionCode(
                code=251,
                name="example_option_code",
                option_space=option_space_response.result.id,
                type="int32"
            )
        )

        if option_code_response is not None:
                    print("Option Code created")
        else:
            raise Exception("Option Code not created")

        option_group_response=api_client.option_group_api.create(
            body=models.OptionGroup(
                name="example_option_group",
                protocol="ip4"
            )
        )

        if option_group_response is not None:
                    print("Option Group created")
        else:
            raise Exception("Option Group not created")
       
        if option_group_response is not None:
            api_client.option_group_api.delete(option_group_response.result.id)
        if option_code_response is not None:
            api_client.option_code_api.delete(option_code_response.result.id)
        if option_space_response is not None:
            api_client.option_space_api.delete(option_space_response.result.id)
        if ipam_host_response is not None:
            api_client.ipam_host_api.delete(ipam_host_response.result.id)
        if range_response is not None:
            api_client.range_api.delete(range_response.result.id)
        if fixed_address_response is not None:
            api_client.fixed_address_api.delete(fixed_address_response.result.id)
        if subnet_response is not None:
            api_client.subnet_api.delete(subnet_response.result.id)
        if address_block_response is not None:
            api_client.address_block_api.delete(address_block_response.result.id)
        if ip_space_response is not None:
            api_client.ip_space_api.delete(ip_space_response.result.id)


        print("Done")
        
    except Exception as e:
        print(f"Error occurred: {str(e)}")


if __name__ == "__main__":
    sample_ipam()