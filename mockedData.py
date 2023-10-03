# fetch all claims
data1 = {
    "usecase_desc": "All Claims Status from the state of CA",
    "response_data":
    {
      "metrics": 
        [
            {
                "xvalue": "Approved",
                "yvalue": "8",
                "zvalue": None,
            },
            {
                "xvalue": "Denied",
                "yvalue": "9",
                "zvalue": None,
            },
            {
                "xvalue": "Denied Then Paid",
                "yvalue": "5",
                "zvalue": None,
            }
      ],
      "insights": ["Your approved claims rate increased by X% compared to last year"]
    }
}

# fetch all claims from the state of NY
data2 = {
    "usecase_desc": "All Claims Status from the state of NY",
    "response_data":
    {
      "metrics": 
        [
            {
                "xvalue": "Approved",
                "yvalue": "8",
                "zvalue": None,
                "raw_data": [
                    {
                        "claim_date": "2020-01-01",
                    },
                    {
                        "claim_date": "2020-02-02",
                    },
                    {
                        "claim_date": "2020-03-01",
                    },
                    {
                        "claim_date": "2020-04-01",
                    },
                    {
                        "claim_date": "2020-05-01",
                    },
                    {
                        "claim_date": "2020-07-01",
                    },
                    {
                        "claim_date": "2020-08-01",
                    },
                    {
                        "claim_date": "2020-09-01",
                    },
                ]
            },
            {
                "xvalue": "Denied",
                "yvalue": "9",
                "zvalue": None,
                 "raw_data": [
                    {
                        "claim_date": "2020-01-01",
                    },
                    {
                        "claim_date": "2020-02-02",
                    },
                    {
                        "claim_date": "2020-03-01",
                    },
                    {
                        "claim_date": "2020-04-01",
                    },
                    {
                        "claim_date": "2020-05-01",
                    },
                    {
                        "claim_date": "2020-06-01",
                    },
                    {
                        "claim_date": "2020-07-01",
                    },
                    {
                        "claim_date": "2020-08-01",
                    },
                    {
                        "claim_date": "2020-09-01",
                    },
                ]
            },
            {
                "xvalue": "Denied Then Paid",
                "yvalue": "5",
                "zvalue": None,
                 "raw_data": [
                    {
                        "claim_date": "2020-01-01",
                    },
                    {
                        "claim_date": "2020-02-02",
                    },
                    {
                        "claim_date": "2020-03-01",
                    },
                    {
                        "claim_date": "2020-04-01",
                    },
                    {
                        "claim_date": "2020-05-01",
                    },
                ]
            }
      ],
      "insights": ["Your approved claims rate increased by X% compared to last year"]
    }
}

