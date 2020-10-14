from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny


# Create your views here.
@permission_classes([AllowAny])
class RegisterUser(APIView):

    def post(self, request):
        username = request.data.get("username", "")
        password = request.data.get("password", "")
        email = request.data.get("email", "")
        if not username or not password:  # or not email:  #not username and
            return Response(
                data={
                    "message": "Please enter username password"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        try:
            new_user = User.objects.create_user(username=username, password=password, email=email)
            new_user.save()
            return Response(data={"message":"User created"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(data={"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


@permission_classes([])
class CategoriesView(APIView):

    def get(self, request):
        return Response(
            data=
                [
                    {
                        "id": "86453728-139b-4ac5-8016-77229a62ba82",
                        "name": "Electrician"
                    },
                    {
                        "id": "bd736671-6865-4d74-9dfa-0e5f4be802d3",
                        "name": "Pharmacies"
                    },
                    {
                        "id": "bc5f4746-526b-452e-b64f-61164b9c6064",
                        "name": "Supermarkets"
                    },
                    {
                        "id": "dda057c6-e222-46ac-803e-9b3ba9cf6036",
                        "name": "Gas"
                    },
                    {
                        "id": "b03dd556-e6ea-457d-9d1b-a03c53b14aab",
                        "name": "Cafeteria"
                    }
                ],
            status=status.HTTP_200_OK
        )

@permission_classes([])
class ServicesView(APIView):
    def get(self, request):
        return Response(
			data = {
	"took": 4,
	"timed_out": False,
	"_shards": {
		"total": 5,
		"successful": 5,
		"failed": 0
	},
	"hits": {
		"total": 39,
		"max_score": "",
		"hits": [{
			"_index": "services-list",
			"_type": "service",
			"_id": "ff35f11d-0229-4c4a-82d1-e2c9e13718b4",
			"_score": "",
			"_source": {
				"name": "The hgeVDsbf",
				"providerId": "6b755e02-d84d-4313-b96a-6b786199cf4c",
				"providerName": "aravind.g@hashedin.com",
				"providerFirstName": "Aravind",
				"cat": "Banks-ATMs",
				"short_description": "Fhsfdhfhd",
				"rating": 0,
				"expire_after": "",
				"is_address_private": True,
				"keywords": ["Back"],
				"name_suggest": {
					"input": ["Back", "The", "hgeVDsbf", "The hgeVDsbf"],
					"output": "The hgeVDsbf",
					"payload": {
						"cat": "Banks-ATMs",
						"service_id": "ff35f11d-0229-4c4a-82d1-e2c9e13718b4"
					}
				},
				"views": 1,
				"media": [],
				"created_at": "2019-01-18 06:15:17.380172+00:00",
				"is_active": True,
				"is_blocked": False,
				"is_verified": False,
				"location": {
					"lat": "12.91237900000000",
					"lon": "77.64027600000000"
				}
			},
			"sort": [1.3563758331506583, "2019"]
		}, {
			"_index": "services-list",
			"_type": "service",
			"_id": "0d46210c-bba6-4903-a842-cbc16109eb7c",
			"_score": "",
			"_source": {
				"name": "Eat street",
				"providerId": "68dabf25-89ad-4237-a94e-b0e4d59a346a",
				"providerName": "+919650059759",
				"providerFirstName": "Abhdh",
				"cat": "Cafes",
				"short_description": "Tasty food",
				"rating": 0,
				"expire_after": "None",
				"is_address_private": False,
				"keywords": [],
				"name_suggest": {
					"input": ["Eat", "street", "Eat street"],
					"output": "Eat street",
					"payload": {
						"cat": "Cafes",
						"service_id": "0d46210c-bba6-4903-a842-cbc16109eb7c"
					}
				},
				"views": 1,
				"media": [{
					"path": "https://s3.amazonaws.com/tnapp-dev/uploads/0d46210c-bba6-4903-a842-cbc16109eb7c/0/1540202420000"
				}],
				"created_at": "2018-10-22 10:01:24.101096+00:00",
				"is_active": True,
				"is_blocked": False,
				"is_verified": False,
				"location": {
					"lat": "12.91238800000000",
					"lon": "77.64034800000000"
				}
			},
			"sort": [1.3644361562470342, "24.101096"]
		}, {
			"_index": "services-list",
			"_type": "service",
			"_id": "f8228ef5-61bd-43ed-8ba1-bae710c388f1",
			"_score": "",
			"_source": {
				"cat": "Ad agencies",
				"is_blocked": False,
				"is_address_private": True,
				"created_at": "2018-06-28 07:40:01.816745+00:00",
				"views": 3,
				"providerName": "chaitra.badarinath@hashedin.com",
				"keywords": ["Test", "Baby"],
				"providerFirstName": "Chaitra",
				"location": {
					"lat": "12.91244800000000",
					"lon": "77.64037100000000"
				},
				"providerId": "6dd60782-b384-4425-80cd-6470f35fd644",
				"rating": 4,
				"name_suggest": {
					"input": ["Test", "Baby", "Such", "Such"],
					"payload": {
						"cat": "Ad agencies",
						"service_id": "f8228ef5-61bd-43ed-8ba1-bae710c388f1"
					},
					"output": "Such"
				},
				"is_active": True,
				"short_description": "Stockbridge",
				"expire_after": "",
				"is_verified": False,
				"media": [{
					"path": "https://s3.amazonaws.com/tnapp-dev/uploads/f8228ef5-61bd-43ed-8ba1-bae710c388f1/0/1530169593000"
				}],
				"name": "Such"
			},
			"sort": [1.3681258059066939, "40"]
		}, {
			"_index": "services-list",
			"_type": "service",
			"_id": "904d35a4-cc60-456d-9e1c-64d572e442cc",
			"_score": "",
			"_source": {
				"name": "twilio",
				"providerId": "de95a849-b224-4da8-b98d-a591a48476f9",
				"providerName": "+919816158734",
				"providerFirstName": "Ronald",
				"cat": "Others",
				"short_description": "archbishop if",
				"rating": 0,
				"expire_after": "",
				"is_address_private": True,
				"keywords": ["you", "hut", "mobile"],
				"name_suggest": {
					"input": ["you", "hut", "mobile", "twilio", "twilio"],
					"output": "twilio",
					"payload": {
						"cat": "Others",
						"service_id": "904d35a4-cc60-456d-9e1c-64d572e442cc"
					}
				},
				"views": 0,
				"media": [],
				"created_at": "2019-01-18 12:59:36.129593+00:00",
				"is_active": True,
				"is_blocked": False,
				"is_verified": False,
				"location": {
					"lat": "12.91241000000000",
					"lon": "77.64066000000000"
				}
			},
			"sort": [1.3990965338029364, "59"]
		}, {
			"_index": "services-list",
			"_type": "service",
			"_id": "559621b1-4cdf-4538-b469-f0f640af61ac",
			"_score": "",
			"_source": {
				"name": "Food",
				"providerId": "27720912-89a0-49b2-ba5d-8cfac14ab8f2",
				"providerName": "dikshant.agarwal@hashedin.com",
				"providerFirstName": "Dikshant",
				"cat": "Cafes",
				"short_description": "Tasty food",
				"rating": 0,
				"expire_after": "",
				"is_address_private": True,
				"keywords": [],
				"name_suggest": {
					"input": ["Food", "Food"],
					"output": "Food",
					"payload": {
						"cat": "Cafes",
						"service_id": "559621b1-4cdf-4538-b469-f0f640af61ac"
					}
				},
				"views": 4,
				"media": [],
				"created_at": "2018-05-29 06:21:34.496405+00:00",
				"is_active": True,
				"is_blocked": False,
				"is_verified": False,
				"location": {
					"lat": "12.91241000000000",
					"lon": "77.64066000000000"
				}
			},
			"sort": [1.3990965338029364, "34.496405"]
		}, {
			"_index": "services-list",
			"_type": "service",
			"_id": "a27e4865-bef2-4a77-84b2-d99147a205b0",
			"_score": "",
			"_source": {
				"name": "Sjgsjh",
				"providerId": "6b755e02-d84d-4313-b96a-6b786199cf4c",
				"providerName": "aravind.g@hashedin.com",
				"providerFirstName": "Aravind",
				"cat": "Auto Repair",
				"short_description": "Bzbgs",
				"rating": 0,
				"expire_after": "",
				"is_address_private": True,
				"keywords": ["Back"],
				"name_suggest": {
					"input": ["Back", "Sjgsjh", "Sjgsjh"],
					"output": "Sjgsjh",
					"payload": {
						"cat": "Auto Repair",
						"service_id": "a27e4865-bef2-4a77-84b2-d99147a205b0"
					}
				},
				"views": 1,
				"media": [],
				"created_at": "2019-01-18 06:07:48.897110+00:00",
				"is_active": True,
				"is_blocked": False,
				"is_verified": False,
				"location": {
					"lat": "12.91189000000000",
					"lon": "77.64116900000000"
				}
			},
			"sort": [1.4467615585433438, "48.897110"]
		}, {
			"_index": "services-list",
			"_type": "service",
			"_id": "6373e243-4687-4741-8f83-031cfb662fcc",
			"_score": "",
			"_source": {
				"name": "Flower and florists",
				"providerId": "011b03f5-0f64-4b35-8e4e-52161d82df43",
				"providerName": "swatitwr8@gmail.com",
				"providerFirstName": "Loft",
				"cat": "Florists",
				"short_description": "new fresh flowers",
				"rating": 3.6666666666666665,
				"expire_after": "",
				"is_address_private": True,
				"keywords": [],
				"name_suggest": {
					"input": ["Flower", "and", "florists", "Flower and florists"],
					"output": "Flower and florists",
					"payload": {
						"cat": "Florists",
						"service_id": "6373e243-4687-4741-8f83-031cfb662fcc"
					}
				},
				"views": 4,
				"media": [{
					"path": "https://s3.amazonaws.com/tnapp-dev/uploads/6373e243-4687-4741-8f83-031cfb662fcc/0/2018-09-19T17-34-03-05-30"
				}, {
					"path": "https://s3.amazonaws.com/tnapp-dev/uploads/6373e243-4687-4741-8f83-031cfb662fcc/1/2018-10-16T01-02-36-05-30"
				}],
				"created_at": "2018-08-28 11:39:38.159595+00:00",
				"is_active": True,
				"is_blocked": False,
				"is_verified": False,
				"location": {
					"lat": "12.91386300000000",
					"lon": "77.64315200000000"
				}
			},
			"sort": [1.7034613561328042, "39"]
		}, {
			"_index": "services-list",
			"_type": "service",
			"_id": "c62bb000-2ab2-43cb-ac4f-96a1e598351b",
			"_score": "",
			"_source": {
				"name": "Did he",
				"providerId": "4f462ed9-3f00-4e75-a3ed-3702bd4fc464",
				"providerName": "mythrim1995@gmail.com",
				"providerFirstName": "Mythri",
				"cat": "Auto Repair",
				"short_description": "Design",
				"rating": 0,
				"expire_after": "",
				"is_address_private": False,
				"keywords": ["Right", "Gone"],
				"name_suggest": {
					"input": ["Right", "Gone", "Did", "he", "Did he"],
					"output": "Did he",
					"payload": {
						"cat": "Auto Repair",
						"service_id": "c62bb000-2ab2-43cb-ac4f-96a1e598351b"
					}
				},
				"views": 0,
				"media": [],
				"created_at": "2018-12-19 17:05:46.239269+00:00",
				"is_active": True,
				"is_blocked": False,
				"is_verified": False,
				"location": {
					"lat": "12.91652100000000",
					"lon": "77.64303200000000"
				}
			},
			"sort": [1.783246263156142, "46.239269"]
		}, {
			"_index": "services-list",
			"_type": "service",
			"_id": "17f91b1c-d52f-4ce9-8bec-fa578ffe6c6e",
			"_score": "",
			"_source": {
				"name": "Burger King",
				"providerId": "056783ea-1a96-4012-abe6-848d78ed4f98",
				"providerName": "manasa.m@hashedin.com",
				"providerFirstName": "New Service ",
				"cat": "Restaurants",
				"short_description": "Take a break from boredom. \nEat chiken fires, chiken keema burger, chocolate shake.",
				"rating": 0,
				"expire_after": "",
				"is_address_private": False,
				"keywords": ["burger", "French fries", "Cold drinks"],
				"name_suggest": {
					"input": ["burger", "French fries", "Cold drinks", "Burger", "King", "Burger King"],
					"output": "Burger King",
					"payload": {
						"cat": "Restaurants",
						"service_id": "17f91b1c-d52f-4ce9-8bec-fa578ffe6c6e"
					}
				},
				"views": 15,
				"media": [{
					"path": "https://s3.amazonaws.com/tnapp-dev/uploads/17f91b1c-d52f-4ce9-8bec-fa578ffe6c6e/0/1522851217000"
				}, {
					"path": "https://s3.amazonaws.com/tnapp-dev/uploads/17f91b1c-d52f-4ce9-8bec-fa578ffe6c6e/1/1522851224000"
				}, {
					"path": "https://s3.amazonaws.com/tnapp-dev/uploads/17f91b1c-d52f-4ce9-8bec-fa578ffe6c6e/2/1522851232000"
				}],
				"created_at": "2018-04-04 14:14:39.530245+00:00",
				"is_active": True,
				"is_blocked": False,
				"is_verified": False,
				"location": {
					"lat": "12.93507500000000",
					"lon": "77.61327500000000"
				}
			},
			"sort": [3.2237831543961555, "39.530245"]
		}, {
			"_index": "services-list",
			"_type": "service",
			"_id": "7c7f6ed8-571f-4822-9a06-83e7c25f5d81",
			"_score": "",
			"_source": {
				"name": "Dominos",
				"providerId": "056783ea-1a96-4012-abe6-848d78ed4f98",
				"providerName": "manasa.m@hashedin.com",
				"providerFirstName": "New Service ",
				"cat": "Restaurants",
				"short_description": "Good food is always cooking!\nGo ahead, order some yummy items",
				"rating": 0,
				"expire_after": "",
				"is_address_private": False,
				"keywords": ["Pizza", "Food", "Cold drinks"],
				"name_suggest": {
					"input": ["Pizza", "Food", "Cold drinks", "Dominos", "Dominos"],
					"output": "Dominos",
					"payload": {
						"cat": "Restaurants",
						"service_id": "7c7f6ed8-571f-4822-9a06-83e7c25f5d81"
					}
				},
				"views": 8,
				"media": [{
					"path": "https://s3.amazonaws.com/tnapp-dev/uploads/7c7f6ed8-571f-4822-9a06-83e7c25f5d81/0/1522851810000"
				}, {
					"path": "https://s3.amazonaws.com/tnapp-dev/uploads/7c7f6ed8-571f-4822-9a06-83e7c25f5d81/1/1522851821000"
				}],
				"created_at": "2018-04-04 14:24:16.568354+00:00",
				"is_active": True,
				"is_blocked": False,
				"is_verified": False,
				"location": {
					"lat": "12.94036000000000",
					"lon": "77.62516800000000"
				}
			},
			"sort": [3.364066524064367, "24"]
		}]
	}
},
            status=status.HTTP_200_OK
        )


@permission_classes([])
class FollowingServicesView(APIView):
    def get(self, request):
        return Response(
            data= {
	"took": 4,
	"timed_out": False,
	"_shards": {
		"total": 5,
		"successful": 5,
		"failed": 0
	},
	"hits": {
		"total": 39,
		"max_score": "",
		"hits": [{
			"_index": "services-list",
			"_type": "service",
			"_id": "ff35f11d-0229-4c4a-82d1-e2c9e13718b4",
			"_score": "",
			"_source": {
				"name": "The hgeVDsbf",
				"providerId": "6b755e02-d84d-4313-b96a-6b786199cf4c",
				"providerName": "aravind.g@hashedin.com",
				"providerFirstName": "Aravind",
				"cat": "Banks-ATMs",
				"short_description": "Fhsfdhfhd",
				"rating": 0,
				"expire_after": "",
				"is_address_private": True,
				"keywords": ["Back"],
				"name_suggest": {
					"input": ["Back", "The", "hgeVDsbf", "The hgeVDsbf"],
					"output": "The hgeVDsbf",
					"payload": {
						"cat": "Banks-ATMs",
						"service_id": "ff35f11d-0229-4c4a-82d1-e2c9e13718b4"
					}
				},
				"views": 1,
				"media": [],
				"created_at": "2019-01-18 06:15:17.380172+00:00",
				"is_active": True,
				"is_blocked": False,
				"is_verified": False,
				"location": {
					"lat": "12.91237900000000",
					"lon": "77.64027600000000"
				}
			},
			"sort": [1.3563758331506583, "2019"]
		}, {
			"_index": "services-list",
			"_type": "service",
			"_id": "0d46210c-bba6-4903-a842-cbc16109eb7c",
			"_score": "",
			"_source": {
				"name": "Eat street",
				"providerId": "68dabf25-89ad-4237-a94e-b0e4d59a346a",
				"providerName": "+919650059759",
				"providerFirstName": "Abhdh",
				"cat": "Cafes",
				"short_description": "Tasty food",
				"rating": 0,
				"expire_after": "None",
				"is_address_private": False,
				"keywords": [],
				"name_suggest": {
					"input": ["Eat", "street", "Eat street"],
					"output": "Eat street",
					"payload": {
						"cat": "Cafes",
						"service_id": "0d46210c-bba6-4903-a842-cbc16109eb7c"
					}
				},
				"views": 1,
				"media": [{
					"path": "https://s3.amazonaws.com/tnapp-dev/uploads/0d46210c-bba6-4903-a842-cbc16109eb7c/0/1540202420000"
				}],
				"created_at": "2018-10-22 10:01:24.101096+00:00",
				"is_active": True,
				"is_blocked": False,
				"is_verified": False,
				"location": {
					"lat": "12.91238800000000",
					"lon": "77.64034800000000"
				}
			},
			"sort": [1.3644361562470342, "24.101096"]
		}, {
			"_index": "services-list",
			"_type": "service",
			"_id": "f8228ef5-61bd-43ed-8ba1-bae710c388f1",
			"_score": "",
			"_source": {
				"cat": "Ad agencies",
				"is_blocked": False,
				"is_address_private": True,
				"created_at": "2018-06-28 07:40:01.816745+00:00",
				"views": 3,
				"providerName": "chaitra.badarinath@hashedin.com",
				"keywords": ["Test", "Baby"],
				"providerFirstName": "Chaitra",
				"location": {
					"lat": "12.91244800000000",
					"lon": "77.64037100000000"
				},
				"providerId": "6dd60782-b384-4425-80cd-6470f35fd644",
				"rating": 4,
				"name_suggest": {
					"input": ["Test", "Baby", "Such", "Such"],
					"payload": {
						"cat": "Ad agencies",
						"service_id": "f8228ef5-61bd-43ed-8ba1-bae710c388f1"
					},
					"output": "Such"
				},
				"is_active": True,
				"short_description": "Stockbridge",
				"expire_after": "",
				"is_verified": False,
				"media": [{
					"path": "https://s3.amazonaws.com/tnapp-dev/uploads/f8228ef5-61bd-43ed-8ba1-bae710c388f1/0/1530169593000"
				}],
				"name": "Such"
			},
			"sort": [1.3681258059066939, "40"]
		}, {
			"_index": "services-list",
			"_type": "service",
			"_id": "904d35a4-cc60-456d-9e1c-64d572e442cc",
			"_score": "",
			"_source": {
				"name": "twilio",
				"providerId": "de95a849-b224-4da8-b98d-a591a48476f9",
				"providerName": "+919816158734",
				"providerFirstName": "Ronald",
				"cat": "Others",
				"short_description": "archbishop if",
				"rating": 0,
				"expire_after": "",
				"is_address_private": True,
				"keywords": ["you", "hut", "mobile"],
				"name_suggest": {
					"input": ["you", "hut", "mobile", "twilio", "twilio"],
					"output": "twilio",
					"payload": {
						"cat": "Others",
						"service_id": "904d35a4-cc60-456d-9e1c-64d572e442cc"
					}
				},
				"views": 0,
				"media": [],
				"created_at": "2019-01-18 12:59:36.129593+00:00",
				"is_active": True,
				"is_blocked": False,
				"is_verified": False,
				"location": {
					"lat": "12.91241000000000",
					"lon": "77.64066000000000"
				}
			},
			"sort": [1.3990965338029364, "59"]
		}, {
			"_index": "services-list",
			"_type": "service",
			"_id": "559621b1-4cdf-4538-b469-f0f640af61ac",
			"_score": "",
			"_source": {
				"name": "Food",
				"providerId": "27720912-89a0-49b2-ba5d-8cfac14ab8f2",
				"providerName": "dikshant.agarwal@hashedin.com",
				"providerFirstName": "Dikshant",
				"cat": "Cafes",
				"short_description": "Tasty food",
				"rating": 0,
				"expire_after": "",
				"is_address_private": True,
				"keywords": [],
				"name_suggest": {
					"input": ["Food", "Food"],
					"output": "Food",
					"payload": {
						"cat": "Cafes",
						"service_id": "559621b1-4cdf-4538-b469-f0f640af61ac"
					}
				},
				"views": 4,
				"media": [],
				"created_at": "2018-05-29 06:21:34.496405+00:00",
				"is_active": True,
				"is_blocked": False,
				"is_verified": False,
				"location": {
					"lat": "12.91241000000000",
					"lon": "77.64066000000000"
				}
			},
			"sort": [1.3990965338029364, "34.496405"]
		}, {
			"_index": "services-list",
			"_type": "service",
			"_id": "a27e4865-bef2-4a77-84b2-d99147a205b0",
			"_score": "",
			"_source": {
				"name": "Sjgsjh",
				"providerId": "6b755e02-d84d-4313-b96a-6b786199cf4c",
				"providerName": "aravind.g@hashedin.com",
				"providerFirstName": "Aravind",
				"cat": "Auto Repair",
				"short_description": "Bzbgs",
				"rating": 0,
				"expire_after": "",
				"is_address_private": True,
				"keywords": ["Back"],
				"name_suggest": {
					"input": ["Back", "Sjgsjh", "Sjgsjh"],
					"output": "Sjgsjh",
					"payload": {
						"cat": "Auto Repair",
						"service_id": "a27e4865-bef2-4a77-84b2-d99147a205b0"
					}
				},
				"views": 1,
				"media": [],
				"created_at": "2019-01-18 06:07:48.897110+00:00",
				"is_active": True,
				"is_blocked": False,
				"is_verified": False,
				"location": {
					"lat": "12.91189000000000",
					"lon": "77.64116900000000"
				}
			},
			"sort": [1.4467615585433438, "48.897110"]
		}, {
			"_index": "services-list",
			"_type": "service",
			"_id": "6373e243-4687-4741-8f83-031cfb662fcc",
			"_score": "",
			"_source": {
				"name": "Flower and florists",
				"providerId": "011b03f5-0f64-4b35-8e4e-52161d82df43",
				"providerName": "swatitwr8@gmail.com",
				"providerFirstName": "Loft",
				"cat": "Florists",
				"short_description": "new fresh flowers",
				"rating": 3.6666666666666665,
				"expire_after": "",
				"is_address_private": True,
				"keywords": [],
				"name_suggest": {
					"input": ["Flower", "and", "florists", "Flower and florists"],
					"output": "Flower and florists",
					"payload": {
						"cat": "Florists",
						"service_id": "6373e243-4687-4741-8f83-031cfb662fcc"
					}
				},
				"views": 4,
				"media": [{
					"path": "https://s3.amazonaws.com/tnapp-dev/uploads/6373e243-4687-4741-8f83-031cfb662fcc/0/2018-09-19T17-34-03-05-30"
				}, {
					"path": "https://s3.amazonaws.com/tnapp-dev/uploads/6373e243-4687-4741-8f83-031cfb662fcc/1/2018-10-16T01-02-36-05-30"
				}],
				"created_at": "2018-08-28 11:39:38.159595+00:00",
				"is_active": True,
				"is_blocked": False,
				"is_verified": False,
				"location": {
					"lat": "12.91386300000000",
					"lon": "77.64315200000000"
				}
			},
			"sort": [1.7034613561328042, "39"]
		}, {
			"_index": "services-list",
			"_type": "service",
			"_id": "c62bb000-2ab2-43cb-ac4f-96a1e598351b",
			"_score": "",
			"_source": {
				"name": "Did he",
				"providerId": "4f462ed9-3f00-4e75-a3ed-3702bd4fc464",
				"providerName": "mythrim1995@gmail.com",
				"providerFirstName": "Mythri",
				"cat": "Auto Repair",
				"short_description": "Design",
				"rating": 0,
				"expire_after": "",
				"is_address_private": False,
				"keywords": ["Right", "Gone"],
				"name_suggest": {
					"input": ["Right", "Gone", "Did", "he", "Did he"],
					"output": "Did he",
					"payload": {
						"cat": "Auto Repair",
						"service_id": "c62bb000-2ab2-43cb-ac4f-96a1e598351b"
					}
				},
				"views": 0,
				"media": [],
				"created_at": "2018-12-19 17:05:46.239269+00:00",
				"is_active": True,
				"is_blocked": False,
				"is_verified": False,
				"location": {
					"lat": "12.91652100000000",
					"lon": "77.64303200000000"
				}
			},
			"sort": [1.783246263156142, "46.239269"]
		}, {
			"_index": "services-list",
			"_type": "service",
			"_id": "17f91b1c-d52f-4ce9-8bec-fa578ffe6c6e",
			"_score": "",
			"_source": {
				"name": "Burger King",
				"providerId": "056783ea-1a96-4012-abe6-848d78ed4f98",
				"providerName": "manasa.m@hashedin.com",
				"providerFirstName": "New Service ",
				"cat": "Restaurants",
				"short_description": "Take a break from boredom. \nEat chiken fires, chiken keema burger, chocolate shake.",
				"rating": 0,
				"expire_after": "",
				"is_address_private": False,
				"keywords": ["burger", "French fries", "Cold drinks"],
				"name_suggest": {
					"input": ["burger", "French fries", "Cold drinks", "Burger", "King", "Burger King"],
					"output": "Burger King",
					"payload": {
						"cat": "Restaurants",
						"service_id": "17f91b1c-d52f-4ce9-8bec-fa578ffe6c6e"
					}
				},
				"views": 15,
				"media": [{
					"path": "https://s3.amazonaws.com/tnapp-dev/uploads/17f91b1c-d52f-4ce9-8bec-fa578ffe6c6e/0/1522851217000"
				}, {
					"path": "https://s3.amazonaws.com/tnapp-dev/uploads/17f91b1c-d52f-4ce9-8bec-fa578ffe6c6e/1/1522851224000"
				}, {
					"path": "https://s3.amazonaws.com/tnapp-dev/uploads/17f91b1c-d52f-4ce9-8bec-fa578ffe6c6e/2/1522851232000"
				}],
				"created_at": "2018-04-04 14:14:39.530245+00:00",
				"is_active": True,
				"is_blocked": False,
				"is_verified": False,
				"location": {
					"lat": "12.93507500000000",
					"lon": "77.61327500000000"
				}
			},
			"sort": [3.2237831543961555, "39.530245"]
		}, {
			"_index": "services-list",
			"_type": "service",
			"_id": "7c7f6ed8-571f-4822-9a06-83e7c25f5d81",
			"_score": "",
			"_source": {
				"name": "Dominos",
				"providerId": "056783ea-1a96-4012-abe6-848d78ed4f98",
				"providerName": "manasa.m@hashedin.com",
				"providerFirstName": "New Service ",
				"cat": "Restaurants",
				"short_description": "Good food is always cooking!\nGo ahead, order some yummy items",
				"rating": 0,
				"expire_after": "",
				"is_address_private": False,
				"keywords": ["Pizza", "Food", "Cold drinks"],
				"name_suggest": {
					"input": ["Pizza", "Food", "Cold drinks", "Dominos", "Dominos"],
					"output": "Dominos",
					"payload": {
						"cat": "Restaurants",
						"service_id": "7c7f6ed8-571f-4822-9a06-83e7c25f5d81"
					}
				},
				"views": 8,
				"media": [{
					"path": "https://s3.amazonaws.com/tnapp-dev/uploads/7c7f6ed8-571f-4822-9a06-83e7c25f5d81/0/1522851810000"
				}, {
					"path": "https://s3.amazonaws.com/tnapp-dev/uploads/7c7f6ed8-571f-4822-9a06-83e7c25f5d81/1/1522851821000"
				}],
				"created_at": "2018-04-04 14:24:16.568354+00:00",
				"is_active": True,
				"is_blocked": False,
				"is_verified": False,
				"location": {
					"lat": "12.94036000000000",
					"lon": "77.62516800000000"
				}
			},
			"sort": [3.364066524064367, "24"]
		}]
	}
},
            status=status.HTTP_200_OK
        )


