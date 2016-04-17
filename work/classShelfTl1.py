#!/home/mfaisal/usr/python/bin/python3
import time, sys, random, re, csv, subprocess, os, getpass, datetime, errno
sys.path.append('/home/mfaisal/usr/python/scripts/.lib')
from terminal3 import Terminal
from conn3 import Conn
from colorama import Fore, Back, Style

os.system('clear')

#====================================================================================================
### Global variables

tl1Prompt = 'M\s+\w+\s+\w+.*\r\n;\r\n<'


#====================================================================================================
class ShelfTl1:

	def __init__(self, ip, port, protocol):
		self.ip = ip
		self.port = port
		self.protocol = protocol
		
		
					
#====================================================================================================	
	def connectToShelf(self):		
		
		check = ''
		user_id = getpass.getuser()
		date = datetime.datetime.now()		
		path = '/opt/corp/projects/verif/ome/' + user_id + '/' + 'python' + '/' + date.strftime("%Y") + '/' + date.strftime("%B") + '/' +  date.strftime("%d") + '/'
		os.makedirs(path,exist_ok=True)
		
		self.conn_name = Conn(self.ip, protocol=self.protocol, interface='tl1', port=self.port, print_resp=False)
		check_tl1 =	self.conn_name.connect(logfile = path+'scriptLogs.txt')
		#check_tl1 = self.conn_name.connect(logfile=None)
		
		if check_tl1[0] == True:
			self.conn_name.tl1_login(login='ADMIN', pw='CHALLENGE')
		elif check_tl1[0] == False:
			return False	
			
			
			
#====================================================================================================
	def getChannel(self, user_key):
### getting channel numbers corresponding to wavelength
		
		self.user_key = user_key

		channel_dict = {'1528.77' : '1528.77(93)','1530.33' : '1530.33(1)','1530.72' : '1530.72(2)','1531.12' : '1531.12(3)','1531.51' : '1531.51(4)','1531.90' : '1531.90(5)','1532.29' : '1532.29(6)','1532.68' : '1532.68(7)','1533.07' : '1533.07(8)','1533.47' :'1533.47(9)','1533.86' : '1533.86(10)','1534.25' : '1534.25(11)','1534.64' : '1534.64(12)','1535.04' : '1535.04(13)','1535.43' : '1535.43(14)','1535.82' : '1535.82(15)','1536.22' : '1536.22(16)','1536.61' : '1536.61(17)','1537.00' : '1537.00(18)','1537.40' : '1537.40(19)','1537.79' : '1537.79(20)','1538.19' : '1538.19(21)','1538.58' : '1538.58(22)','1538.98' : '1538.98(23)','1539.37' : '1539.37(24)','1539.77' : '1539.77(25)','1540.16' : '1540.16(26)','1540.56' : '1540.56(27)','1540.95' : '1540.95(28)','1541.35' : '1541.35(29)','1541.75' : '1541.75(30)','1542.14' : '1542.14(31)','1542.54' : '1542.54(32)','1542.94' : '1542.94(33)','1543.33' : '1543.33(34)','1543.73' : '1543.73(35)','1544.13' : '1544.13(36)','1544.53' : '1544.53(37)','1544.92' : '1544.92(38)','1545.32' : '1545.32(39)','1545.72' : '1545.72(40)','1546.12' : '1546.12(41)','1546.52' : '1546.52(42)','1546.92' : '1546.92(43)','1547.32' : '1547.32(44)','1547.72' : '1547.72(45)','1548.11' : '1548.11(46)','1548.51' : '1548.51(47)','1548.91' : '1548.91(48)','1549.32' : '1549.32(49)','1549.72' : '1549.72(50)','1550.12' : '1550.12(51)','1550.52' : '1550.52(52)','1550.92' : '1550.92(53)','1551.32' : '1551.32(54)','1551.72' : '1551.72(55)','1552.12' : '1552.12(56)','1552.52' : '1552.52(57)','1552.93' : '1552.93(58)','1553.33' : '1553.33(59)','1553.73' :'1553.73(60)','1554.13' : '1554.13(61)','1554.54' : '1554.54(62)','1554.94' : '1554.94(63)','1555.34' : '1555.34(64)','1555.75' : '1555.75(65)','1556.15' : '1556.15(66)','1556.55' : '1556.55(67)','1556.96' : '1556.96(68)','1557.36' : '1557.36(69)','1557.77' : '1557.77(70)','1558.17' : '1558.17(71)','1558.58' : '1558.58(72)','1558.98' : '1558.98(73)','1559.39' : '1559.39(74)','1559.79' : '1559.79(75)','1560.20' : '1560.20(76)','1560.61' : '1560.61(77)','1561.01' : '1561.01(78)','1561.42' : '1561.42(79)','1561.83' : '1561.83(80)','1562.23' : '1562.23(81)','1562.64' : '1562.64(82)','1563.05' : '1563.05(83)','1563.45' : '1563.45(84)','1563.86' : '1563.86(85)','1564.27' : '1564.27(86)','1564.68' : '1564.68(87)','1565.09' : '1565.09(88)'
}	

		return (channel_dict[user_key])
		
		
		
