#!/home/mfaisal/usr/python/bin/python3
import sys, os, string, tty, termios, subprocess
sys.path.append('/home/mfaisal/usr/python/scripts/.lib')
from classShelfMon import *
from classShelfTl1 import *
from colorama import Fore, Back, Style

#====================================================================================================	
all_shelves = {}
primary_shelves = {}
system = {}
captive_choice = {}
sub_row_to_print = []
row_to_print = []


#====================================================================================================
def keyPress():
# takes care of keystrokes
	
	fd = sys.stdin.fileno()
	old_settings = termios.tcgetattr(fd)
	try:
		tty.setraw(sys.stdin.fileno())
		ch = sys.stdin.read(1)
	finally:
		termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
	return ch
	
	
#====================================================================================================
def countdown():
# 10 secs countdown before xterm closes

	for i in range(10,0,-1):
		sys.stdout.write(Fore.RED + "This window will close in ... " + format(i, '02d') + " seconds\r" + Fore.RESET)
		sys.stdout.flush()
		time.sleep(1)
	sys.exit('\n')

	
	
#====================================================================================================
def getSystem():
		
	with open('/opt/corp/projects/verif/ome/automain/.Captives.csv') as f:
		reader = csv.reader(f)
		for row in reader:
			if not row[0] in row_to_print:
				row_to_print.append(row[0])
			else:
				continue
	f.closed
	
	print('\n' + 'Choose a System Type')
	print('--------------------')

	count = 1
	for items in sorted(row_to_print)[:-1]:
		print (chr(count+64) + ')  ' + items)
		system [chr(count+64)] = items
		count += 1	
	print ('\n')
	print ("X)  Press 'X' to exit \n")	
	sys.stdout.write('\n'+'Select a system: ')
	system_input = keyPress().upper()

	os.system('clear')
	print ('System selected: ' + system[system_input] + '\n')
	with open('/opt/corp/projects/verif/ome/automain/.Captives.csv') as f:
		reader = csv.reader(f)
		for row in reader:
			if row[0] == system[system_input]:
				sub_row_to_print.append(row[1])
			else:
				continue
	f.closed	
		
	count = 1
	for items in sorted(set(sub_row_to_print)):
		print (chr(count+64) + ')  ' + items)
		captive_choice [chr(count+64)] = items
		count += 1	
	print ('\n')
	sys.stdout.write('\n'+'Select a captive: ')
	captive_select = keyPress().upper()

	return captive_choice[captive_select]



#====================================================================================================
def getSubSystem():

	shelf_name = []
	shelf_name_full = []
	shelf_name_dict = {}

	with open('/opt/corp/projects/verif/ome/automain/.Captives.csv') as f:	
		reader = csv.reader(f)

		for row in reader:
			if re.match(captiveName, row[1]) and re.match('47.13.', row[3]):
				_ome = re.search (r'OM.+_(.*)_T',row[2])
				_cpl = re.search (r'CPL_(.*)_T',row[2])
				_tseries = re.findall (r'65ts_(.*)_t',row[2])		
				if _ome:
					shelf_name_full.append (row[2])
				elif _cpl:
					shelf_name_full.append (row[2])
				elif _tseries:
					shelf_name_full.append (row[2])
				else:
					sys.exit ('Failed to get shelf names ... exiting now ....')
	f.closed
	
	count = 1
	for items in sorted(shelf_name_full):	
		print (chr(count+64) + ')  ' + items)
		shelf_name_dict [chr(count+64)] = items
		count += 1	

	return (shelf_name_dict)