# fetch all claims from the state of NY and CA
data3 = {
    "usecase_desc": "All Claims Status from the state of NY and CA",
    "response_data":
    {
      "metrics": 
        [
            {
                "xvalue": "Approved",
                "yvalue": "8",
                "zvalue": "NY",
                "raw_data": [
                    {
                        "claim_date": "2020-01-01",
                    },
                    {
                        "claim_date": "2020-02-02",
                    },
                    {
                        "claim_date": "2020-03-01",
                    },
                    {
                        "claim_date": "2020-04-01",
                    },
                    {
                        "claim_date": "2020-05-01",
                    },
                    {
                        "claim_date": "2020-07-01",
                    },
                    {
                        "claim_date": "2020-08-01",
                    },
                    {
                        "claim_date": "2020-09-01",
                    },
                ]
            },
            {
                "xvalue": "Denied",
                "yvalue": "9",
                "zvalue": "NY",
                 "raw_data": [
                    {
                        "claim_date": "2020-01-01",
                    },
                    {
                        "claim_date": "2020-02-02",
                    },
                    {
                        "claim_date": "2020-03-01",
                    },
                    {
                        "claim_date": "2020-04-01",
                    },
                    {
                        "claim_date": "2020-05-01",
                    },
                    {
                        "claim_date": "2020-06-01",
                    },
                    {
                        "claim_date": "2020-07-01",
                    },
                    {
                        "claim_date": "2020-08-01",
                    },
                    {
                        "claim_date": "2020-09-01",
                    },
                ]
            },
            {
                "xvalue": "Approved",
                "yvalue": "8",
                "zvalue": "NY",
                "raw_data": [
                    {
                        "claim_date": "2020-01-01",
                    },
                    {
                        "claim_date": "2020-02-02",
                    },
                    {
                        "claim_date": "2020-03-01",
                    },
                    {
                        "claim_date": "2020-04-01",
                    },
                    {
                        "claim_date": "2020-05-01",
                    },
                    {
                        "claim_date": "2020-07-01",
                    },
                    {
                        "claim_date": "2020-08-01",
                    },
                    {
                        "claim_date": "2020-09-01",
                    },
                ]
            },
            {
                "xvalue": "Denied Then Paid",
                "yvalue": "5",
                "zvalue": "NY",
                 "raw_data": [
                    {
                        "claim_date": "2020-01-01",
                    },
                    {
                        "claim_date": "2020-02-02",
                    },
                    {
                        "claim_date": "2020-03-01",
                    },
                    {
                        "claim_date": "2020-04-01",
                    },
                    {
                        "claim_date": "2020-05-01",
                    },
                ]
            },
            {
                "xvalue": "Approved",
                "yvalue": "6",
                "zvalue": "CA",
                "raw_data": [
                    {
                        "claim_date": "2020-01-01",
                    },
                    {
                        "claim_date": "2020-02-02",
                    },
                    {
                        "claim_date": "2020-03-01",
                    },
                    {
                        "claim_date": "2020-07-01",
                    },
                    {
                        "claim_date": "2020-08-01",
                    },
                    {
                        "claim_date": "2020-09-01",
                    },
                ]
            },
                        {
                "xvalue": "Denied",
                "yvalue": "11",
                "zvalue": "CA",
                 "raw_data": [
                    {
                        "claim_date": "2020-01-01",
                    },
                    {
                        "claim_date": "2020-02-02",
                    },
                    {
                        "claim_date": "2020-03-01",
                    },
                    {
                        "claim_date": "2020-04-01",
                    },
                    {
                        "claim_date": "2020-05-01",
                    },
                    {
                        "claim_date": "2020-06-01",
                    },
                    {
                        "claim_date": "2020-07-01",
                    },
                    {
                        "claim_date": "2020-08-01",
                    },
                    {
                        "claim_date": "2020-09-01",
                    },
                    {
                        "claim_date": "2020-08-01",
                    },
                    {
                        "claim_date": "2020-09-01",
                    },
                ]
            },
            {
                "xvalue": "Denied Then Paid",
                "yvalue": "6",
                "zvalue": "CA",
                 "raw_data": [
                    {
                        "claim_date": "2020-01-01",
                    },
                    {
                        "claim_date": "2020-02-02",
                    },
                    {
                        "claim_date": "2020-03-01",
                    },
                    {
                        "claim_date": "2020-04-01",
                    },
                    {
                        "claim_date": "2020-05-01",
                    },
                    {
                        "claim_date": "2020-10-01",
                    },
                ]
            },
      ],
      "insights": ["Your approved claims rate increased by X% compared to last year"]
    }
}

mockData = {
  "NY": {
      "Approved" : ['11/1/22','7/1/22','2/1/22','2/1/23'],
      "Denied" : ['11/2/22','2/1/23','4/1/23','5/1/23'],
      "Denied Then Paid" : ['3/2/22','7/2/22','3/2/22','2/2/23','11/2/22']
  },
  "CA": {
      "Approved" : ['12/2/22','11/2/22','4/1/23'],
      "Denied" : ['2/1/22','3/1/22','7/2/22','12/2/22','3/2/23'],
      "Denied Then Paid" : ['5/1/23','1/1/23','2/1/22','7/1/22']
  },
  "CO": {
      "Approved" : ['3/2/22','12/2/22'],
      "Denied" : ['1/1/22','2/1/22'],
      "Denied Then Paid" : ['2/1/23','4/1/23']
  },
  "NV": {
      "Approved" : ['3/2/22'],
      "Denied" : ['1/1/22'],
      "Denied Then Paid" : ['2/1/23']
  },
  "OH": {
      "Approved" : ['5/1/23','12/2/22','11/2/22','11/2/22'],
      "Denied" : ['11/2/22','2/1/22','2/1/22','2/1/22'],
      "Denied Then Paid" : ['2/1/22','4/1/23','5/1/23','5/1/23']
  }
}

