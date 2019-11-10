import json

class searchProgram:
	Results = {}

	print("Welcom to Search")

	try:
		x = int(input("Please Select 1) for users, 2) for Organizations, 3) for Tickets: "))
	
		#If select 1, it will search for users
		if x == 1 :

			with open('users.json') as data_file:    
				data = json.load(data_file)

			u = input('Select 1) to search from Name or 2) to search from id: ')

			if u == 1:

				new = raw_input('Please input name to search: ')

				with open('organizations.json') as data_file:    
						cv = json.load(data_file)

				with open('tickets.json') as data_file:    
						cv2 = json.load(data_file)

				
				Udata = {}
				user = []
				for c in data:
					if (c["name"] == new):
						ds = {}
						ds["url"] = c["url"]
						ds["_id"] = c["_id"]
						ds["external_id"] = c["external_id"]
						ds["tags"] = c["tags"]
						ds["tags"] = c["organization_id"]

						user.append(ds)
						x = c["organization_id"]
				Udata["Users Data"] = user

				organizationD = []
				for l in cv:
					if l["_id"] == x:
						ws = {}
						ws["id"] = l["_id"]
						ws["url"] = l["url"]
						ws["external_id"] = l["external_id"]
						ws["name"] = l["name"]
						ws["domain_names"] = l["domain_names"]
						ws["created_at"] = l["created_at"]
						ws["details"] = l["details"]
						ws["shared_tickets"] = l["shared_tickets"]
						ws["tags"] = l["tags"]
						organizationD.append(ws)
				Udata["Organization data"] = organizationD

				try:
					ticket = []
					for h in cv2:
						if h["organization_id"] == x:
							ts = {}
							ts["Ticket ID"] = h["_id"]
							ts["Ticket URL"] = h["url"]
							ts["Ticket Organization ID"] = h["organization_id"]
							ticket.append(ts)
							Udata["Ticket data"] = ticket
			
				except KeyError:
					pass

				Results = Udata
				print(Results)

			elif u == 2:

				new2 = int(input('Please input _id to search: '))

				with open('organizations.json') as data_file:    
						cv = json.load(data_file)

				with open('tickets.json') as data_file:    
						cv2 = json.load(data_file)

				Udata = {}
				user = []
				for c in data:
					if (c["_id"] == new2):
						ds = {}
						ds["url"] = c["url"]
						ds["name"] = c["name"]
						ds["external_id"] = c["external_id"]
						ds["tags"] = c["tags"]
						ds["organization_id"] = c["organization_id"]
						user.append(ds)
						Udata["Users data"] = user

						x = c["organization_id"]

				organizationD = []
				for l in cv:
					if l["_id"] == x:
						ws = {}
						ws["_id"] = l["_id"]
						ws["url"] = l["url"]
						ws["external_id"] = l["external_id"]
						ws["name"] = l["name"]
						ws["domain_names"] = l["domain_names"]
						ws["created_at"] = l["created_at"]
						ws["details"] = l["details"]
						ws["shared_tickets"] = l["shared_tickets"]
						ws["tags"] = l["tags"]
						organizationD.append(ws)
						Udata["Organization data"] = organizationD

				try:
					ticket = []
					for h in cv2:
						if h["organization_id"] == x:
							ts = {}
							ts["_id"] = h["_id"]
							ts["url"] = h["url"]
							ts["organization_id"] = h["organization_id"]
							ticket.append(ts)
							Udata["Ticket data"] = ticket
				except KeyError:
					pass

				Results = Udata
				print(Results)

		#Select 2 to search for organization data		
		elif x == 2 :

			with open('organizations.json') as data_file:    
				data = json.load(data_file)

			u = input('Select 1) to search from Organization Name or 2) to search from Organization id: ')

			if u == 1:

				org = raw_input('Please input  Organization name to search: ')

				with open('users.json') as data_file:    
						cv = json.load(data_file)

				with open('tickets.json') as data_file:    
						cv2 = json.load(data_file)

				Udata = {}	
				organizationD = []
				for c in data:
					if (c["name"] == org):
						ws = {}
						ws["_id"] = c["_id"]
						ws["external_id"] = c["external_id"]
						ws["name"] = c["name"]
						ws["domain_names"] = c["domain_names"]
						ws["created_at"] = c["created_at"]
						ws["details"] = c["details"]
						ws["shared_tickets"] = c["shared_tickets"]
						ws["tags"] = c["tags"]
						organizationD.append(ws)
						Udata["Organization data"] = organizationD

						x = c["_id"]

				try:
					user = []		
					for l in cv:
						if l["organization_id"] == x:
							ds = {}
							ds["url"] = l["url"]
							ds["_id"] = l["_id"]
							ds["external_id"] = l["external_id"]
							ds["tags"] = l["tags"]
							ds["organization_id"] = l["organization_id"]
							user.append(ws)
							Udata["Organization data"] = user
				except KeyError:
					pass

				try:
					ticket = []
					for h in cv2:
						if h["organization_id"] == x:
							ts = {}
							ts["_id"] = h["_id"]
							ts["url"] = h["url"]
							ts["organization_id"] = h["organization_id"]
							ticket.append(ts)
							Udata["Organization data"] = ticket
				except KeyError:
					pass

					Results = Udata
					print(Results)			

			elif u == 2:

				org = int(input('Please input _id to search: '))

				with open('users.json') as data_file:    
						cv = json.load(data_file)

				with open('tickets.json') as data_file:    
						cv2 = json.load(data_file)

				Udata = {}	
				organizationD = []
				for c in data:
					if (c["_id"] == org):
						ws = {}
						ws["_id"] = c["_id"]
						ws["url"] = c["url"]
						ws["external_id"] = c["external_id"]
						ws["name"] = c["name"]
						ws["domain_names"] = c["domain_names"]
						ws["created_at"] = c["created_at"]
						ws["details"] = c["details"]
						ws["shared_tickets"] = c["shared_tickets"]
						ws["tags"] = c["tags"]
						organizationD.append(ws)
						Udata["Organization data"] = organizationD

						x = c["_id"]

				for l in cv:
					user = []	
					if l["organization_id"] == x:
						ds = {}
						ds["_id"] = l["_id"]
						ds["url"] = l["url"]
						ds["name"] = l["name"]
						ds["external_id"] = l["external_id"]
						ds["tags"] = l["tags"]	
						user.append(ds)
						Udata["User data"] = user

				try:
					ticket = []
					for h in cv2:
						if h["organization_id"] == x:
							ts = {}
							ts["_id"] = h["_id"]
							ts["url"] = h["url"]
							ts["organization_id"] = h["organization_id"]
							ticket.append(ts)
							Udata["Ticket data"] = ticket

				except KeyError:
					pass

				Results = Udata
				print(Results)
			
		#Select 3 for tickets data		
		elif x == 3:

			with open('tickets.json') as data_file:    
				data = json.load(data_file)

			tik = raw_input('Please input ticket ID to search: ')
			print(tik)

			with open('organizations.json') as data_file:    
				cv = json.load(data_file)

			with open('users.json') as data_file:    
				cv2 = json.load(data_file)

			Udata = {}
			ticket = []
			for h in data:
				if h["_id"] == tik:
					ts = {}
					ts["_id"] = h["_id"]
					ts["url"] = h["url"]
					ts["organization_id"] = h["organization_id"]
					ticket.append(ts)
					Udata["Ticket data"] = ticket
					x = h["organization_id"]
				
			organizationD = []
			for c in cv:
				if (c["_id"] == x):
					ws = {}
					ws["_id"] = c["_id"]
					ws["external_id"] = c["external_id"]
					ws["name"] = c["name"]
					ws["domain_names"] = c["domain_names"]
					ws["created_at"] = c["created_at"]
					ws["details"] = c["details"]
					ws["shared_tickets"] = c["shared_tickets"]
					ws["tags"] = c["tags"]
					organizationD.append(ws)
					Udata["Organization data"] = organizationD

			try:
				user = []		
				for l in cv2:
					if l["organization_id"] == x:
						ds = {}
						ds["url"] = l["url"]
						ds["_id"] = l["_id"]
						ds["external_id"] = l["external_id"]
						ds["tags"] = l["tags"]
						ds["organization_id"] = l["organization_id"]
						user.append(ds)
						Udata["User data"] = user
			except NameError:
				pass

			Results = Udata
			print(Results)

		else :
			print('Invalid Options Selected!')

	except (ValueError):
		print("Invalid option has been selected, program will be terminated!")
		
	