#====================================================================================================	
	def getOsrp(self):
### Retrieves OSRP node name and adds to the file
	 
		osrp_found = ''
		cmd = self.conn_name.send('RTRV-OSRP::ALL:A;')

		pattern = r'NODENAME=\S+[\"](\S+)[\\][\"],NODEID'
		search = re.search(pattern, cmd[2])

		if search:
			self.osrp_found = str(search.group(1))
			#writetofile(osrp, tid)
		else:
			self.osrp_found = 'NO OSRP NODES FOUND'
		
		return self.osrp_found



#====================================================================================================	
	def getShelf(self):
### Retrieves shelf number for all the shelves in a captive

		cmd = self.conn_name.send_expect('RTRV-SHELF::ALL:A;',[tl1Prompt])
		search_shelf = re.search('SHELF-(\d+)::SITEID', cmd[2])
		
		if search_shelf:	
			self.shelf_id = search_shelf.group(1)
		else:
			self.shelf_id = 'No SHELF provisioned'
				
		return self.shelf_id	



#====================================================================================================
	def getTid(self):
### Retrieves TID (SID) name for all the shelves in a captive

		cmd = self.conn_name.send_expect('RTRV-SHELF::ALL:A;',[tl1Prompt])
		search_tid = re.search(r'[\"](.*)[\"] \d+\d+-\d+\d+', cmd[2])	
		
		if search_tid:
			self.tid_name = search_tid.group(1)
		else:
			self.tid_name = 'No TID found'
			
		return self.tid_name



#====================================================================================================
	def getExcessLoss(self):
### Runs a RTRV-ADJ-FIBER on a shelf and reports excess loss
	
		self.excess = {}
		self.excess_loss = {}

		cmd = self.conn_name.send_expect('RTRV-ADJ-FIBER::ALL:A;',[tl1Prompt])
		pattern = r'.+(ADJ\S+)::DRIFTTHRESH.+(EXCESSLOSS\S+),PADLOSS'	
		search = re.findall(pattern, cmd[2])

		if search:
			for item in search:
				self.excess.update({item[0] : item[1]})
		else:
			print ('ERROR: NO MATCHES FOUND')
			
		for key in self.excess:	
			value = self.excess[key]
			search_non_zero = re.search (r'EXCESSLOSS=(\S+)', value)
			if (search_non_zero.group(1)) != '0.00':
				self.excess_loss.update({key : value})

		if len(self.excess_loss) == 0:
			return False
		else:
			return self.excess_loss



#====================================================================================================
	def getFiberLoss(self, fiber_loss_check):
### Retrieves fiber loss greater than 1dB on all ADJ-FIBER facilities 

		self.fiber = {}
		self.fiber_loss = {}
		self.fiber_loss_check = fiber_loss_check
		
		cmd = self.conn_name.send_expect('RTRV-ADJ-FIBER::ALL:A;',[tl1Prompt])
		pattern = r'.+(ADJ\S+)::DRIFTTHRESH.+(FIBERLOSS\S+),PORTLABEL'
		search = re.findall(pattern, cmd[2])
		
		if search:
			for item in search:
				self.fiber.update({item[0] : item[1]})
		else:
			print ('ERROR: NO MATCHES FOUND')
			
		for key in self.fiber:	
			value = self.fiber[key]
			search_value = re.search (r'FIBERLOSS=(\S+)', value)
			if (search_value.group(1) != 'N/A') and (float (search_value.group(1)) > float(self.fiber_loss_check)):
				self.fiber_loss.update({key : value})
			
		if len(self.fiber_loss) == 0:
			return False
		else:
			return self.fiber_loss



#====================================================================================================
	def getSnc(self):