mockDataNewWireframe1 = {
    "response_desc": "",
    "response_data": {
        "metrics": [
            {
                "xvalue": "Approved",
                "yvalue": 3,
                "zvalue": "CA"
            },
            {
                "xvalue": "Denied",
                "yvalue": 5,
                "zvalue": "CA"
            },
            {
                "xvalue": "Denied Then Paid",
                "yvalue": 4,
                "zvalue": "CA"
            },
            {
                "xvalue": "Approved",
                "yvalue": 2,
                "zvalue": "CO"
            },
            {
                "xvalue": "Denied",
                "yvalue": 2,
                "zvalue": "CO"
            },
            {
                "xvalue": "Denied Then Paid",
                "yvalue": 2,
                "zvalue": "CO"
            },
            {
                "xvalue": "Approved",
                "yvalue": 1,
                "zvalue": "NV"
            },
            {
                "xvalue": "Denied",
                "yvalue": 1,
                "zvalue": "NV"
            },
            {
                "xvalue": "Denied Then Paid",
                "yvalue": 1,
                "zvalue": "NV"
            },
            {
                "xvalue": "Approved",
                "yvalue": 4,
                "zvalue": "NY"
            },
            {
                "xvalue": "Denied",
                "yvalue": 4,
                "zvalue": "NY"
            },
            {
                "xvalue": "Denied Then Paid",
                "yvalue": 5,
                "zvalue": "NY"
            },
            {
                "xvalue": "Approved",
                "yvalue": 4,
                "zvalue": "OH"
            },
            {
                "xvalue": "Denied",
                "yvalue": 4,
                "zvalue": "OH"
            },
            {
                "xvalue": "Denied Then Paid",
                "yvalue": 4,
                "zvalue": "OH"
            }
        ],
        "insights": None
    }
}

mockDataNewWireframe2 = {  
    "response_desc": "Trend_Analysis_Amounts",  
    "response_data": {    
        "metrics": [      
            {        
                "s1value": 0,        
                "s2value": 96860,        
                "s3value": 0,   
                "datevalue": "August"      
            },      
            {        
                "s1value": 7585800,        
                "s2value": 392330933,        
                "s3value": 0,        
                "datevalue": "July"       
            },      
            {        
                "s1value": 2418871,        
                "s2value": 612506382,        
                "s3value": 0,        
                "datevalue": "June"       
            },      
            {        
                "s1value": 10650350,        
                "s2value": 300507302,        
                "s3value": 0,
                "datevalue": "May"       
            }
    ],
    "variables": ['s1value', 's2value', 's3value'],
    "insights": None   }
}

mockDataNewWireframe2 = {  
    "response_desc": "Trend_Analysis_Amounts",  
    "response_data": {    
        "metrics": [      
            {        
                "paidAmountAdj": 0,        
                "totalChargeAmountAdj": 96860,        
                "interestAmountAdj": 0,   
                "claimCompletionMonth": "August"      
            },      
            {        
                "paidAmountAdj": 7585800,        
                "totalChargeAmountAdj": 392330933,        
                "interestAmountAdj": 0,        
                "claimCompletionMonth": "July"       
            },      
            {        
                "paidAmountAdj": 2418871,        
                "totalChargeAmountAdj": 612506382,        
                "interestAmountAdj": 0,        
                "claimCompletionMonth": "June"       
            },      
            {        
                "paidAmountAdj": 10650350,        
                "totalChargeAmountAdj": 300507302,        
                "interestAmountAdj": 0,
                "claimCompletionMonth": "May"       
            }
    ],
    "variables": ['paidAmountAdj', 'totalChargeAmountAdj', 'interestAmountAdj'],
    "insights": None   }
}