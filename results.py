from bs4 import BeautifulSoup
import mechanize
import urllib2
# Create a Browser
y = '1999'
f = open("test.txt",'w')
fl=0
for i in range(1,13):
    for j in range(1,32):
        b = mechanize.Browser()
        b.set_handle_robots(False)
        b.open('http://cbseresults.nic.in/jee_main_zxc/jee_cbse_2017.htm')
        b.select_form(name='FrontPage_Form1')
        #Replace Register Number
        b['regno'] = '17805935'
        d = str(j)
        m = str(i)
        if i<10:
            d = '0'+d
        if m<10:
            m = '0'+m
        b['dob'] = d+"/"+m+"/"+y
        fd = b.submit()
        soup = BeautifulSoup(fd.read(),'html.parser')
        tables = soup.findAll("b")
        for table in tables:
            for row in table.findAll("tr"):
                if tables[1].getText().encode('ascii', 'ignore').decode('ascii').strip()=='Result Not Found Please verify your Roll Number/DOB and try again here':
                    continue;
                print(j," ",i," ",y)
                fl = 1
                break
            if fl==1:
                break;
if fl==1:
   	print("Found")
else:
   	print("Not Found")
