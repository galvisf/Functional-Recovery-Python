# -*- coding: utf-8 -*-
"""
Code for generating optional_inputs.json file

"""

import json
optional_inputs = {
# impedance Options
"impedance_options" : {
    
    
"include_impedance":       {
                            "inspection" : True,
                            "financing" : True,
                            "permitting" : True,
                            "engineering" : True,
                            "contractor" : True
                            },
"system_design_time" :      {
                            "f" : 0.04,
                            "r" : 175,
                            "t" : 1.3,
                            "w" : 8
                            },
"mitigation"  :             {
                            "is_essential_facility" : False,
                            "is_borp_equivalent" : False,
                            "is_engineer_on_retainer" : False,
                            "is_contractor_on_retainer" : False,
                            "funding_source" : 'private',
                            "capital_available_ratio" : 0.1
                            },
"impedance_beta" : 0.6,
"impedance_truncation" : 2                
                            },
                      

# Repir Schedule Options
"repair_time_options" : {
                        "temp_repair_beta" : 0.6,
                        "max_workers_per_sqft_story"  : 0.001,
                        "max_workers_per_sqft_building" : 0.00025,
                        "max_workers_building_min" :  20,
                        "max_workers_building_max" :  260
                       },

# Functionality Assessment Options
"functionality_options" : {
                       "door_racking_repair_day" : 3,
                       "egress_threshold" : 0.5,
                       "egress_threshold_wo_fs" : 0.75,
                       "required_ratio_operating_hvac_main" : 0.6667,
                       "required_ratio_operating_hvac_unit" : 0.6667,
                       "exterior_safety_threshold" : 0.1,
                       "interior_safety_threshold" : 0.25,
                       "door_access_width_ft" : 9
                       },

# Regional Impact
"regional_impact" : {
                    "surge_factor" : 1}
}

with open("optional_inputs.json", "w") as outfile:
    json.dump(optional_inputs, outfile)
   
