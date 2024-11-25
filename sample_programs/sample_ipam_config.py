import sys
sys.path.append("../src")

import logging
import ipam.models as models
from typing import Optional
from ipam.api import NewApiClient 
from ipam.models import (
     IPSpace,
     AddressBlock,
     ASMConfig,
     Subnet,
     ExclusionRange,
     Range,
     FixedAddress,
     Address,
     IpamHost,
     HostAddress,
     OptionSpace,
     OptionGroup,
     OptionCode
)
 

def create_ip_sapce(api_client:NewApiClient,name:str)-> Optional[IPSpace]:
     """Creates an IP Space"""
     return api_client.ip_space_api.create(
          body=IPSpace(name=name)
     )

def create_address_block(api_client:NewApiClient,address:str,cidr:int,asm_config:ASMConfig,space:str)->Optional[AddressBlock]:
     """Creates Address Block"""
     return api_client.address_block_api.create(
          body=AddressBlock(address=address,cidr=cidr,asm_config=asm_config,space=space)
     )


def create_subnet(api_client:NewApiClient,address:str,cidr:int,space:str)->Optional[Subnet]:
     """Creates a Subnet"""
     return api_client.subnet_api.create(
          body=Subnet(address=address,cidr=cidr,space=space)
     )

def create_range(api_client:NewApiClient,space:str,start:str,end:str,name:str,exclusion_ranges:ExclusionRange)->Optional[Range]:
     """Creates a Range"""
     return api_client.range_api.create(
          body=Range(space=space,start=start,end=end,name=name,exclusion_ranges=[exclusion_ranges])
     )

def create_fixed_address(api_client:NewApiClient,ip_space:str,address:str,match_type:str,match_value:str)->Optional[FixedAddress]:
     """Creates a Fixed Address"""
     return api_client.fixed_address_api.create(
          body=FixedAddress(ip_space=ip_space,address=address,match_type=match_type,match_value=match_value)
     )

def create_reservation(api_client:NewApiClient,address:str,space:str,comment:str)->Optional[Address]:
     """Creates a Reservation"""
     return api_client.address_api.create(
          body=Address(address=address,space=space,comment=comment)
     )

def create_ipam_host(api_client:NewApiClient,name:str,addresses:HostAddress)->Optional[IpamHost]:
     """Creates a Ipam Host"""
     return api_client.ipam_host_api.create(
          body=IpamHost(name=name,addresses=[addresses])
     )

def create_option_space(api_client:NewApiClient,name:str,protocol:str)->Optional[OptionSpace]:
     """Creates a Option Space"""
     return api_client.option_space_api.create(
          body=OptionSpace(name=name,protocol=protocol)
     )

def create_option_code(api_client:NewApiClient,code:int,name:str,option_space:str,type:str)->Optional[OptionCode]:
     """Creates a Option Code"""
     return api_client.option_code_api.create(
          body=OptionCode(code=code,name=name,option_space=option_space,type=type)
     )

def create_option_group(api_client:NewApiClient,name:str,protcol:str)->Optional[OptionGroup]:
     """Creates a Option group"""
     return api_client.option_group_api.create(
          body=OptionGroup(name=name,protocol=protcol)
     )

def cleanup_resources(api_client: NewApiClient, resource_ids: list):
    """Deletes created resources for cleanup."""
    resource_ids.reverse()
    for resource_type, resource_id in resource_ids:
        try:
            getattr(api_client, f"{resource_type}_api").delete(resource_id)
            logging.info(f"Deleted {resource_type} with ID: {resource_id}")
        except Exception as e:
            logging.error(f"Failed to delete {resource_type} with ID {resource_id}: {e}")

def sample_ipam():
    """Runs a sample IPAM configuration process."""

    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
    api_client = NewApiClient()
    resource_ids = []

    try:
        ip_space_response=create_ip_sapce(api_client,"example_ip_space")
        if ip_space_response: 
            resource_ids.append(("ip_space", ip_space_response.result.id))
            logging.info("IP Space created successfully")

        address_block_response=create_address_block(api_client,"192.168.0.0",16,ASMConfig(
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
                ip_space_response.result.id
            )
        if ip_space_response: 
            resource_ids.append(("address_block", address_block_response.result.id))
            logging.info("Address Block created successfully")

        
        subnet_response=create_subnet(api_client,"192.168.1.0",24,ip_space_response.result.id)
        if subnet_response: 
            resource_ids.append(("subnet", subnet_response.result.id))
            logging.info("Subnet created successfully")
   
        range_response=create_range(api_client,ip_space_response.result.id,"192.168.1.15","192.168.1.30","example",ExclusionRange(
                            start = "192.168.1.17",
                            end = "192.168.1.20"
                            ))
                
        if range_response: 
            resource_ids.append(("range", range_response.result.id))
            logging.info("Range created successfully")   


        fixed_address_response=create_fixed_address(api_client,ip_space_response.result.id,"192.168.1.10","mac","00:00:00:00:00:00")
        if fixed_address_response: 
            resource_ids.append(("fixed_address", fixed_address_response.result.id))
            logging.info("Fixed Address created successfully") 

        reservation_response=create_reservation(api_client,"192.168.1.1",ip_space_response.result.id,"reservation for Site A")
        if reservation_response: 
            logging.info("Reservation created successfully") 

        ipam_host_response=create_ipam_host(api_client,"example_ipam_host",HostAddress(
                        address="192.168.1.1",
                        space=ip_space_response.result.id
                    ))
        if ipam_host_response: 
            resource_ids.append(("ipam_host", ipam_host_response.result.id))
            logging.info("IPAM Host created successfully")        


        option_space_response=create_option_space(api_client,"example_dhcp_option_space",protocol="ip4")
        if option_space_response: 
            resource_ids.append(("option_space", option_space_response.result.id))
            logging.info("Option Space created successfully") 
        

        option_code_response=create_option_code(api_client,251,"example_option_code",option_space_response.result.id,"int32")
        if option_code_response: 
            resource_ids.append(("option_code", option_code_response.result.id))
            logging.info("Option Code created successfully") 


        option_group_response=create_option_group(api_client,"example_option_group","ip4")
        if option_group_response: 
            resource_ids.append(("option_group", option_group_response.result.id))
            logging.info("Option Group created successfully")

    except Exception as e:
        logging.error(f"Error occurred: {e}")

    finally:
        cleanup_resources(api_client, resource_ids)


if __name__ == "__main__":
    sample_ipam()