#====================================================================================================
def shelfConnection():

	with open('/opt/corp/projects/verif/ome/automain/.Captives.csv') as f:	
		reader = csv.reader(f)

		for row in reader:
			if re.match(captiveName, row[1]) and re.match('47.13.', row[3]):
				search_shelf_ome = re.search (r'OM.+_(.*)_T',row[2]) or re.search (r'OM.+_(.*)_t',row[2]) or re.search (r't_C(.*)',row[2])
				search_shelf_cpl = re.search (r'CPL_(.*)_T',row[2]) or re.search (r'CPL_(.*)_t',row[2]) or re.search (r't_C(.*)',row[2])
				search_tseries = re.findall (r'65ts_(.*)_t',row[2])
				if search_shelf_ome:
					all_shelves[row[2]] = [row[3], row[7], row[8]]
				elif search_shelf_cpl:
					all_shelves[row[2]] = [row[3], row[7], row[8]]
				elif search_tseries:
					for item in search_tseries:
						all_shelves[row[2]] = [row[3], row[7], row[8]]	
				else:
					sys.exit ('Failed to retrieve IPs ... exiting now ....')
	f.closed

	check_primary = False
	for key,value in all_shelves.items():
		if re.search('.+(\d+P)', key) or re.search('.+(Pri)', key) or re.search('.+(PRI)', key) or re.search('.+(pri)', key): 
			primary_shelves[key] = value
			check_primary = True
	if check_primary == True:
		return primary_shelves
	elif check_primary == False:
		primary_shelves.update(all_shelves)
		return primary_shelves
	else:
		sys.exit ('Failed to retrieve PRIMARY IPs ... exiting now ....')
	