### Retrieves all the SNCs ...

		self.snc_label = []

		cmd = self.conn_name.send_expect('RTRV-SNC::ALL:A;', [tl1Prompt])

		pattern_label = r',LABEL=\\[\"](.*)\\[\"],LEP.+,SNCEPSTATE=ORIG'
		pattern_LEP = r',LEP=(.*),MAXADM.+,SNCEPSTATE=ORIG'
		pattern_REP = r',RMTEP=(.*),RMTNODE.+,SNCEPSTATE=ORIG'
	
		search_label = re.findall(pattern_label, cmd[2])
		search_LEP = re.findall(pattern_LEP, cmd[2])
		search_REP = re.findall(pattern_REP, cmd[2])
		
		if search_label and search_LEP and search_REP:
			for item in zip(search_label, search_LEP, search_REP):
				self.snc_label.append(item)
				
		return self.snc_label

		
				
#====================================================================================================
	def setClearStc(self):
### Puts AMP facility in AINS...return list of facilites that were put in AINS

		cmd = self.conn_name.send_expect('RTRV-COND-ALL::ALL:A;', [tl1Prompt])

		pattern_stc = r'[\"](\S+),AMP:MJ,STC_OTS'

		self.search_stc = re.findall(pattern_stc, cmd[2])

		if self.search_stc:
			for item in self.search_stc:
				cmd_clear = self.conn_name.send_expect('ED-AMP::' + item + ':CTAG::::,AINS;', [tl1Prompt])

		return self.search_stc
				
		
		
#====================================================================================================
	def setClearOptmonLoss(self):
### Puts OPTMON faicility in AINS

		cmd = self.conn_name.send_expect('RTRV-COND-ALL::ALL:A;', [tl1Prompt])

		pattern_loss = r'[\"](\S+),OPTMON:MJ,LOS_OTS'

		self.search_loss = re.findall(pattern_loss, cmd[2])
		
		if self.search_loss:
			for item in self.search_loss:
				cmd_clear = self.conn_name.send_expect('ED-OPTMON::' + item + ':CTAG::::,AINS;', [tl1Prompt])
					
		return self.search_loss		



#====================================================================================================
	def setDisableTelnet(self):
### Disables telnet
		ShelfTl1.getShelf(self)
		cmd = self.conn_name.send_expect('ED-TELNET::SHELF-' + self.shelf_id + ':CTAG:::SERVER=DISABLED;', [tl1Prompt])
		print (cmd[2])
		
		
		
#====================================================================================================		
	def close(self):
### Closing telnet/ssh sessions for main class
	
		self.conn_name.close()
		

#====================================================================================================
	def getShelfIp(self):
### Gets Shelf IP which in most cases is the same as OSPF Router IP
		
		ShelfTl1.getShelf(self)
		cmd_shelf_ip = self.conn_name.send_expect('RTRV-IP::SHELF-' + self.shelf_id + ':CTAG;', [tl1Prompt])
		
		self.search_shelf_ip = re.search(r'IPADDR=(\S+),NETMASK', cmd_shelf_ip[2])
		
		if self.search_shelf_ip:
			return self.search_shelf_ip.group(1)
		else:
			return ('Failed to retrieve Shelf IP')

#====================================================================================================
	def getEndPoints(self):
