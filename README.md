# crud_app

#Steps to run program:
1) Install requirements.txt file using pip3 ```install -r requirements.txt``` command
2) Run ```uvicorn main:app --reload``` command to run project



#CRUD API
1) Create Address:
    - Method :  Post
    - Endpoint :  http://127.0.0.1:8000/address
    
    - Body: {
      "id": 9,
      "latitude": "25.594095",
      "longitude": "85.137566"
     }

     - Response:
     {
      "latitude": "25.594095",
      "longitude": "85.137566",
      "address_from_cordinates": null,
      "id": 9
     }
   
2) Update Address:
    - Method :  Put
    - Endpoint :   http://127.0.0.1:8000/address/{address_id}
    
    - Body: {
    "id": 9,
    "latitude": "89.099.232.111",
    "longitude": "25.099.232.111"
    }  

   - Response:
   {
    "latitude": "25.594095",
    "longitude": "85.137566",
    "address_from_cordinates": null,
    "id": 9
   }
   
   
3) Get Address details:
     - Method : Get
     
     - Endpoint :  http://127.0.0.1:8000/address

      - Response:
      {
      "limit": 10,
      "offset": 0,
      "data": [
          {
              "id": 10,
              "latitude": "25.594095",
              "longitude": "85.137566",
              "address_from_cordinates": null
          },
          {
              "id": 11,
              "latitude": "25.256095",
              "longitude": "89.137566",
              "address_from_cordinates": null
          }
        ]
  }

 
4) Delete Address:
  
  
    - Method: Delete
    - Endpoint :   http://127.0.0.1:8000/address/9
    
    - Response: {
      "message": "Address Deleted Successfully"
     }
  

   

   
   
   