#====================================================================================================
def chooseFunction():

	os.system('clear')

	print ('\n')
	print ('****************************************')
	print ('********** UNDER CONSTRUCTION **********')
	print ('****************************************')
	print ('========================================')
	print ('      WELCOME TO PV TOOLS IN PYTHON')
	print ('========================================')
	print ('Contact: Fahd Faisal')
	print ('Captive selected: ' + Fore.WHITE + Back.BLUE + captiveName + Fore.RESET + Back.RESET)
	print ('\n')
	print ('Option 1 : Get OSRP names')
	print ('Option 2 : Get Shelf IDs')
	print ('Option 3 : Get TID names')
	print ('Option 4 : Check for non-zero provisioned Excess Loss')
	print ('Option 5 : Check for Fiber Loss greater than a custom defined value')
	print ('Option 6 : Get SNC Labels')
	print ('Option 7 : Put AMP facilities in AINS - L0CP on CDC Captives only ')
	print ('Option 8 : Put OPTMON facilities in AINS - L0CP on CDC Captives only')
	print ('Option 9 : Mon - Ping')
	print ('Option 10: Mon - Traceroute')
	print ('Option 11: Mon - Pixel Power')
	print ('Option 12: Disable Telnet')
	print ('Option 13: Find endpoints (SNCs for L0CP)')
	print ('Option 14: Clear CP Fail alarm on PKTOTN cards (11.1ER load only)')
	print ('Option 15: WL3n FPGA Load Upgrade - 11.1')
	print ('\n')

	try:
		option = input('Select an option number to run & press ENTER: ')
		#option = keyPress()
		#print ("\x1b[8;74;199t") #Sets screen size		
		os.system('clear')
		local_protocol = ''
	except KeyboardInterrupt:
		sys.exit('***Program terminated by user Ctrl-C, Exiting!!***')
		
	#--------------------------------------------------------------------------------	
	if option == '1':
		for key,values in primary_shelves.items():
			if values[1] == '23' or values[1] == '':
				local_protocol = 'telnet'
			else:
				local_protocol = 'ssh'
			shelf_telnet = ShelfTl1(values[0], values[1], local_protocol)
			if shelf_telnet.connectToShelf() == False:
				print ('Return value: False')
			else:
				print(shelf_telnet.getOsrp())
				shelf_telnet.close()

			
	#--------------------------------------------------------------------------------			
	elif option == '2':
		for key,values in all_shelves.items():
			if values[1] == '23' or values[1] == '':
				local_protocol = 'telnet'
			else:
				local_protocol = 'ssh'		
			shelf_telnet = ShelfTl1(values[0], values[1], local_protocol)
			
			if shelf_telnet.connectToShelf() == False:
				print ('Return value: False')
			else:
				print('Shelf ID: ' + shelf_telnet.getShelf())
				shelf_telnet.close()
			
			
	#--------------------------------------------------------------------------------			
	elif option == '3':
		for key,values in primary_shelves.items():
			if values[1] == '23' or values[1] == '':
				local_protocol = 'telnet'
			else:
				local_protocol = 'ssh'		
			shelf_telnet = ShelfTl1(values[0], values[1], local_protocol)
			if shelf_telnet.connectToShelf() == False:
				print ('Return value: False')
			else:
				print(shelf_telnet.getTid())
				shelf_telnet.close()
			
	#--------------------------------------------------------------------------------		
	elif option == '4':
		for key,values in all_shelves.items():
			if values[1] == '23' or values[1] == '':
				local_protocol = 'telnet'
			else:
				local_protocol = 'ssh'		
			shelf_telnet = ShelfTl1(values[0], values[1], local_protocol)
			if shelf_telnet.connectToShelf() == False:
				print ('Return value: False')
			else:
				try:
					for i,j in shelf_telnet.getExcessLoss().items():
						print (i,j)
				except:
					print ('No matching facilities found')
				shelf_telnet.close()
			
	#--------------------------------------------------------------------------------				
	elif option == '5':
		fiber_loss_check = input ('Enter the fiber loss threshold that you want to check: ')
		for key,values in all_shelves.items():
			if values[1] == '23' or values[1] == '':
				local_protocol = 'telnet'
			else:
				local_protocol = 'ssh'		
			shelf_telnet = ShelfTl1(values[0], values[1], local_protocol)
			if shelf_telnet.connectToShelf() == False:
				print ('Return value: False')
			else:
				try:
					for i,j in shelf_telnet.getFiberLoss(fiber_loss_check).items():
						print (i,j)
				except:
					print ('No matching facilities found')
				shelf_telnet.close()
			
	#--------------------------------------------------------------------------------		
	elif option == '6':
		for key,values in primary_shelves.items():
			if values[1] == '23' or values[1] == '':
				local_protocol = 'telnet'
			else:
				local_protocol = 'ssh'		
			shelf_telnet = ShelfTl1(values[0], values[1], local_protocol)
			if shelf_telnet.connectToShelf() == False:
				print ('Return value: False')
			else:
				if len(shelf_telnet.getSnc()) == 0:
					print ('No SNCs found')
				else:
					for snc in shelf_telnet.getSnc():
						print ('Label: '+snc[0]+',' , 'Start: '+snc[1]+',' , 'End: '+snc[2]) 
				shelf_telnet.close()
			
	#--------------------------------------------------------------------------------	
	elif option == '7':
		for key,values in all_shelves.items():
			if values[1] == '23' or values[1] == '':
				local_protocol = 'telnet'
			else:
				local_protocol = 'ssh'		
			shelf_telnet = ShelfTl1(values[0], values[1], local_protocol)
			if shelf_telnet.connectToShelf() == False:
				print ('Return value: False')
			else:
				stc_list = shelf_telnet.setClearStc()
				if len(stc_list) == 0:
					print ('No AMP facilites were put in AINS')
				else:
					print ('Following AMP facilities were put in AINS:')
				for item in stc_list:
					print (item)
				shelf_telnet.close()
			
	#--------------------------------------------------------------------------------				
	elif option == '8':
		for key,values in all_shelves.items():
			if values[1] == '23' or values[1] == '':
				local_protocol = 'telnet'
			else:
				local_protocol = 'ssh'		
			shelf_telnet = ShelfTl1(values[0], values[1], local_protocol)
			if shelf_telnet.connectToShelf() == False:
				print ('Return value: False')
			else:
				optmon_list = shelf_telnet.setClearOptmonLoss()
				if len(optmon_list) == 0:
					print ('No OPTMON facilites were put in AINS')
				else:
					print ('Following OPTMON facilities were put in AINS:')
					for item in optmon_list:
						print (item)
				shelf_telnet.close()
			
	#--------------------------------------------------------------------------------				
	elif option == '9':
		shelf_name_dict = getSubSystem()
		try:
			sys.stdout.write('\n' + 'Select the first shelf: ')
			shelf_1 = keyPress().upper()
			sys.stdout.write(shelf_name_dict[shelf_1])
			sys.stdout.write('\n' + 'Select the second shelf: ')
			shelf_2 = keyPress().upper()
			print(shelf_name_dict[shelf_2])
		except:
			print ('\n'+'Invalid selection')
			#countdown()
		for key,values in all_shelves.items():
			if values[1] == '23' or values[1] == '':
				local_protocol = 'telnet'
			else:
				local_protocol = 'ssh'	
			if key == shelf_name_dict[shelf_1]:
				shelf_telnet = ShelfTl1(values[0], values[1], local_protocol)
				shelf_telnet.connectToShelf()
				shelf_1_ip = shelf_telnet.getShelfIp()
				print ('Retrieving Shelf IP for the first shelf selected...')
				shelf_telnet.close()
			elif key == shelf_name_dict[shelf_2]:
				shelf_telnet = ShelfTl1(values[0], values[1], local_protocol)
				shelf_telnet.connectToShelf()
				shelf_2_ip = shelf_telnet.getShelfIp()
				print ('Retrieving Shelf IP for the second shelf selected...')
				shelf_telnet.close()		
		for key,values in all_shelves.items():
			if values[2] == '8888' or values[1] == '':
				local_protocol = 'telnet'
			else:
				local_protocol = 'ssh'	
			if key == shelf_name_dict[shelf_1]:
				shelf_mon = ShelfMon(values[0], values[2], local_protocol)
				shelf_mon.connectToShelf()
				shelf_mon.getPing(shelf_2_ip)			
			elif key == shelf_name_dict[shelf_2]:
				shelf_mon = ShelfMon(values[0], values[2], local_protocol)
				shelf_mon.connectToShelf()
				shelf_mon.getPing(shelf_1_ip)

	#--------------------------------------------------------------------------------	
	elif option == '10':
		shelf_name_dict = getSubSystem()
		try:
			sys.stdout.write('\n' + 'Select the first shelf: ')
			shelf_1 = keyPress().upper()
			sys.stdout.write(shelf_name_dict[shelf_1])
			sys.stdout.write('\n' + 'Select the second shelf: ')
			shelf_2 = keyPress().upper()
		except:
			print ('\n'+'Invalid selection')
			#countdown()
		print(shelf_name_dict[shelf_2])
		for key,values in all_shelves.items():
			if values[1] == '23' or values[1] == '':
				local_protocol = 'telnet'
			else:
				local_protocol = 'ssh'	
			if key == shelf_name_dict[shelf_1]:
				shelf_telnet = ShelfTl1(values[0], values[1], local_protocol)
				shelf_telnet.connectToShelf()
				shelf_1_ip = shelf_telnet.getShelfIp()
				print ('Retrieving Shelf IP for the first shelf selected...')
				shelf_telnet.close()
			elif key == shelf_name_dict[shelf_2]:
				shelf_telnet = ShelfTl1(values[0], values[1], local_protocol)
				shelf_telnet.connectToShelf()
				shelf_2_ip = shelf_telnet.getShelfIp()
				print ('Retrieving Shelf IP for the second shelf selected...')
				shelf_telnet.close()		
		for key,values in all_shelves.items():
			if values[2] == '8888' or values[1] == '':
				local_protocol = 'telnet'
			else:
				local_protocol = 'ssh'	
			if key == shelf_name_dict[shelf_1]:
				shelf_mon = ShelfMon(values[0], values[2], local_protocol)
				shelf_mon.connectToShelf()
				shelf_mon.getTraceRoute(shelf_2_ip)			
			elif key == shelf_name_dict[shelf_2]:
				shelf_mon = ShelfMon(values[0], values[2], local_protocol)
				shelf_mon.connectToShelf()
				shelf_mon.getTraceRoute(shelf_1_ip)
				
	#--------------------------------------------------------------------------------	
	elif option == '11':
			shelf_name_dict = getSubSystem()
			try:
				sys.stdout.write('\n' + 'Select a shelf: ')
				shelf_1 = keyPress().upper()
				sys.stdout.write(shelf_name_dict[shelf_1] + '\n')
				wss_slot = input ('Enter the WSS slot: ')
				channel_id = input ('Enter a channel number: ')
			except:
				print ('Invalid selection')
				#countdown()
			for key,values in all_shelves.items():
				if values[2] == '8888' or values[1] == '':
					local_protocol = 'telnet'
				else:
					local_protocol = 'ssh'	
				if key == shelf_name_dict[shelf_1]:
					shelf_mon = ShelfMon(values[0], values[2], local_protocol)
					sys.stdout.write('\n' + 'Do you want to retrieve in a continueous loop? (Y/N):   ' + '\n')
					true_loop = keyPress().upper()
					shelf_mon.connectToShelf()
					try:
						if true_loop.upper() == 'Y':
							while True:
								shelf_mon.getPixelPower(wss_slot, channel_id)		
						else:
							shelf_mon.getPixelPower(wss_slot, channel_id)	
					except:
						print ('\n' + 'Invalid entries...')
						#countdown()
						
	#--------------------------------------------------------------------------------	
	elif option == '12':
		for key,values in all_shelves.items():
			if values[1] == '23' or values[1] == '':
				local_protocol = 'telnet'
			else:
				local_protocol = 'ssh'		
			shelf_telnet = ShelfTl1(values[0], values[1], local_protocol)
			shelf_telnet.connectToShelf()
			print(shelf_telnet.setDisableTelnet())
			shelf_telnet.close()
	
	#--------------------------------------------------------------------------------	
	elif option == '13':
		for key,values in primary_shelves.items():
			if values[1] == '23' or values[1] == '':
				local_protocol = 'telnet'
			else:
				local_protocol = 'ssh'		
			shelf_telnet = ShelfTl1(values[0], values[1], local_protocol)
			shelf_telnet.connectToShelf()
			shelf_telnet.getEndPoints()
			shelf_telnet.close()

	#--------------------------------------------------------------------------------	
	elif option == '14':
		for key,values in all_shelves.items():
			if values[1] == '23' or values[1] == '':
				local_protocol = 'telnet'
			else:
				local_protocol = 'ssh'		
			shelf_telnet = ShelfTl1(values[0], values[1], local_protocol)
			shelf_telnet.connectToShelf()
			card_list = shelf_telnet.findOtnFail()
			if len(card_list) > 0:
				shelf_mon = ShelfMon(values[0], values[2], local_protocol)
				shelf_mon.connectToShelf()
				shelf_mon.ResetLowPower(card_list)
				shelf_telnet.DGN(card_list)
			shelf_telnet.close()

	#--------------------------------------------------------------------------------	
	elif option == '15':
		for key,values in all_shelves.items():
			if values[1] == '23' or values[1] == '':
				local_protocol = 'telnet'
			else:
				local_protocol = 'ssh'		
			shelf_telnet = ShelfTl1(values[0], values[1], local_protocol)
			shelf_telnet.connectToShelf()
			wl3n_dict = shelf_telnet.getWL3n()
			if len(wl3n_dict) > 0:
				shelf_mon = ShelfMon(values[0], values[2], local_protocol)
				shelf_mon.connectToShelf()
				shelf_mon.wl3nFPGA(wl3n_dict, values[0])
			shelf_telnet.close()
			
#====================================================================================================
def main():

	try:
		global captiveName 
		captiveName = getSystem()
		print (captiveName)
		shelfConnection()
	except KeyboardInterrupt:
		sys.exit('***Program terminated by user Ctrl-C, Exiting!!***')
	except:
		print('\n' + 'Failed to connect to shelves ... Exiting now!!' + '\n')
		#countdown()

	try:
		while True:
			chooseFunction()			
			print ('\n')
			sys.stdout.write('\n' + 'Do you want to run another function against the same captive? (Y/N):  ')
			continue_to_run = keyPress().upper()
			if continue_to_run == 'Y':
				continue
			else:
				print ('\n' + '***********************************************************************************')
				print (Fore.BLUE + 'For feedback/comments, please email Fahd Faisal <mfaisal@ciena.com> ' + Fore.RESET)
				print ('***********************************************************************************' + '\n')
				#countdown()
				break		
	except KeyboardInterrupt:
		sys.exit('***Program terminated by user Ctrl-C, Exiting!!***')




#====================================================================================================
if __name__ == "__main__":
	main()