### Gets available end points on CCMD12/CCMD44/CCMD8x16 with paired transponders
		
		ShelfTl1.getTid(self)
		self.end_point_dict = {}	
		pattern_ocld = r'(\d+)-(\d+)-(\d+)-\S+'
		slot_ocld = ''
		
		cmd_adj_tx = self.conn_name.send_expect('RTRV-ADJ-TX::ALL:CTAG;', [tl1Prompt])	
		cmd_adj = self.conn_name.send_expect('RTRV-ADJ::ALL:CTAG;', [tl1Prompt])	
		
		self.search_adj_tx = re.findall(r'ADJ-(\S+)::ADJTXTYPE.+DISCTYPE=(\S+),SYNCPROV.+DISCWAVELENGTH=(\S+),MATEINFO', cmd_adj_tx[2])
		self.search_adj = re.findall(r'ADJ-(\S+)::ADJTYPE.+DISCFEADDR=[\\][\"](.*)[\\][\"],DADDRFORM', cmd_adj[2])
				
		#check if the discovered wavelength is non-zero ..
		#if true then set it as a key and lambda as its first value
		if self.search_adj_tx:
			for items in self.search_adj_tx:
				if float(items[2]) > 0.00:
					self.end_point_dict [str(items[0])] = [items[2]]
		
		
		
		#check if regex matches an existing key 
		#append DISCFEAADDRR value to the dict values (OCLD FEA)
		if self.search_adj:
			for items in self.search_adj:				
				if (items[0]) in self.end_point_dict:
					self.end_point_dict [str(items[0])].append(items[1])
				
		
		
		#to get PECs from transponders ...
		for key,value in self.end_point_dict.items():
						
			search_ocld = re.search(pattern_ocld, str(value[1])[::-1])
			if search_ocld:
				slot_ocld = search_ocld.group(3)[::-1] + '-' + search_ocld.group(2)[::-1]			
				cmd_ocld = self.conn_name.send_expect('RTRV-INVENTORY::SLOT-' + slot_ocld + ':CTAG;', [tl1Prompt])
				self.search_pec = re.search(r'PEC=(\S+),REL', cmd_ocld[2])
				if self.search_pec:
					self.end_point_dict[key].append(self.search_pec.group(1))
				else:
					self.end_point_dict[key].append('Err:PEC')			
					
			
			#Filling the status coloumn .. consider removing it
			if value[0] == '1528.77':
				self.end_point_dict[key].append('Available')
			elif value[0] is not '1528.77':
				self.end_point_dict[key].append('In Use')
			
			
			
			#Finding out SNC ID based on CMD ports (dict[key])
			cmd_crs = self.conn_name.send_expect('RTRV-CRS-OCH::ALL,ALL:CTAG;', [tl1Prompt])
			self.test = re.findall(r'SOURCEPORT=[\\][\"](.*)[\\][\"],SOURCEPORTFORM.*SNCCKTID=[\\][\"](.*)[\\][\"],PRIME=CPS',cmd_crs[2])
			for items in self.test:
				if (self.tid_name+'-'+key) == items[0]:
					self.end_point_dict[key].append(items[1])
							
			if value[0] == '1528.77':
				self.end_point_dict[key].append('Free_')
								

		print ('TID: ' + Fore.BLUE + self.tid_name + Fore.RESET + '\n')
		
		if len(self.end_point_dict) > 0:			
			print ('CMD port'.rjust(14)+'Channel'.rjust(14)+'Paired card'.rjust(32)+'PEC'.rjust(15)+'Status'.rjust(19)+'Status Info'.rjust(35))
			print ('-----------------------------------------------------------------------------------------------------------------------------------')
			for key,value in self.end_point_dict.items():
				user_key = value[0]
				chnum = ShelfTl1.getChannel(self, user_key)
				if len(value) == 5:
					print (('ADJ-'+key).rjust(14) + chnum.rjust(14) + value[1].rjust(32)+ value[2].rjust(15)+ value[3].rjust(19)+ value[4].rpartition('_')[0].rjust(35))
				elif len(value) == 4:
					self.end_point_dict[key].append('Err:NotFound_')
					print (('ADJ-'+key).rjust(14) + chnum.rjust(14) + value[1].rjust(32)+ value[2].rjust(15)+ value[3].rjust(19)+ value[4].rpartition('_')[0].rjust(35)) 
				else:
					print (key)
		else:
			print ('No paired transponders found at this site')

		
#====================================================================================================
	def findOtnFail(self):
### finds OTN CP Fails alarms only for 11.1ER load

		self.card_list = {}
		cmd = self.conn_name.send_expect('RTRV-COND-ALL::ALL:A;', [tl1Prompt])
		pattern_fail = r'[\"](\S+),EQPT:(\S+),EQPT_FAIL'

		search_fail = re.findall(pattern_fail, cmd[2])
		
		if search_fail:	
			for item in search_fail:
				if 'OTN' in item[0]:
					search_card = re.search (r'(\S+)-(\S+)-(\S+)', item[0])
					self.card_list[search_card.group(3)] = search_card.group(0)
				else:
					print ('not found')

		#print (self.card_list)
		return self.card_list


#====================================================================================================
	def DGN(self,card_list):
### DGN-EQPT for slots & AID provided 

		for key,value in self.card_list.items():
			print ('DGN-EQPT......')
			cmd2 = self.conn_name.send_expect('DGN-EQPT::'+value+':ctag;', [tl1Prompt])
			
			

#====================================================================================================
	def getWL3n(self):
### finds OTN CP Fails alarms only for 11.1ER load

		self.card_wl3n = {}
		cmd = self.conn_name.send_expect('RTRV-INVENTORY:::CTAG;', [tl1Prompt])
		pattern_wl3n = r'[\"]PKTOTN-(\S+)-(\S+)::CTYPE(.*),PEC=(\S+),REL'

		search_wl3n = re.findall(pattern_wl3n, cmd[2])
		
		if search_wl3n:	
			for item in search_wl3n:
				if 'NTK669A' in item[3]:
					self.card_wl3n[item[1]] = item[3] 
		if len (self.card_wl3n) > 0:
			print (self.card_wl3n)
		return self.card_wl3n	
		
